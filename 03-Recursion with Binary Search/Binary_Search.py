def issorted(arr, length):
    # Base Case
    if length <= 1:  # If the length is 1 or 0, it's sorted
        return True
    
    # If the first element is greater than the second, it's not sorted
    if arr[0] > arr[1]:
        return False
    
    # Recur for the rest of the array
    return issorted(arr[1:], length - 1)

arr = [2, 4, 10, 8, 9]
size = len(arr)
ans = issorted(arr, size)
if ans:
    print("Array is Sorted")
else:
    print("Array is not Sorted")
