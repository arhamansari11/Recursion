arr = [1, 2, 3, 4, 5]

l = 0
r = len(arr) - 1
key = 2

found = False  

while l <= r: 
    mid = (l + r) // 2
    if arr[mid] == key:
        found = True
        break  
    elif arr[mid] > key:
        r = mid - 1  
    else:
        l = mid + 1 

print(found)
