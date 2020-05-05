# Chapter 16 - OS Module

# os.name:
"""
The os module has both callable functions and normal values. In the case of
os.name, it  is just a value. When we accesss os.name we will get information
about what platform we are rugging on.
"""
import os
print(os.name)

# os.environ, os.getenv() and os.putenv()
"""
The os.environ value is known as a mapping object that returns a dictionary
of the user's environmental variable.
Every time we use our computer some environment variable are set.
These can give us valuable information, such as number of processor,
type of CPU, the computer name, etc.
"""
import os
print(os.environ)

# We can access the environmental variable using our normal dictionary methods.

print("\n")
print(os.environ["TMP"])
print(os.environ["USERNAME"])

# We could also use the os.getenv function to access this environmental variable

print(os.getenv("TMP"))

"""
The benefit of using os.getenv() insted of the os.environ dictionary is that if we happen to try to access an environmental variable that doesn't exists, the
getenv function will just return None. If we did the same thing with os.environ,
we would receive on error.
"""

# os.chdir() and os.getcwd()
"""
The os.chdir function allows us to change the dictionary that we're currently
running our Python session in. If we want to actually know what path we are
currently in, then we would call os.getcwd().
"""
print("\n")
print("Our current working Directory is: ", os.getcwd())

# Change the current working directory:
os.chdir(r"D:\Class\Python\RealPython")
print("\n")
print("Now we have change the current working directory to: ", os.getcwd())
os.chdir(r"D:\Class\Python") # Return to the working directory

# os.mkdir() and os.makedirs()
"""
The first one is os.mkdir(), which allows us to create a single folder/directory .
"""
#os.mkdir("test")
#path = r"D:\Class\Python\test\pytest"
#os.mkdir(path)

"""
The first line of code will create a folder named test in the current directory.
or assign a path to a variable and then we pass the path to so.mkdir(). This
allows us to create a folder anywhere on our system we have permission to.
"""
# The os.makedirs() function will create all the intermediate folder in a path if they don't already exists.

path = r"D:\Class\Python\test\2014\02\19"
#os.makedirs(path)


# os.remove() and os.rmdir()
"""
The os.remove() and os.rmdir() functions are used for deleting files and directories respectively.
"""
# os.remove("test.text")
"""
This code snippet will attempt to remove a file named test.text from our current
working directory. If it cannot find the file, we will likely receive some sort
of error. We will also receive an error if the file is in use(i.e. locked) or
we do not have permission to delete the file.
"""
# Note: Check os.unlink()

# os.rmdir("pytest")

"""
The code above will attempt to remove a directory named pytest from our current
working directory. An error will be raise if the diectory does not exist, we do
not have the permission to remove it or if the directory is not empty.
"""
# Note: Check os.removedirs() Which can remove nested empty directories recursively.

# os.rename(src, dst)
"""
The os.rename() function will rename a file or a folder.
"""
# os.rename("test.text", "pytest.txt")
# There is also an os.renames() function that recursively renames a directory or file .

# os.startfile()
"""
The os.startfile() method allows us to "start" a file with its associated
program. In other words, we can open a file with it's associated program,
just like when we double-click a PDF and it opens in Adobe Reader.
"""

# os.startfile(r"D:\Class\Python\test.txt")

# os.walk():
"""
The os walk() method gives us a way to iterate over a root level path.
What this means is that we can pass a  path to this function and get access
to all its sub-directories and files.
"""
"""
path = r"D:\Class\Python"
for root, dirs, files in os.walk(path):
    print(root)


# If we want we can loop over dirs and fies too.

for root, dirs, fiels in os.walk(path):
    print(root)
    for _dir in dirs:
        print(_dir)
    for _file in fiels:
        print(_file)

"""

# os.path:
"""
the os.path sub-module of the os modules has lots of great functionality built in.

. basename
. dirname
. exists
. isdir and isfile
. join
. split

"""

# os.path.basename:
"""
The basename function will return just the filename of a path
"""
print(os.path.basename(r"Chapter_16_OS_MODULE.py"))

# os.path.dirname
"""
The dirname function will return just the directory portion of the path.
"""
path = r"D:\Class\Python\Chapter_16_OS_MODULE.py"
print(os.path.dirname(path))


# os.path.exists:
"""
The exists function will tell us if a path exists or not. All we have to do is
pass it a path.
"""
path = r"D:\Class\Python\test.txt"
print("We are checking the file path is exists or not ! :",os.path.exists(path))

path = r"D:\Class\Python\tet.txt"
print("We are checking the file path is exists or not ! :",os.path.exists(path))

# os.path.isdir / os.path.isfile
"""
 The isdir and isfile method are closely related to the exists method in that
 they also test for existance. However isdir only checks is the path is a
 directory and isfile only checks if the path is a file.
 If we want to check if a path exists regardless of wheather it is a file or
 directory , then we'll want to use the exists method.
"""

path  = r"D:\Class\Python\Chapter_16_OS_MODULE.py"
print(os.path.isdir(path))
print(os.path.isfile(path))

path  = r"D:\Class\Python"
print(os.path.isdir(path))
print(os.path.isfile(path))

# os.path.join:
"""
The join method gives us the ability to join one or more path components
together using the appropriate separator.
For ex: On Windows the path separator is the backslash, but in linux, the
separator is the forward slash.
"""
print(os.path.join(r"D:\Class\Python", "Chapter_16_OS_MODULE.py"))

# Note: The join method does not check of the result actually exists.

# os.path.split:
"""
The split method will split a path into a tuple that contains the diectory and
the file.
"""

path = r"D:\Class\Python\Chapter_16_OS_MODULE.py"

print(os.path.split(path))

# If path does not have a file name :
path = r"D:\Class\Python"

print(os.path.split(path))


dirname, fname = os.path.split(r"D:\Class\Python\Chapter_16_OS_MODULE.py")
print("Directory: %s" %(dirname))
print(f"filename:{fname}")
