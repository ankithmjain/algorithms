arr = '11111'
lenarr = len(arr)
global total
total = 0
def calculate_substr(arr, n):
    """"""
    global total
    #print total
    #print n
    for i in range(len(arr)-n+1):
        print arr[i:n+i]
        crr = int(''.join(arr[i:n+i]))
        total += crr
for i in range(1, lenarr):
    calculate_substr(arr,i)
#calculate_substr(arr, 2)
print total