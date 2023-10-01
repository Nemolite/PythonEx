# class Example:
#     ''' Класс принимает от пользователя переменные и в зависимости от операции
#     выполняет арифметическую операцию'''
#     def refresh(self):
#         ''' Выполнения арифметических операции'''
#         match self.ch:
#             case '+':
#                 self.res = self.x + self.y
#             case '-':
#                 self.res = self.x - self.y
#             case '/':
#                 self.res = self.x / self.y
#             case '*':
#                 self.res = self.x * self.y
#             case _:
#                 self.res = None
#         return self.res
#
#     def set_x(self):
#         ''' Получение первого числа '''
#         while True:
#             x = input("Введите первое число: ")
#             if not x.isnumeric():
#                 print("Вы ввели не число. Попробуйте снова: ")
#             else:
#                 self.x = int(x)
#                 break
#
#     def set_y(self):
#         ''' Получение второго числа '''
#         while True:
#             y = input("Введите второе число: ")
#             if not y.isnumeric():
#                 print("Вы ввели не число. Попробуйте снова: ")
#             else:
#                 self.y = int(y)
#                 break
#
#     def set_ch(self):
#         ''' Получение символа арифметической операции '''
#         while True:
#             ch = input("Введите арифметическую операцию: ")
#             if ch not in '+-/*':
#                 print("Вы ввели неправильно. Попробуйте снова: ")
#             else:
#                 self.ch = ch
#                 break
#
# d = Example()
# d.set_x()
# d.set_y()
# d.set_ch()
# d.refresh()
# print(d.res,end='')

# class Test:
#     pass
#
# d = Test
# list1 = dir(d)
# print(type(list1))
#
# for i in list1:
#     print(i)

# class Person:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#
#     def amarok(self,c):
#         print(c)
#         return c
#
# lider = Person(2,3)
# Person.amarok(lider,4)

class Students:
    c = 12
    def __init__(self,a,b):
        self.varA = a
        self.varB = b

    def jobpfanc(self,de):
        self._pfunc(de)

    def _pfunc(self,c):
        print(c)

st = Students(3,4)
st.jobpfanc(243)
st._pfunc(241) # не рекомендуется

# Задания
# 1. Смоделируйте с помощью ООП модель клиента банка
# 2. Создайте модель персонажа какой-нибудь игры
# 3. Создайте класс для моделирования лайков соц.сетей.
# 4. Создайте класс для моделирования бытового электроприбора (то-
# стер, стиральная машина, холодильник и т. д.)




