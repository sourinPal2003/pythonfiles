f=open("fileAdv.txt",'w')
f.write("How are you?\nI am fine\nhello vai\nyes bro")
f.close()

f=open("fileAdv.txt",'r')
mytext=f.readline()
print(mytext)
mytext=f.readline()
print(mytext)
f.close()

print("----------------------------------------------------------")

f=open("fileAdv.txt",'r')
while True:
    if not mytext:
        break
    mytext=f.readline()
    print(mytext)


print("----------------------------------------------------------")


f=open("fileAdvMarks.txt",'w')
f.write("50,45,78\n90,46,87\n55,34,91")
f.close()

f=open("fileAdvMarks.txt",'r')

i=1
while True:
    line=f.readline()
    if not line:
        break

    listt=line.split(',')
    phy=listt[0]
    chem=listt[1]
    math=listt[2]

    print(f"student{i}--> Physics:{phy} Chemistry:{chem} Maths={math}")
    i=i+1







