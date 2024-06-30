f=open("fileSeek_d51.txt",'w')
f.write("123456789abcdefghijklmnopqrstuvwxyz")
f.close()

f=open("fileSeek_d51.txt",'r')

print(f.tell())

f.seek(6)
print(f.tell())

mytxt=f.read(10)
print(mytxt)
print(f.tell())

f.close()

