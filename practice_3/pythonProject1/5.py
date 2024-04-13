class Nicola:

    default_name = "Николай"
    __slots__ = ['name', 'age']

    def __init__(self, name, age):

        if name == "Николай":
            self.name = "Николай"
        else:
            self.name = "Я не " + name + ", я Николай"

        self.age = age


person1 = Nicola("Иван", 31)
person2 = Nicola("Николай", 14)
print(person1.name)
print(person2.name)
try:
    person2.surname = 'Петров'
    print(person2.surname)
except AttributeError:
    print('Попытка создать дополнительный атрибут.\nОТКАЗАНО')

