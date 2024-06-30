class Shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def area(self):
        return self.x*self.y
    

class Circle(Shape):
    def __init__(self,r):
        self.r=r
        super().__init__(r,r)

    def area(self):
        return 3.14* super().area()


c1 = Circle(10)
print(c1.area())
