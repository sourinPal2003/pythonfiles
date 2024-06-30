myfile = open("myTextDocument.txt",'w')
myfile.write('this is me !')
myfile.close()

myfile= open("myTextDocument.txt",'a')
myfile.write('\nHow are you?')
myfile.close()

myfile=open("myTextDocument.txt",'r')
a = myfile.read()
print(a)
myfile.close()


###to change location of file see: d46_OSmodule.py


