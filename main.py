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
# d = Test()
# list1 = dir(d)
# print(type(list1))
#
# for i in list1:
#     print(i)

class Test2:
    def __init__(self,c,d):
        self.c = c
        self.d =d
    def adrok(self,a):
        print(a)
        return a
re = Test2(2,3)
Test2.adrok(re,2)

print(dir(re))
print(re.__dict__)
print(re.__class__)




