class Student:
    ##class variables
    school="RHS"

    def __init__(self,name,id):
        ##instance variables
        self.name=name
        self.id=id
    
    def show(self):
        print(f"{self.name}(id: {self.id} ) reads in {self.school}")


    ###in this way if we change in s1 object the school change for only s1 not for every object(s2,s3,s4...)
    def changeSchoolForOne(self,newSchool):
        self.school=newSchool
        

    ###but in this way the school will change for every object in the class
    @classmethod
    def changeSchoolForAll(cls,newSchool):
        cls.school=newSchool







s1=Student('sourin',1090122189)
s1.show()

s2=Student('naren',1090122930)
s2.show()



s3=Student('ushan',1090893389)

##although it change it for s3 but the scool is change for all because of classmethod
s3.changeSchoolForAll('BHS')

s3.show()


s4=Student('amar',10388274849)
s4.show()

s5=Student('rajan',1948765649)
s5.show()
