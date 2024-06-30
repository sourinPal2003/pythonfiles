a={1,2,3}
b={4,5,6}

###two set are said to be disjoint if they have no element in common
print(a.isdisjoint(b))

c={1,2,3,4,5,6,7}
d={1,2,3}

print(c.issuperset(d))
print(d.issubset(c))

e={2,4,6,8,10}

print(e)
e.add(99)
print(e)

print(" ")

f={1,2,3,4,5}

print(f)
f.remove(3)
print(f)

'''The main difference between remove and discard is that,
 if we try to delete an item which is not present in set,
 then remove() raises an error, whereas discard() does not raise any error.'''

# f.remove(80)       #gives error
f.discard(80)       #don,t give error

print("---------------------------------")


### 'del' is a keyword which deletes the set entirely.
del f
# print(f)

### '.clear()' method clears all items in the set and prints an empty set.
e.clear()
print(type(e))
print(e)