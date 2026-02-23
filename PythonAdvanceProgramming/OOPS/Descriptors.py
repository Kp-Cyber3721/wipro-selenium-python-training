#descriptor -  control the access of the object attributes
#_get_()
#_set_()
#_delete_()

class Desc:
    def __get__(self, instance, owner):
        print("getting the value")
        return 10

class Test:
    x = Desc();

t=Test();
print(t.x)

#this non-data descriptor - use only __get__ descriptor
#data desc uses both get and set method

class mydesc:
    def __get__(self, instance, owner):
        return instance._value
    def __set__(self, instance, value):
        print("Setting the value")
        instance._value = value
class Test:
    x = mydesc()

t = Test()
t.x = 100
print(t.x)

#delete
class Name:
    def __get__(self, instance, owner):
        return instance._name

    def __set__(self, instance, value):
        instance._name = value
    def __delete__(self, instance):
        print("Deleting name")
        del instance._name

class Person:
    name = Name()
p= Person()
p.name = "Harsha"
del p.name






