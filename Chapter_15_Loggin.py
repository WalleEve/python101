# Chapter 15 - Logging
"""
Python provides a very powerfull logging library in its standard library.
Instead of print statements for debugging we can also use logging to do this.
"""

# Creating a Simple Logger

import logging

# add filemode="w" to overwrite
logging.basicConfig(filename="sample3.log", filemode="w", level=logging.INFO)

logging.debug("this is a debug message")
logging.info("Informational message")
logging.error("An error has happened!")

"""
To access the logging module we have to first import it.
The easiest way to create a log to use the logging module's
basicConfig funtion and pass it some keyword arguments.
It accespts the following: filename, filemode, format, datefmt, level, and stream.
there are five levels of logging
DEBUG
INFO
WARNING
ERROR
CRITICAL

If we run this code multiple times, it will append to the log if it already exists.
If we would rather have our logger overwrite the log, then pass in  a filemode="W".

"""

# Note:
"""
That the debugging isn't the output. That is because we set the level at INFO.
So our logger will only log if it's a INFO, WARNING, ERROR or CRITICAL message.
The root part just means that this logging message is comming from the root logger or main logger.

The logging module can also log some exceptions to file or wherever we have it configured to log to.

"""

import logging

logging.basicConfig(filename="sample3.log", level=logging.INFO)

try:
	raise RuntimeError
except RuntimeError:
	# log.exception("Error!")
	pass


# How to log from Multiple Modules ( and formatting too!)

import logging
import otherMod

def main():
	"""
	The main entry point of the application
	"""

	logging.basicConfig(filename="sample3.log", level=logging.INFO)
	logging.info("Program Started")
	result = otherMod.add(7, 8)
	logging.info("Done!")

if __name__ == "__main__":
	main()





import logging
import otherMod2


def main():
	"""
	The main entry point of the application
	"""

	logger = logging.getLogger("exampleApp")
	logger.setLevel(logging.INFO)

	# create the logging file handler
	fh = logging.FileHandler("new_snake.log")

	formatter = logging.Formatter(" %(asctime)s - %(name)s - %(levelname)s -%(message)s ")
	fh.setFormatter(formatter)

	# add handler to logger object
	logger.addHandler(fh)

	logger.info("Program started")
	result = otherMod2.add(10,25)
	logger.info("Done!")


if __name__ == "__main__":
	main()



 # Configuring Logs for Work.
"""
 The logging modules can be configured 3 different ways. We can configure it using methods (loggers, formatters, handlers) ,
 we can use a configure file and pass it to fileConfig(); or we can create a dictionary of configuration information and pass it to  the dictConfig() function.
"""


"""


[loggers]
keys = root, exampleApp

[handlers]
keys = FileHandler, consoleHandler

[formatters]
keys = myFormatter

[logger_root]
keys = CRITICAL
handlers = consoleHandler

[logger_axampleApp]
level = INFO
handlers = fileHandler
qualname = exampleApp

[handler_consoleHandler]
class = StreamHandler
level = DEBUG
formatter = myFormatter
args = (sys, stdout)

[handler_fileHandler]
class = FileHandler
formatter = myFormatter
args = ("config.log",)

[formatter_myFormatter]
format = %(asctime)s - %(name)s - %(levelname)s - %(message)s
datefmt=

"""

#Note
"""
We will notice that we have two loggers specified: toot and exampleApp.
For whatever reason, "root" is required. If we don't inclide it, Python will
raise a ValueError from config.py's _install_loggers function, which is a part
of the logging module.
If we set the root's handler to fileHandler, then we'll and up doubling the log output,
so to keep that from happening, we send it to the console instead.

"""
#
#
# import logging
# import logging.config
# import otherMod2
#
# def main():
# 	"""
# 	Based on http://docs.python.org/howto/logging.html#configuring-logging
# 	"""
#
# 	logging.config.fileConfig('logging.conf')
# 	logger = logging.getLogger("exampleApp")
#
# 	logger.info("Program started")
# 	result = otherMod2.add(7, 9)
# 	logger.info("Done!")
#
#
# if __name__ == "__main__":
# 	main()
