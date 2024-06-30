a="Sourin"
print(a.upper())
print(a.lower())

b="Sourin is always Sourin. Don't underestimate with Sourin."
print(b.count("Sourin"))
print(b.replace("Sourin","Bula",2))

c="!!!Sourin!!!"
print(c.rstrip("!")) #!!!Sourin

d="I am a good boy"
print(d.split(" "))

f= "abcd Ef gH"
print(f.capitalize()) #Abcd ef gh

g="Welcome to python"
print(g.center(100))
print(len(g))
print(len(g.center(100)))

h="This is also me"
print(h.startswith("This"))
print(h.endswith("me")) #True  #it's check is the string end with give value
print(h.endswith("ma")) #False
print(h.endswith("so",2,12)) #True #is the line from (2 to 11) -->"is is also" is end with given val

m="It is python. and this is not a snake."
print(m.find("is")) #first 'is' find
print(m.index("is")) #first 'is' index
print(m.find("am")) #if we can't find, it's return -1
# print(m.index("am")) #if we can't get, it's give a error 

n= "abcd12nb3SFVA"
print(n.isalnum()) #True #only alphabet and number

p="23fyrf34sm"
print(p.isalpha()) #False #only alphabet

q="hello bhai"
print(q.islower())
print(q.isupper())

r="helo world \n"
print(r.isprintable()) #False because '\n" is not a printable character

s="     "
print(s.isspace()) #True only space only

t="World Health Organization"
u="World health organization"
print(t.istitle())
print(u.istitle())

v="ami je tomar"   #Ami Je Tomar
print(v.title()) #change into Title form

w="Abc def gHij"
print(w.swapcase()) #aBC DEF GhIJ  #upper <--> lower


