def maxLen(arr):
    # NOTE: Dictonary in python in implemented as Hash Maps
    # Create an empty hash map (dictonary)
    hash_map = {}

    # Initialize result
    max_len = 0

    # Initialize sum of elements
    curr_sum = 0

    # Traverse through the given array
    for i in range(len(arr)):

        # Add the current element to the sum
        curr_sum += arr[i]

        if arr[i] is 0 and max_len is 0:
            max_len = 1

        if curr_sum is 0:
            max_len = i + 1
        print i, curr_sum, max_len
        # NOTE: 'in' operation in dictonary to search key takes O(1)
        # Look if current sum is seen before
        if curr_sum in hash_map:
            max_len = max(max_len, i - hash_map[curr_sum])
        else:
            # else put this sum in dictonary
            hash_map[curr_sum] = i
        print hash_map
    return max_len
arr = [15, -2, 2, -8, 1, 7, 10, 13]
print "Length of the longest 0 sum subarray is %d" % maxLen(arr)