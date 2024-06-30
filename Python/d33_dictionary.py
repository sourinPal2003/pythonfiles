infoDic = {'k':'element','name':'Sourin','age':20,'eligible':True}
print(infoDic)
print(infoDic.values())
print(infoDic.keys())

print(infoDic.items()) ###give a pair of key and element

for k,elm in infoDic.items():
    print(f"{k}'s value is {elm}")

print(infoDic['k'])
print(infoDic['name'])
print(infoDic['age'])
print(infoDic['eligible'])

# print(infoDic['Roll'])   ## if key not present give error
print(infoDic.get('Roll')) ## if key not present don't give error just write None


#let make a y dict where key is value of x and value is key of x
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
y = dict((value, key) for key, value in x.items())
print(y)

#sort a dictionary by value
a = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
b=dict(sorted(a.items(), key=lambda x: x[1]))
print(b)


d = {i: i*i for i in range(10)}
print(d)

###note: https://docs.python.org/3/tutorial/datastructures.html#dictionaries