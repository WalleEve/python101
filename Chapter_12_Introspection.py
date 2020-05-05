# Chapter 12 - Introspection:
"""
type
dir
help
"""
# The Python Type :
"""
Python can tell us what type of variable we have or what type is returned from a function.
Python has a keyword called "type" that can tell us what is what.
"""
x = "Test"
y = 7
z = None
alist = ["1", "a", "c", 2]
atuple = (1, 2, 3, "a")
adictionary = {1:"a", 2:"b", 3:"c"}
aset = {1, 2, 3, "a"}
print(type(x))
print(type(y))
print(type(z))
print(type(alist))
print(type(atuple))
print(type(adictionary))
print(type(aset))
a = len(alist)
print(type(a))
print(type(len(alist)))

# The Python Dir
"""
The "dir" keyword is used to tell the programmer what attributes and methods there
are in the passed in object.
If we forget to pass in an object, dir will return a list of names in the current scope.

"""

print(dir("test"))
"""
Since everything in Python is an object we can pass a string to dir and find out
what methods it has.
"""

print("\n")
print(dir(adictionary))
print("\n")

import sys
print(dir(sys))


# Python Help!
"""
Python comes with a handy help utility. Just type "help()" into a Python shell
and we'll see the python version details.

Welcome to Python 3.7's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.7/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".
"""
help()

"""
# Note:
New we have a "help>" prompt instead of the ">>>".
When we are in help mode, we can explore the various modules, keywords and topics found in Python
"""
