'''
toys.py

Simple toy functions to get comfortable working 
with functions.
'''


# I wrote a function that adds 1 to the input and prints the result
def inc(a):
    print(a + 1)


# I wrote a function that adds 1 to the input and returns the result
def inc_return(a):
    return a + 1


# I wrote a function that adds the two input numbers together and returns the sum
def sum(a, b):
    return a + b


# I wrote a function that takes two numbers, adds them together using sum() and then increments the sum using inc_return.
def sum_inc(a, b):
    return sum(a, b) + 1


# write a function that returns a 
# boolean (True or False) for whether 
# the input number is even
def is_even(a):
    return (a % 2) == 0


# create for loop that takes a string
# and an integer and returns a new string 
# that is the string repeated equal to 
# integer
# e.g. string_repeat('ho', 3) returns
# 'hohoho'
def string_repeat(a, b):
    return a * b
    # hint: you can add strings together 
    # in order to concatenate them

