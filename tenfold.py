import json
import requests
import ast
BASE_URI = 'https://integration-tests-challenge.herokuapp.com'

def get_token_test():
    r = requests.post('{}/login'.format(BASE_URI),
                      data={'username': 'salesforce@tenfold.com', 'password': 'tenfold'},
                      verify=False)
    if r.status_code != 200:
        raise Exception('Invalid status code', r.status_code)
    response_dict = ast.literal_eval(r.text)
    token = response_dict.get('token')
    if not token:
        raise Exception('Unable to generate token, please check username or password', r.text)
    return token

def get_record_test():
    token= get_token_test()
    r = requests.post('{}/record'.format(BASE_URI),
                      data={'module': 'Account', 'name': 'Patrick', 'token': token},
                      verify = False)
    if r.status_code == 403:
        raise Exception('Invalid token', r)
    if r.status_code != 200:
        raise Exception('Invalid status code while getting record', r)
    response_dict = ast.literal_eval(r.text)
    if response_dict.get('id') is None:
        raise Exception('Id not found for given response', r)

def get_allrecords_test():
    token = get_token_test()
    r = requests.get('{}/records'.format(BASE_URI), data={'token': token}, verify = False)
    if r.status_code != 200:
        raise Exception('Invalid status coe while getting record', r)
    response = ast.literal_eval(r.text)
    if not response:
        raise Exception('Received empty list while querying for records', r)
    return r

print get_token_test()
print get_allrecords_test()