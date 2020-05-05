# Chapter 11 - Classes
"""
Everything in Python is an object.
What that means is that every thing in Python has methods and values.
This reason is that everything is based on a class.
A Class is the blueprint of an object.
"""
#Example:

x = "Mike"
print(dir(x))

"""
If we use Python's "dir" keyword, we can get a list of all the methods we can
call on our string.
There are 71 methods here ! Technically we are not suppose to call the methods that
start with underscores directly, so that resuces the total to 38.
It means that a string is based on a class and x is an instance of that class!
"""
# Creating a Class:

# Python 2.x syntax
class Vehicle(object):
    """ docstring"""

    def __init__(self):
        """Constructor"""
        pass

"""
To Create a class we need to use Python's "class" keyword, followed by the name of the class.
In Python, onvention says that the class name should have the first letter capitalized. Next we have an open
parentheses followed by the word object and a close parentheses. The object is what the class is based on onject.
Class have a special method called __init__ (for initialization). This method is called whenever we create (or instantiate)
an object based on this class. The __init__ method in only called once nad is not to be called again inside the program.
Another term for __init__ is constructor.
A Function changes its name to "method" when it is within a class. Also that every method has to have at least
one argument (i.e. self).

In Python 3.x we do not need to explicitly say we're inheriting from object. Insted we could have written the above like this:
"""
# Python 3.x syntax
class Vehicel:
    """docstring"""

    def __init__(self):
        """constructor"""
        pass


# Class with some attributes and methods :

class Vehicle(object):
    """docstring"""

    def __init__(self, color, doors, tires):
        """constructor"""
        self.color = color
        self.doors = doors
        self.tires = tires

    def brake(self):
        """
        Stop that Char
        """
        return "Breaking"
    def driver(self):
        """
        Drive the Car
        """
        return "I'm driving"

"""
The code above added three attributes and two methods.
the three attributes are:
self.color = color
self.doors = doors
self.tires = tires
"""

# What is self:
# Python classes need a way to refer to themselves.
# The word "self"  is a way to describe itself.

# Example:
class Vehicle(object):
    """docString"""

    def __init__(self, color, doors, tires):
        self.color = color
        self.doors = doors
        self.tires = tires

    def brake(self):
         """
         Breaking the Car
         """
         return "Break"

    def drive(self):
        """
        Driving the Car
        """
        return "Driving"
    if __name__ =="__main__":
        car  = Vehicle("blue", 5, 4)
        print(car.color)

        truck = Vehicle("red", 3, 6)
        print(truck.color)




class Vehicle(object):
    """Constructor"""

    def __init__(self, color, doors, tires, vtype):
        self.color = color
        self.doors = doors
        self.tires = tires
        self.vtype = vtype

    def brake(self):
        """
        Stop the Car
        """
        return "%s breaking" %self.vtype

    def drive(self):
        """
        Driving the Car
        """
        return "I'm driving a %s %s!" %(self.color, self.vtype)

if __name__ =="__main__":
    car = Vehicle("blue", 5, 4, "car")
    print(car.brake())
    print(car.drive())

    truck = Vehicle("red", 3, 6, "truck")
    print(truck.drive())
    print(truck.brake())

# Subclass:

class Car(Vehicle):
    """
    The Car class
    """
    def brake(self):
        """
        Override break method
        """
        return "The car class is breaking slowly!"

if __name__ == "__main__":
    car = Car("yellow", 2, 4, "car")
    print(car.brake())
    print(car.drive())
