class person:
    ##Constructor
    def __init__(self,nm,oc):
        self.name=nm
        self.occupation=oc
        print(f"Constructor Created")

    def info(self):
        print(f"{self.name} is a {self.occupation}.")



a=person('Sourin','software developer')

a.info()
    




note='''
A constructor is a special method in a class used to create and initialize an object of a class.
There are different types of constructors. 
Constructor is invoked automatically when an object of a class is created.

A constructor is a unique function that gets called automatically when an object is created of a class.
The main purpose of a constructor is to initialize or assign values to the data members of that class. 
It cannot return any value other than None.



Types of Constructors in Python,
1) Parameterized Constructor:
    When the constructor accepts arguments along with self, it is known as parameterized constructor.
    These arguments can be used inside the class to assign the values to the data members.
    ex:
        def __init__(self,nm,oc):
        self.name=nm
        self.occupation=oc

2) Default Constructor:
    When the constructor doesn't accept any arguments from the object and has only one argument, self,
 in the constructor, it is known as a Default constructor.
    ex:
        def __init__(self):
        print(f"Constructor Created")

 '''



