# Chapter 8 - Working With Files.

# Read a File:
# Python has a builtin function called "open" that we can use to open a file for reading.

"""
We have create a text file name test.txt

with content:
This is test file
line 2
line 3
this line intentionally left blank

"""
# Open file test.txt to read
handle = open("test.txt")
handle = open(r"D:\Class\Python\test.txt", "r")
data = handle.read()
print(data)
handle.close()


# Difference between specifing a raw string versus a regular string

# regular string
print("C:\\Users\\sayed\\py101book\\data\test.txt")

# raw string
print(r"C:\Users\sayed\py101book\data\test.txxt")



# Read file one line at a time

handle = open(r"D:\Class\Python\test.txt", "r")
data = handle.readline() # read just one line
print(data)
handle.close()



handle = open(r"D:\Class\Python\test.txt", "r")
data = handle.readlines()  # read all the lines
print(data)
handle.close()


handle = open("test.txt", "r")

for line in handle:
    print(line)
handle.close()


handle = open("test.txt", "r")

while True:
    data = handle.read(1024)
    print(data)
    if not data:
        break
# Rad a Binary File:
handle =  open("test.pdf", "rb")
data = handle.read()
#print(data)

"""
So this time we change the file mode to rb, which means read-binary. We will find
that we may need to read binary files when we are downloading PDF from the internet or transfer files from PC to PC.
"""


# Writing Files in Python :
# Flags for writing files: "w" and "wb" for write-mode, write-binary-mode.
# CAUTION: When using "w", "wb" modes, if the file already exists, it will be overwritten with no warning!
# We can check if a file exists before we open it by using Python's os module, see the os.path.exists.

handle = open("test.txt", "w")
handle.write("This is a test!")
handle.close()


# Using the with operator:
# The "with" operator cretes what is known as contex manager in Python.
# That will automatically close the file for us when we are done processing it.

with open("test.txt") as file_handler:
    for line in file_handler:
        print(line)


# Catching Errors:

try:
    file_handler = open("test.txt")
    for line in file_handler:
        print(line)
except IOError:
    print("An IOError occurred!")
finally:
    file_handler.close()


try:
    with open("test.txt") as file_handler:
        for line in file_handler:
            print(line)
except IOError:
    print("An IOErro Occurred!")
 
