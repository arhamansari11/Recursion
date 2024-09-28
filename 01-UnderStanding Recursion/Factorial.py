def factorial(n):

    # Base Case

    if n == 0:
        return 1
    
    # Recursive Relation

    # small_prob = factorial(n-1)
    # big_prob = n * small_prob
    # return big_prob

    # Recursive Relation

    return n * factorial(n-1)


n = 5
print(factorial(n))