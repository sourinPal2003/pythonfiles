def cube(x):
    return x*x*x



listNum=[1,2,3,4,5,6,7,8]
print(listNum)




listCube=[]
for i in listNum:
    listCube.append(cube(i))

print(listCube)




##same thing using map
listCubeMap = list(map(cube,listNum))
print(listCubeMap)




##using filter:
##this fn return 'True' or 'False'
def aboveHndred(a):
    return a>100

newl=list(filter(aboveHndred,listCubeMap))
print(newl)



print('------------------------------------------------------')

from functools import reduce

def sum(a,b):
    return a+b

sumofList = reduce(sum,listNum)
print(sumofList)







