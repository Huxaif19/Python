class person():
    def setName(self, name):
        self.name = name.title()
    def getName(self):
        return self.name
    def cap(self):
        return self.name.title().lower()
person1 = person()
person1.setName('r. Smith')
print(person1.getName())
print(person1.cap())
type(person1)