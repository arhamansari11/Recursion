def Digits(n , arr):

    # Base Case

    if n == 0:
        return
    
    # PreProcessing

    digit = n % 10
    n = n // 10

    # Recursive Relation
    
    Digits(n , arr)
    print(arr[digit])




n = 410
arr = ["zero" , "one" , "two" , "three" , "four" , "five"  , "six" , "seven" , "eight" , "nine"]
Digits(n , arr)