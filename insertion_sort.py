arr = [64, 34, 25, 12, 22, 11, 90]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i -1
        while j>= 0 and key < arr[j]:
            print(j, key, arr[j], arr)
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        print(arr)

insertion_sort(arr)

print ("Sorted array by insertion sort is:")
for i in range(len(arr)):
    print ("%d" %arr[i])