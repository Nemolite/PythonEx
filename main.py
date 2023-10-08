class Person:
    pass

a = Person()
print(type(a))
check = isinstance(a,Person)
print(check)

setattr(Person, 'b','Hello')

s = Person.b
print(s)







