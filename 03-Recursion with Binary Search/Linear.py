def linear(arr , size , key):
    if size == 0:
        return True
    if size == 1:
        return arr[0] == key
    
    if arr[0] == key:
        return True
    else:
        ans = linear(arr[1:] , size - 1 , key)
        return ans



arr = [ 4 ,5 ,7]
key = 9
size = len(arr)
ans = linear(arr , size , key)
print(ans) 