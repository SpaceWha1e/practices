class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print("The", self.name, "sat down ;)")

    def roll_over(self):
        print("The", self.name, "rolled over :D")


my_dog = Dog('lucy', 3)
my_dog.sit()
my_dog.roll_over()

