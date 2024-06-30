'''
Python Sets:
Sets are unordered collection of data items. They store multiple items in a single variable.
 Set items are separated by commas and enclosed within curly brackets {}. 
 Sets are unchangeable, meaning you cannot change items of the set once created.
 **Sets do not contain duplicate items.
'''

mySet={23,67,23,23,23,45,45}
print(type(mySet))
print(mySet)  #{67, 45, 23}

for i in mySet:
    print(i)




#make a empty set

#wrong method:
p={}
print(type(p)) #<class 'dict'>

#right method:
q=set()
print(type(q)) 


