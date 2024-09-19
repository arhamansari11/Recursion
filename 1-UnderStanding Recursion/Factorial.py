# When a function calls itself directly or indirectly is called recursion.

# def dfs(n):

#     dfs(n)


def factorial(n):
    if n == 0:
        return 1
    
    smallProb = factorial(n-1)  
    bigProb = n * smallProb

    return bigProb

    # return n * factorial(n-1)

a = 3

print(factorial(a))

