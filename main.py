import pytest

def oper(a,b):
    return a/b

def get_info_of_file():

    with open("myfile.txt","r") as file:
        list1 = file.readlines()

    file.close()
    return list(map(lambda x: x[:-1], list1))

