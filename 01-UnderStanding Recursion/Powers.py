def power(n):
    
    if n == 0:
        return 1
    
    small_prob = power(n-1)
    big_prob = 2 * small_prob
    return big_prob
    


n = 5
print(power(n))