## single / basic inheritance
#
#class Parent:
#    def __init__(self, name):
#        self.name = name
#    def greet(self):
#        print(f"Hello, my name is {self.name}")
#        
#class Child(Parent):
#    def play(self):
#        print(f"{self.name} is playing")
#        
#                    
#child = Child("Soham")
#child.play()
#child.greet()


# multilevel 
#class Grandparent :
#    def __init__(self, name):
#            self.name = name
#    def story(self):
#        print(f"{self.name} tells a story")   
#             
#class Parent(Grandparent):
#    
#    def greet(self):
#        print(f"Hello, my name is {self.name}")
#        
#class Child(Parent):
#    def play(self):
#        print(f"{self.name} is playing")
#
#
#child = Child("Soham")
#child.play()
#child.greet()
#child.story()


# hirarchial 

#class Parent:
#    def __init__(self, name):
#        self.name = name
#    def greet(self):
#        print(f"Hello, my name is {self.name}")
#        
#class Child1(Parent):
#    def play(self):
#        print(f"{self.name} is playing")
#        
#class Child2(Parent):
#    def study(self):
#        print(f"{self.name} is studying")        
#                    
#child = Child1("Soham")
#child.play()
#child.greet()
#
#chill = Child2("Soma")
#chill.study()
#chill.greet()

# multiple 


#class A:
#    def __init__(self, name):
#        self.name = name
#    def greet(self):
#        print(f"Hello from A {self.name}")
#        
#class B(A):
#    def greet(self):
#        print(f"hello from B, {self.name}")
#        super().greet()    
#        
#class C(A):
#    def greet(self):
#        print(f"hello from C, {self.name}")
#        
#        super().greet()     
#    
#class D(B,C):
#    def greet(self):
#        print(f"hello from D, {self.name}")
#        
#        super().greet()              
#                    
#d = D("Frank")
#d.greet()



# hybrid


# BASE CLASS
class Animal:
    def __init__(self, name):
        self.name = name
    def sound(self):
        print(f"{self.name} makes a sound")    
        
        
class Mammel(Animal):
    def feed(self):
        print(f"{self.name} is feeding, milk")

class Bird(Animal):
    def fly(self):
        print(f"{self.name} is flies")
        
        
class Bat(Mammel, Bird): 
    def __init__(self, name):
        Mammel.__init__(self,name)
         
    def nocturnal(self):
        print(f"{self.name} is nocturnal")     


bat = Bat("Bruce")
bat.sound()
bat.feed()
bat.fly()
bat.nocturnal()