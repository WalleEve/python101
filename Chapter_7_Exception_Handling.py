# Chapter 7 - Exception Handling:
"""
# Common Exceptions:
. Exception: This is what almost all the others are built off of
. AttributeError: Raised when an attribute reference or assignment fails.
. IOError: Raised when an I/O operation (such as print statement, the built in open() function
           or a method of a file object) fails for an I/O- related reasons,
           eg: "file not found", "disk full"
. ImportError: Raised when an import statement fails to find the module definition or when a from...import fails to
               find a name that is to be imported.
. IndexError: Raised when a sequence subscript is out of range,
. KeyError: Raised when a mapping (dictionary) key is not found in the set of existing keys.
. KeybordInterrupt: Raised when the user hits the interrupt key (normally Control-C or Delete)
. NameError: Raised when a local or global name is not found.
. OSError: Raised when a function returns a system-related error.
. SyntaxError: Raised when the parser encounters a syntax error.
. TypeError: Raised when an operation or function is applied to an object of inappropriate type.
             The associated value is a string giving details about the type mismatch.
. ValueError: Raised when a built-in operation or function receives an argument that has the right type
              but an inappropriate value, and the situation is not described by a more precise exception such as IndexError.
. ZeroDivisionError: Raised when the second argument of a division or modulo operation is zero.

"""
# How to handle Exceptions:
# division by zero:

# print( 1 / 0)
"""
Traceback (most recent call last):
  File "D:\Class\Python\Chapter_7_Exception_Handling.py", line 26, in <module>
    print( 1 / 0)
ZeroDivisionError: division by zero
"""

try:
    print (1 / 0)
except ZeroDivisionError:
    print("You can not divide by zeor!")


try:
    print (1 / 0)
except:
    print("You cannot divide by zeor!")

# This is not recommended in Python, this is known as "bare except", which means it will catch any and all exception.

my_dict = {"a":1, "b":2, "c":3}

try:
    value = my_dict["d"]
    print(value)
except KeyError:
    print("That key does not exists!")


my_list = [1, 2, 3, 4, 5]

try:
    print(my_list[6])
except IndexError:
    print("That index is not in the list!")



# Catch multiple exceptions:
my_dict = {"a":1, "b":2, "c":3}

try:
    value = my_dict["d"]
    print(value)
except IndexError:
    print("This index does not exists")
except KeyError:
    print("This key is not present in the dictionry")
except:
    print("Some other error occurred!")


try:
    value = my_dict["d"]
except (KeyError, IndexError):
    print("An IndexError or KeyError occured!")


# The finally Statement;
my_dict = {"a":1, "b":2, "c":3}

try:
    value = my_dict["d"]
except KeyError:
    print("A Key Error occurred!")
finally:
    print("The finally statement has executed!")


# try, except, or else!
"""
The try/except statement also has an else clause. The else will only run if there are no errors raised.
"""

my_dcit = {"a":1, "b":2, "c":3}

try:
    value = my_dict["a"]
    print(value)
except keyError:
    print("A KeyError occurred!")
else:
    print("No Error occurred")


my_dict = {"a":1, "b":2, "c":3}

try:
    value = ["a"]
    print(value)
except KeyError:
    print(" A keyErro Occurred!")
else:
    print("No Error Occurred")
finally:
    print("The finally statement ran!")
