arr = [1, 2, 3, 4, 9, 10, 40 ]
x = 10


def linear_search(arr, x):
    for i in range(len(arr)):

        if arr[i] == x:
            return i

    return -1


print("By linear search", linear_search(arr, x))


def binary_search(arr, x):
    lower = 0
    upper = len(arr) -1
    while True:
        mid = int((lower + upper)/2)
        if x > arr[mid]:
            lower = mid
        elif x< arr[mid]:
            upper = mid
        else:
            return mid


print("By binary search", binary_search(arr, x))

