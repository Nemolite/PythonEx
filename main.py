class Person:
    pass

a = Person()
print(type(a))
# <class '__main__.Person'>
check = isinstance(a,Person)
print(check)

setattr(Person, 'b','Hello')

s = Person.b
print(s)


class Exam:
    def __init__(self,x,y):
        self.a = x
        self.b = y
        print('Я появлюсь при создании объекта')


obj1 = Exam(1,2)

print(obj1.__dict__)


# True
# Hello
# Я появлюсь при создании объекта
# {'a': 1, 'b': 2}












