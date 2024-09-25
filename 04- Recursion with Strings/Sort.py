def issort(arr , size):
    if size == 0:
        return
    if size == 1:
        return arr[0]
    for i in range(size-1):
        if arr[i] > arr[i+1]:
            arr[i] , arr[i+1]  = arr[i+1] , arr[i]
    issort(arr , size - 1)



arr = [5 ,  1 , 2, 4 ,8]
size = len(arr)
issort(arr , size)
# for i in range(len(arr)):
#     print(arr[i])

print(arr)