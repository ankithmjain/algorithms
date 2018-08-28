def lbs(arr):
    n = len(arr)

    # allocate memory for LIS[] and initialize LIS values as 1
    # for all indexes
    lis = [1 for i in range(n + 1)]
    for i in range(n):
        initial = i
        sum = arr[initial]
        for j in range(i + 1, n):
            
            if arr[j] > arr[initial]:
                sum =+ arr[j]


# Driver program to test the above function
arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13,
       3, 11, 7, 15]
print "Length of LBS is", lbs(arr)