class Animal():
    def __init__(self, name):
        self.name = name
    def speak(self) :
        raise NotImplementedError ("this must be an abstact method")
class  Dog(Animal) :
    def speak(self):
        return self.name + "says woof!"
class  Cat(Animal) :
    def speak(self):
        return self.name + "says meow!"
felix = Cat("felix")
fido = Dog ("fido")
print(felix.speak())
print(fido.speak())