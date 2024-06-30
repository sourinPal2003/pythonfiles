class person:
    name = 'Default name'
    occupation = 'Default occupation'
    age = 0

    def info(self):
        print(f"{self.name} is a {self.occupation}.His age is {self.age}")



a=person()
a.name='Sourin'
a.occupation='Sofware developer'
a.age=20
a.info()


b=person()
b.name='Subham'
b.occupation='Doctor'
b.age=38
b.info()


c=person()
c.info()




