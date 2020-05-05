# Chapter 6 - Python Comprehensions:
"""
The Python language has a couple of methods for creating lists and dictionaries that are known as Comprehensions.
There is a third type of Comprehensions for creating a Python set.
"""
#List Comprehensions:
"""
List Comprehensions in Python are very handy. They can also be a little hard to understand .
A list Comprehensions is basically a one line for loop that produces a Python list data structure.
"""
x = [i for i in range(5)]
print(x)

x = ['1', '2', '3', '4', '5']
y = [int(i) for i in x]
print(y)

myStringList = ['a', 'b', 'C']
myString = [s.strip() for s in myStringList]

vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
vecList = [num for elem in vec for num in elem]
print(vecList)


# Dictionary Comprehensions:
print( {i: str(i) for i in range(5)} )

my_dict = {1:"dog", 2:"cat", 3:"hamster"}
print({value:key for key, value in my_dict.items()})

# Set Comprehensions

my_list = [1, 2, 2, 3, 4, 5, 5, 7, 8]
my_set = set(my_list)
print(my_set)


my_list = [1, 2, 2, 3, 4, 5, 5, 7, 8]
my_set = {x for x in my_list}
print(my_set)
