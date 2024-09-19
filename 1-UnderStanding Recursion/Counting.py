def counting(n):

    # Base Case

    if n == 0:
        return 0
    
    # PreProcessing

    print(n)

    # Other Base Case

    # if n == 1:
    #     return 1 

    #  Recursive Relation

    return n + counting(n-1)


print(counting(7))