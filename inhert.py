
# BASE CLASS
class Animal:
    def __init__(self):
        self.name = "Bunty"
    def speak(self):
        print(f"{self.name} makes a sound")    
        
        
class Dog(Animal):
    def __init__(self, breed):
        super().__init__()
        self.breed = breed
        
    def speak(self): # override bcz animal alo had this method
        super().speak()
        print(f"{self.name} barks, it is {self.breed}")

        
        
animal = Animal()
animal.speak()

dog = Dog("bunty")
dog.speak()

animal = Animal()
animal.speak()