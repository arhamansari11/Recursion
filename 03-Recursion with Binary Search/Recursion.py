def binarysearch(arr , l , r , key):
    
    if l > r:
        return False
    
    mid = (l + r) // 2

    if arr[mid] == key:
        return True

    if arr[mid] < key:
        return binarysearch(arr , mid + 1, r , key)
    
    else:
        return binarysearch(arr , l , mid -1 , key)




arr = [ 1 , 2 , 3 ,4 ,5]
left = 0
right = len(arr) - 1
key = 6
print(binarysearch(arr , left , right , key))