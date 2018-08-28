arr = [-8, -3, -2, -5, -7, -4, -6]
from sys import maxint
def kadanes(arr):
    maxsofar = -10000
    maxendinghere = 0
    for i in arr:
        maxendinghere = maxendinghere + i
        #print maxendinghere, maxsofar
        if maxendinghere > maxsofar:
            #print maxsofar, maxendinghere
            maxsofar = maxendinghere
        if maxendinghere < 0:
            maxendinghere = 0
    return maxsofar


def maxSubArraySum(a, size):
    max_so_far = -maxint - 1
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        print max_ending_here, max_so_far
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far

print maxSubArraySum(arr, len(arr))
print kadanes(arr)