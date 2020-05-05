# Chapter 18 - The sqlite Module
"""
SQLite is a self-contained server-less, config-free transactional SQL Database
Engine.

Note : Use SQLite Manager Plugins for Forefox to inspect our Database visually.

"""
# How to Create a Database and Insert Some Data .

import sqlite3

conn = sqlite3.connect("mydatabse.db") # or use :memory: to  put it in ram

cursor = conn.cursor()

# Create a Table :
cursor.execute(""" CREATE TABLE albums
(title text, artist text, release_date text, publisher text, media_type text)
""")

"""
First we have to import the sqlite3 module and create a connection to the database.
We can pass it a file path, file name or just use the special string ":memory:"
to create the database in memory.
In our case we created it on disk in a file called mydatabase.db.
Next we create a cursor object, which allows us to interact with the database
and add records, among other things. Here we use SQL syntax to create a table
named albums with 5 text fields.
SQLite only supports five data types: null, integer, real, text, and blob.

"""

# Note: If we run the CREATE TABLE command and the Database already exists, we will receive an error message.


# insert some data.
cursor.execute(""" INSERT INTO albums
VALUES ('Glow', 'Andy Hunter', '7/24/2012', 'Xplore Records', 'MP3')""")

 # Save data to databse
conn.commit()

# Insert multiple records using the more secure "?" method

albums = [
 ('Exodus', 'Andy Hunter', '7/9/2002', 'Sparrow Records', 'CD' )
 ('Until We have Faces', 'Red', '2/1/2011', 'Essential Records', 'CD')
 ('The End is Where we Begin', 'Thousand Foor Kutch', '4/17/2012', 'TF\Kmusic', 'CD')
 ('The Good Life', 'Trip Lee', '4/10/2012', 'Reach Records', 'CD')
 ]

cursor.executemany("INSERT INTO albums VALUES (?, ?, ?, ?, ?)", albums)
conn.commit()

# Updating and Deleting Records:

import sqlite3

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

sql = """
UPDATE albums
SET artist = 'John Doe'
WHERE artist = 'Andy Hunter'
"""
cursor.execute(sql)
conn.commit()

# Delete:

import sqlite3

conn = sqlite3.connect("mydatabse.db")
cursor = conn.cursor()

sql = """
DELETE FROM albums
WHERE artist = 'John Doe'
"""
cursor.execute(sql)
conn.commit()

import sqlite3

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

sql = "SELECT * FROM albums WHERE artist=?"
cursor.execute(sql,[("Red")])
print(cursor.fetchall()) # or use fetch
