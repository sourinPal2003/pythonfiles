tup=(10,20,30,40,50,60)
print(tup[2])
print(tup[0:6])

###in tupple we can't insert element like this
###tup[3]=90

#in tupple we can esily copy tupple from one to another but in list we can't
tup2 = tup[1:4]
print(tup)
print(tup2)

###make a tupple into list
list1=list(tup2)
print(list1)

###make a list into tupple
list3=[36,47,20,59]
tup3=tuple(list3)
print(tup3)




###one element tupple

##wrong method:
p=(10)
print(type(p))

##right method
q=(10,)
print(type(q))


input_string = input("Enter elements separated by spaces: ")
input_list = input_string.split()
input_tuple = tuple(map(int, input_list))
print("Tuple created from input:", input_tuple)