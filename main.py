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
import random

from icecream import ic
# def fanc(a,b):
#     rs = a * b
#     ic(rs)
#     return rs
#
# print(fanc(2,3))
#
# class Exam:
#     a = 11
#     # def __init__(self,a):
#     #     self.a = a
#
#     def __setattr__(self, key, value):
#         print(key)
#         print(value)
#
#     # Срабатывает при обращение к атрибуту класса
#     def __getattribute__(self, item):
#         print('__getattribute__')
#         return object.__getattribute__(self,item)
#
#     # Срабатывает при обращение к несуществующему атрибуту класса
#     def __getattr__(self, item):
#         print('__getattr__')
#
#     def __delattr__(self, item):
#         print('__delattr__')
#
#
#
# obj = Exam()
# ic(obj.a)
# ic(obj.s)
#
# obj.a =12
# del obj.s

# class Exam:
#     def get_a(self):
#         return self.__a
#
#     def set_a(self,a):
#         self.__a = a
#
#     a = property(get_a, set_a)
#
# obj = Exam()
# obj.a = 12
# ic(obj.a)
#
#
# class Exam2:
#     @property
#     def a(self):
#         return self.__a
#     @a.setter
#     def a(self,a):
#         self.__a = a
#
#
# obj2 = Exam2()
# obj2.a = 12
# ic(obj.a)
#
# class Modi:
#     def __call__(self,a,b, *args, **kwargs):
#         return a + b
#
# obj3 = Modi()
# ic(obj3(2,3))
#
#
# class Real:
#     def __init__(self, func):
#         self.__fn = func
#
#     def __call__(self, x, *args, **kwargs):
#         return self.__fn(x + 100)
#
# def mfu(a):
#     return a
#
# mfu = Real(mfu)
# ic(mfu(4))
#
# A = [2, 1, 10, 3, 4, 5, 11, 10]
# B = [3, 5, 7, 9, 5]
# ic(sum(A+B))
#
# A1 = {2, 3}
# ic(A1)


# from random import randint
# n = int(input("Введите 1 число = "))
# m = int(input("Введите 2 число = "))
# arrN = [random.randint(1,100) for i in range(n)]
# arrM = [random.randint(1,100) for i in range(m)]
# print(len(set(arrN).intersection(set(arrM))))


# uarrN = set(arrN)
# uarrM = set(arrM)
# result = uarrN.intersection(uarrM)
# ic(result)
# ic(len(result))

# def DictPascalTriangle(rows):
#     pascal_triangle = [1]
#     dict_pascal_triangle = {0:pascal_triangle}
#     for i in range(rows):
#         print(dict_pascal_triangle)
#         pascal_triangle = [sum(x) for x in zip([0] + pascal_triangle, pascal_triangle + [0])]
#         dict_pascal_triangle = {i+1:pascal_triangle}
#
# N = int(input("Введите число = "))
# DictPascalTriangle(N)

# a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# N = int(input("Введите число = "))
# if (N in a):
#     index = a.index(N)
#     arrA = list(a)
#     arrA.pop(index)
#     a = tuple(arrA)
#     print(a)
# else:
#     print(a)

# print('Первый список самы длинный' if len(input("Введите 1 список = "))>len(input("Введите 2 список = ")) else 'Второй список самый длинный')

class Main:
    def __init__(self):
        print('Создание объекта Main')
obj = Main()











