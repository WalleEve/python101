# CHAPTER 5 - LOOPS:
# The Python world has two types of loops:
# 1: the for loop
# 2: the while loop

"""
Loops are used when we want to do something many times. Usually we will find that we need to do some operations or a set of
operations on a piece of data over and over. This is where loops come in.
"""
# The for loop
# range function:
# The range function will create a list that is n in length.
# In Python 2.x the function name is xrange but in 3.x it is called range
# Example:
print(range(5))
# Output : range(0, 5)
"""
As we can see the range function above took an integer and returned a range object.
The range function also accepet a beginning value, an end value and a step value.
"""

# Example:
print(range(5, 10))
print( list(range(1, 10, 2)))

for number in range(5):
    print(number)
for number in [0, 1, 2, 3, 4]:
    print(number)

a_dict = {"one": 1, "two": 2, "three": 3}
for key in a_dict:
    print(key)

for key in a_dict.keys():
    print(key)

a_dict = {1: "One", 2: "Two", 3: "Three"}
keys = a_dict.keys()
keys = sorted(keys)
for key in keys:
    print(key)

for number in range(10):
    if number % 2 ==0:
        print(number)

# The while Loop:

i = 0
while i < 10:
    print(i)
    i = i + 1

# Break
i = 0
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1

# The break builtine also known as flow control tool.

# Continue:
# Continue used to basically skip an iteration or continue with the next iteration.
i = 0

while i < 10:
    if i == 3:
        i  += 1
        continue
    print(i)
    if i == 5:
        break
    i += 1


# else in loop
# The else statement in loops only executes if the loop completes successfully.
# The primary use of the else statement is for searching for items.

my_list = [1, 2, 3, 4, 5]

for i in my_list:
    if i == 3:
        print("Item found")
        break
    print(i)
else:
    print("item not found!")

# In this code, we break out of the loop when i equals 3. This causes the else statement to be skipped

for i in my_list:
    if i == 6:
        print("Item found")
        break
    print(i)
else:
    print("item not found!")
