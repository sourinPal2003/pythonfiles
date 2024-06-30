class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
    def show(self):
        print(f"{self.name}'s salary is {self.salary}")
    
    ##classmethod as a alternative constructor
    @classmethod
    def fromStr(cls,str):
        return cls(str.split('-')[0],int(str.split('-')[1]))


##using normal method
e1=Employee('Harish',5000)
e1.show()

##using class method
e2=Employee.fromStr('Amitav-2000')
e2.show()