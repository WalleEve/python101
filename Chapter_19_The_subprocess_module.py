# Chapter 19 - The Subprocess Module
"""
The subprocess module gives the developer the ability to start process or
program from mpython. We can start applications and pass arguments to them
using the subprocess module.
The subprocess module added to replace the os module set of os.popen, os.spawn
and os.system calls well as replace popen2 and the old commands module.
"""

# The call function
"""
The subprocess module provides a function named call. This function allows us to call another program,
wait for the command to complete and then return the return code. It accepts one or more arguments as
well as the  following keywords arguments(with their defaults):
stdin = None
stdout = None
stderr = None
shell = False
"""

# Example 1:
# import subprocess
# subprocess.call("notepad.exe")

"""
If we run this code on a windows machine, we should see Notepad open up.
We will notice that IDLE waits for us to close Notepad and then it returns a code zero(0).
This means that it completed successfully. If we receive anything except for a zero, then it usually means
we have had some kind of error.

Normally when we call this function we would want to assign the resulting return code to a variable
so we can check to see if it was the result we expect.
"""
import subprocess

# code = subprocess.call("notepad.exe")
# if code == 0:
#     print("success!")
# else:
#     print("Error")


#  call method also acceps arguments to be passed to the program that we're executing.

# code = subprocess.call(["ping","www.google.com"])

# The Popen Class :
"""
The Popen class executes a child program in a new process. Unlikely call method it does not wait for the called
process to end unless we tell it to using by using the wait method.
"""

# program = "notepad.exe"
# subprocess.Popen(program)
# print("Subprocess ends!")

# Let's make Popen wait for the program to finish:

program = "notepad.exe"
process = subprocess.Popen(program)
code = process.wait()
print(code)
