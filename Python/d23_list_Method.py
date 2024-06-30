l=[36,89,23,16,90,1,86,75,10,5,78]
print(l)

l.append(60)
print(l)

l.sort()
print(l)

l.sort(reverse=True)
print(l)

print("-------------------------------------------------------------------B")

m=[36,89,16,89,23,16,90,1,86,16,75,16,10,5,78]
print(m)
print(m.index(86))
print(m.index(16,6,11)) #find 16 element from 6 index to 11 index
print(m.count(16))

n=m.copy()
print(n)

print("-------------------------------------------------------------------c")

p=[10,20,30,40,50]
print(p)
p.insert(2,56)
print(p)

q=[98,76,34,91]

p.extend(q)
# p=p+q
print(p)
print("-------------------------------------------------------------------D")

r=[23,45,63,71]
if 63 in r:
    print("yes")
else:
    print("no")

print("-------------------------------------------------------------------E")

s=[10,20,30,40,50]
print(s)
t=s
t[2]=99
print(s)
print(t)
### s and t both indicate one list 


z =[]
print(z)

