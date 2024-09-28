def say_digits(n , arr):

# Base Case
    if n == 0:
        return
    
#  Recursive Relation
    digit = n % 10
    n = n // 10

    say_digits(n , arr)

# PreProcessing
    print(arr[digit])
    

n = 410
arr = ["zero" , "one" , "two" , "three" , "four" , "five" , "six" , "seven" , "eight" , "nine"]
say_digits(n , arr)