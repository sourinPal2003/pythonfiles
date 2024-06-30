list1=[10,20,30,40,50]
for element in list1:
    print(element)

print('----------------------------------------------------------------------------------A')
list2=[13,25,38,49,57]

for index,element in enumerate(list2):
    print(index)
    print(element)
print('----------------------------------------------------------------------------------B')
for index,element in enumerate(list2,start=1):
    print(index)
    print(element)


