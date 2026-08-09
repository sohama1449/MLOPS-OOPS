class Employee:
    # special funcion/methods/ magic methos(constructor)/dunder method
    def __init__(self): 
        print(id(self))
        print("starts the constructor")
        self.id = 123
        self.designation = "Software Engineer"
        self.salary = 50000
        print("ends the constructor")
        
    def travel(self, destination):
        print("Travelling method is called")
        print(f"Travelling to {destination}")
            

#create an obj/ instance of class Employee

sam = Employee()
print(id(sam))

#print(sam.id)        
sam.travel("Kolhapur")

print(type(sam))