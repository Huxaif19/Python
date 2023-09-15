class Dog (): 
    def __init__(self, name) :
        self.name = name 
    def speak(self) :
        return self.name + " says woof!"
class Cat (): 
    def __init__(self, name) :
        self.name = name 
    def speak(self) :
        return self.name + " says moew!"
niko = Dog("niko" ) 
felix = Cat("felix")
for pet in [niko, felix] :
    print(type(pet))
    print((pet.speak()))
def pet_speak(pet) :
    print(pet.speak())
print(pet_speak(niko))