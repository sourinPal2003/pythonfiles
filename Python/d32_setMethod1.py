print("------------------------------------------------------------------------------------------------1")

s1={'A','C','D','G','H'}
s2={'B','D','E','F','G'}
print(s1)
print(s2)
print(s1,s2)
print(" ")

print(s1.union(s2))   #a U b
print(s1.intersection(s2)) #a ^ b
print(s1.symmetric_difference(s2)) #(a U b) - (a ^ b)
print(s1.difference(s2)) #a - b


print("------------------------------------------------------------------------------------------------2")

print("s1 before update with s2: ",s1)
s1.update(s2)
print("s1 after update with s2: ",s1)


### different between union and update:
### in union it's just show union or give the union part in another third set,it's dont't change s1
### but in update it's change the s1 

print("------------------------------------------------------------------------------------------------3")


s3={'A','C','D','G','H'}
s4={'B','D','E','F','G'}

print("s1 before update intersection with s2: ",s3)
s3.intersection_update(s4)
print("s1 after update intersection with s2: ",s3)

print(" ")

s5={'A','C','D','G','H'}
s6={'B','D','E','F','G'}

print(s5)
s5.difference_update(s6)
print(s5)
