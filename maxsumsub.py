# Dynamic Programming bsed Python implementation of Maximum Sum Increasing
# Subsequence (MSIS) problem

# maxSumIS() returns the maximum sum of increasing subsequence in arr[] of
# size n
def maxSumIS(arr, n):
    max = 0
    msis = arr
    for i in range(1, n):
        maxsub = arr[i]
        for j in range(i):
            if arr[j] < arr[i]:
                maxsub += arr[j]
        msis[j] = maxsub
    return max


# Driver program to test above function
arr = [1, 101, 2, 3, 100, 4, 5]
n = len(arr)
print("Sum of maximum sum increasing subsequence is " +
      str(maxSumIS(arr, n)))
