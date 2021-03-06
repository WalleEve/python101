# Chapter 14 - Configparser:
"""
Configuration files are used by both user and programmers.
They are usually used for storing our application's setting or even our operating system's settings.
Python's core library includes a module called configparser that we can use for creating and
interacting with configuration files.
"""

# Creating a Config File

import configparser

def createConfig(path):
    """
    Create a config file
    """
    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "font", "Courier")
    config.set("Settings", "font_size", "10")
    config.set("Settings", "font_tryle", "Normal")
    config.set("Settings", "font_info", "We are using %(font)s at %(font_size)s pt")

    with open(path, "w") as config_file:
        config.write(config_file)


if __name__ == "__main__":
    path = "settings.ini"
    createConfig(path)


# How to Read, Update and Delete Options:

import configparser
import os

def crudConfig(path):
    """
    Create, read, update, delete config
    """

    if not os.path.exists(path):
        createConfig(path)

    config = configparser.ConfigParser()
    config.read(path)

    # read some values from the config
    font = config.get("Settings", "font")
    font_size = config.get("Settings", "font_size")

    # change a value in the config
    config.set("Settings", "font_size", "12")

    # delete a value from the config
    config.remove_option("Settings", "font_style")

    # Write changes back to the config file
    with open(path, "w") as config_file:
        config.write(config_file)


if __name__ == "__main__":
    path = "settings.int"
    crudConfig(path)

"""
When we want to change an option's value, then we use the "set" method,
where  we pass the section name, the option name the value.
Finally, we cann use the remove_option method to remove an option.

"""


import configparser
import os

def create_config(path):
    """
    Create a donfig file
    """

    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "font", "Courier" )
    config.set("Settings", "font_size", "20")
    config.set("Settings", "font_style", "Normal")
    config.set("Settings", "font_info", "We are using %(font)s at %(font_size)s pt")

    with open(path, "w") as config_file:
        config.write(config_file)

def get_config(path):
    """
    Returns the config object
    """
    if not os.path.exists(path):
        create_config(path)

    config = configparser.ConfigParser()
    config.read(path)
    return config


def get_setting(path, section, setting):
    """
    Printing out setting
    """
    config = get_config(path)
    value = config.get(section, setting)
    msg = "{section}  {setting} is {value}".format(section=section, setting=setting, value=value)
    print(msg)
    return value


def update_setting(path, section, setting, value):
    """
    Update a setting
    """
    config = get_config(path)
    config.set(section, setting, value)
    with open (path, "w") as config_file:
        config.write(config_file)


def delete_setting(path, section, setting):
    """
    Delete a setting
    """
    config = get_config(path)
    config.remove_option(section, setting)
    with open(path, "w") as config_file:
        config.write(config_file)


if __name__ == "__main__":
    path = "setting.ini"
    font = get_setting(path, "Settings", "font")
    font_size = get_setting(path, "Settings", "font_size")

    update_setting(path, "Settings", "font_size", "12")

    delete_setting(path, "Settings", "font_style")


# How to Use Interpolation
"""
The configparser module also allows interpolation, which means we use some options to build
another option. We actually do this with the font_info option in that its value is based on the
font and font_size option. We can change an interpolated value using a Python dictionary.
"""

import configparser
import os

def interpolationDemo(path):
    if not os.path.exists(path):
        createConfig(path)

    config = configparser.ConfigParser()
    config.read(path)

    print(config.get("Settings", "font_info"))

    print(config.get("Settings", "font_info", vars={"font":"Arial", "font_size":"100"}))


if __name__ =="__main__":
    path = "Settings.ini"
    interpolationDemo(path)
