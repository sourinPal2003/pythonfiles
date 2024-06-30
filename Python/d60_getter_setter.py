class infoVal:
    def __init__(self,value):
        self._value=value
    
    @property
    def cube(self):
        return self._value**3
    
    @cube.setter
    def cube(self,newValue):
        self._value=newValue



a=infoVal(10)
print(a.cube)
a.cube=5 ##--> here a.cube as setter
print(a.cube) ##--> here a.cube as getter
