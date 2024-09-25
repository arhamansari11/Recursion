def Palindrome(arr , l , r):

    if l >= r:
        return True
    
    if arr[l] != arr[r]:
        return False
    
    return Palindrome(arr , l + 1 , r - 1)


arr = "abc"
l = 0
r = len(arr) - 1
ans = Palindrome(arr , l , r)
print(ans)
if ans:
    print("Done")
else:
    print("Not Done")

