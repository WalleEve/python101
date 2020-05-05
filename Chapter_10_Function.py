# Chapter 10 - FUnctions:
"""
A Function is a structure that we define. We get to decide if they have arguments or not.
We can add keyword arguments and default arguments too. A function is a block of code that
starts with the "def" keyword, a name for the function and a colon .

"""

def a_function():
    print("We have just created a function!")

# An Empty Function (the stub)
def empty_function():
    pass

# Passing Arguments to a function:
def add_(a, b):
    return a + b

result = add_(2, 4)
print(result)


# Keyword Arguments
def keyword_function(a=1, b=4):
    return a+b
print(keyword_function(a=4, b=45))
print(keyword_function())

def mixed_function(a, b= 2, c=3):
    return a+b+c

print(mixed_function(a=4, b=23, c=4))
print(mixed_function(5))


# *args and **kwargs:
"""
We can also set up functions to accepet any number of arguments or keywords arguments by using a
special syntax. To get infinite arguments, use *args and for infinite keyword arguments, use **kwargs.
The args and kwargs words are not important.

"""
def many(*args, **kwargs):
    print(args)
    print(kwargs)

print(many(1, 2, 3, 4, name="Mike", job="Programmer"))


# A Note on Scope and Global:
""""
Python has the concept of scope just like most programming languages. Scope tell us when a variable is
available to use and where. If we define a variable inside a function, thoes variables can be used inside
that function. Once the function ends, they can no longer be used because they are out of scope.
"""

def function_a():
    global a
    a = 1
    b = 3
    return a + b

def function_b():
    c = 3
    return a+c


print(function_a())
print(function_b())
