
import pytest

def oper(a,b):
    return a/b

def get_info_of_file():

    with open("myfile.txt","r") as file:
        list1 = file.readlines()

    file.close()
    return list(map(lambda x: x[:-1], list1))


list1 = [1,2,3,[4,{"k1":"v1","k2":[8,9,10]},6],{"t1","t2",(3,4,5)},44]
print(list1)

# Задание 1. Заменить 9 на 19
list1[3][1]["k2"][1] = 19
print(list1)
# Задание 2. Змаенить все 4 на 14
list1[3][0] = 14
list1[4].discard((3,4,5))
list1[4].update({(3,14,5)})
print(list1)
# Задание 3. Посчитать количество цифер
# list1 = [1,2,3,[4,{"k1":"v1","k2":[8,9,10]},6],{"t1","t2",(3,4,5)},44]

def counter(arr1):
    count_elemet = 0
    for i in arr1:
        if type(i)==int:
            count_elemet+=1
        if (type(i)==tuple)|(type(i)==set)|(type(i)==list):
            count_elemet += counter(i)
        if (type(i)==dict):
            for k,v in i.items():
                count_elemet += counter(v)
    return count_elemet

print(counter(list1))

# Задание 4. Удалить "t1" и 5
list1[4].discard("t1")
print(list1)
# Задание 5 . Добавить "k3" со значение "v3" в словарь
list1[3][1]["k3"] = "v3"
print(list1)
# Задание 6 Посчитать количество всех элементов (пара ключ:значение - один элемент )
# list1 = [1,2,3,[4,{"k1":"v1","k2":[8,9,10]},6],{"t1","t2",(3,4,5)},44]
# print(len(list1[3][1]["k2"]))
# print( len(list1[3][1]))
def c(arr_set):
    count_elemet =0
    for i in arr_set:
        if type(i)==tuple:
            count_elemet = len(i)
    return count_elemet

# print(c(list1[4]))
# print(len(list1[4]))
# print(len(list1[3]))
# print(len(list1))
print(len(list1[3][1]["k2"])+len(list1[3][1])+c(list1[4])+len(list1[4])+len(list1[3])+len(list1))

# from collections import namedtuple
#
#
# class Person:
#     pass
#
# a = Person()
# print(type(a))
# # <class '__main__.Person'>
# check = isinstance(a,Person)
# print(check)
#
# setattr(Person, 'b','Hello')
#
# s = Person.b
# print(s)
#
#
# class Exam:
#     def __init__(self,x,y):
#         self.a = x
#         self.b = y
#         print('Я появлюсь при создании объекта')
#
#
# obj1 = Exam(1,2)
#
# print(obj1.__dict__)
#
#
# # True
# # Hello
# # Я появлюсь при создании объекта
# # {'a': 1, 'b': 2}
#
# class Exam2:
#     def __init__(self):
#         print('__init__')
#
#     def __del__(self):
#         print('__del__')
#
#
# obj2 = Exam2()
# input('Enter to stop')
#
# class Exam3:
#     def __new__(cls, *args, **kwargs):
#         print('__new__')
#         # return super().__new__(cls)
#     def __init__(self):
#         print('__init__')
#
# obj3 = Exam3()
#
# def m(a,*,b):
#     return a,b
#
# print(m(1,b=2))
#
# LatLon = namedtuple('LatLon', 'lat lon')
# print(type(LatLon))


