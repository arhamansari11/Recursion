def power(n):

    # Base Case

    if n == 0:
        return 1
    
    # Recursive Solution

    return 2 * power(n-1)
    

print(power(8))