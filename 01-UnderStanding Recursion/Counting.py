def counting(n):

    print(n)

    if n == 0:
        return 0
    
    ans = n + counting(n-1)
    
    print(ans)
    return ans




n = 7
print(counting(n))