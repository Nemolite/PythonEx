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


from icecream import ic
def fanc(a,b):
    rs = a * b
    ic(rs)
    return rs

print(fanc(2,3))

class Exam:
    a = 11
    # def __init__(self,a):
    #     self.a = a

    def __getattribute__(self, item):
        print('__getattribute__')
        # return object.__getattribute__(self,item)

obj = Exam()
ic(obj.a)







