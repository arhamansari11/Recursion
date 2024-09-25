# Simple Code

# s = ["a" , "b" , "c" , "d" , "e"] 
# length = len(s)
# l = 0
# r = length - 1
# while l < r: 
#     s[l], s[r] = s[r], s[l]  
#     l += 1
#     r -= 1

# print("".join(s))  


#  Through Recursion
def Reverse(arr, l, r):
    print(arr)
    if l >= r:
        return
    else: 
        arr[l], arr[r] = arr[r], arr[l] 
        return Reverse(arr, l + 1, r - 1)

s = ["a", "b", "c", "d", "e"]
l = 0
r = len(s) - 1
Reverse(s, l, r)
print(s) 
