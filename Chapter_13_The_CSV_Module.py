# Chapter 13 - The csv Module
"""
The csv modules gives the Python programmer the ability to parse CSV (Comma Separated Values ) files.
A CSV files is a human readable text file where each line has a number of fields, separated by
commas or some other delimiter.
We can think of each line as a row and each fields as a column.

"""

# Reading a CSV File
"""
There are two ways to read a CSV file.
We can use csv modules's reader function or we can use the DictReader class.

"""

import csv

def csv_reader(file_object):
    """
    Read a csv file
    """
    reader = csv.reader(file_object)
    for row in reader:
        pass
        #print("  ".join(row))


if __name__ == "__main__":
    csv_path = "TB_data_dictionary_2020-04-03.csv"
    with open (csv_path, "r") as f_obj:
        csv_reader(f_obj)




import csv

def csv_dict_reader(file_obj):
    """
    Read a CSV file using csv.DictReader
    """

    reader = csv.DictReader(file_obj, delimiter=",")

    for line in reader:
        print(line["first_name"] , line["last_name"])

if __name__ =="__main__":
    with open("CustData.csv", "r") as f_obj:
        csv_dict_reader(f_obj)


# Writing a CSV File:
"""
The csv module also has two methods that we can use to write a CSV file.
We can use the write function or the DictWriter class.
"""

import csv

def csv_writer(data, path):
    """
    Write data to a CSV file path
    """
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)

if __name__ == "__main__":
    data = ["first_name, last_name, city".split(","),
            "Tyrese, Hirthe, Strackeport".split(","),
            "Jules, Dicki, Lake Nickolasville".split(","),
            "Dedric, Medhurst, Stiedemannberg".split(",")]

    path = "output.csv"
    csv_writer(data, path)



# DictWriter:
import csv

def csv_dict_writer(path, ieldnames, data):
    """
    Write a CSV file using DictWriter
    """
    with open(path, "w", newline='') as out_file:
        writer = csv.DictWriter(out_file, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()
        for row  in data:
            writer.writerow(row)


if __name__ == "__main__":
    data =  ["first_name, last_name, city".split(","),
            "Tyrese, Hirthe, Strackeport".split(","),
            "Jules, Dicki, Lake Nickolasville".split(","),
            "Dedric, Medhurst, Stiedemannberg".split(",")]
    my_list = []
    fieldnames = data[0]
    for values in data[1:]:
        inner_dict = dict(zip(fieldnames, values))
        my_list.append(inner_dict)

    path = "dict_output.csv"
    csv_dict_writer(path, fieldnames, my_list)
