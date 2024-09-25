def power(n, p):

    # Base Case: if the power is 0, return 1 (since anything raised to the power of 0 is 1)
    if p == 0:
        return 1

    # Recursive Case: multiply n by the result of power(n, p-1)
    return n * power(n, p - 1)

ans = power(3, 2)
print(ans)
