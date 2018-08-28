def argstut(*args, **kwargs):
    for i in args:
        print i
    for key in kwargs:
        print key, kwargs[key]


argstut(1, 2, 4)
argstut(3, {'a':2, 'b':1})