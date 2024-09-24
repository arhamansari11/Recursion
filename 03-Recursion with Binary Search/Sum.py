def add ( arr , length ):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    
    remaining = add(arr[1:] , length - 1)
    getsum = arr[0] + remaining
    return getsum




arr = [1,2,3]
size = len(arr)
ans = add(arr , size)
print(ans)



# add([1, 2, 3])  --> (calls add([2, 3]))
#     |
#     +-- add([2, 3])  --> (calls add([3]))
#         |
#         +-- add([3])  --> returns 3
#     |
#     +-- remaining = 3
#     +-- getsum = 2 + 3 = 5  --> returns 5
# |
# +-- remaining = 5
# +-- getsum = 1 + 5 = 6  --> returns 6


