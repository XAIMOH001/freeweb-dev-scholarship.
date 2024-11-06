class Animal:
    def mave(self):
        print("animal is moving")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")


a = Animal()
d = Dog()
d.mave()