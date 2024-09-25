# Recursion with Merge Sort Array 
# Merge sort is the best and fast sorting method.

def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        mergesort(left)
        mergesort(right)
        i = j = k = 0
        while i <len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1




arr = [12 , 5 , 4 ,2 ,90 , 10]
mergesort(arr)
print(arr)