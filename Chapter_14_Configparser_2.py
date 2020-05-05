# Python ConfigParser:
"""
ConfigParser is a Python class which implments a basic configuration language
for Python Programs. It provides a structure similar to
Microsoft Windows INI files.
ConfigParser allows to write Python programs whcih can be costomized by end users easily.

The configuration file consists of sections followed by key/value pairs of option.
The section names are delimited with [] characters.
The pairs are separated either with : or = .
Commnets start either with # or with ;.

"""


# configuaration data from a file db.ini
# Example db.ini
"""
[mysql]
host = localhost
user = user7
passwd = s$cret
db = ydb

[postgresql]
host = localhost
user = postgres
passwd = postgres
port = 5432
db = test_db

"""
# Python ConfigParser read file :


import configparser

config = configparser.ConfigParser()
config.read('db.ini')

host = config['mysql']['host']
user = config['mysql']['user']
passwd = config['mysql']['passwd']
db = config['mysql']['db']

print('MySQL configuration')
print(f"host: {host}")
print(f"user: {user}")
print(f"passwod: {passwd}")
print(f"db: {db}")



host2 = config['postgresql']['host']
user2 = config['postgresql']['user']
passwd2 = config['postgresql']['passwd']
port2 = config['postgresql']['port']
db2 = config['postgresql']['db']

print('PostgrSQL configuration')
print(f"host: {host2}")
print(f"user: {user2}")
print(f"passwod: {passwd2}")
print(f"port: {port2}")
print(f"db: {db2}")


# Python ConfigParser sections
"""
The configparser data is organized into sections. The sections() function reads all the sections and the has_section() function checks if there is the specified section.
"""

# sections.py


import configparser

config = configparser.ConfigParser()
config.read('db.ini')

sections = config.sections()
print(f"Sections: {sections}")


sections.append('sqlite')

for section in sections:
    if config.has_section(section):
        print(f"Config file has section {section}")
    else:
        print(f"Config file does not have section {section}")



# Python ConfigParser read from string
"""
We can read configuration data from a string with the read_string() method
"""

# read_from_string

import configparser

cfg_data = """
[mysql]
host = localhost
user = user7
passwd = s$cret
db = ydb
"""
config = configparser.ConfigParser()
config.read_string(cfg_data)

host = config['mysql']['host']
user = config['mysql']['user']
passwd = config['mysql']['passwd']
db = config['mysql']['db']

print(f"Host: {host}")
print(f"User: {user}")
print(f"Password: {passwd}")
print(f"Database: {db}")



# Python ConfigParser read from dictionary
"""
We can read configuration data from a dictionary with the read_dict() method

"""


import configparser


cfg_data = {
'mysql':{'host': 'localhost', 'user':'user7', 'passwd':'s$cret', 'db':'testDb'}
}


config = configparser.ConfigParser()
config.read_dict(cfg_data)

host = config['mysql']['host']
user = config['mysql']['user']
passwd = config['mysql']['passwd']
db = config['mysql']['db']

print(f"Host: {host}")
print(f"User: {user}")
print(f"Password: {passwd}")
print(f"Database: {db}")


"""
The example reads configuration from a Python dictionary:
cfg_data = {
'mysql':{'host': 'localhost',
'user':'user7',
 'passwd':'s$cret',
  'db':'testDb'}
}


Keys are section names, Values are dictionaries with keys and values that are presnet in the section.
"""



# Python ConfigParser write

"""
The write() method writes configuration data.

"""
# writing
import configparser


config = configparser.ConfigParser()

config.add_section('mysql') # we add a ection with add_section()

# Set the options
config['mysql']['host'] = 'localhost'
config['mysql']['user'] = 'user7'
config['mysql']['passwd'] = 's$cret'
config['mysql']['db'] = 'TestDB'

# Write the data with write()
with open ('db3.ini', 'w') as configfile:
    config.write(configfile)

# ConfigParser interpolation
"""
CofigParser allows to use interpolation in configuration file
It uses the %() syntax.

"""
# cfg.ini
"""
[info]
user_dir = D:\Class
name = Python
home_dir = %(user_dir)s\%(name)s

# We build the home_dir with interpolation. Note that the 's' is part if the syntax.
"""

# interpolation.py

import configparser

config =configparser.ConfigParser()
config.read('cgf.ini')

users_dir = config['info']['user_dir']
name = config['info']['name']
home_dir = config['info']['home_dir']

print(f'Users Directory: {users_dir}')
print(f'name: {name}')
print(f'Home directory: {home_dir}')
