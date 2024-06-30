'''
Python Lists:
1) Lists are ordered collection of data items.
2) They store multiple items in a single variable.
3) List items are separated by commas and enclosed within square brackets [].
4) Lists are changeable meaning we can alter them after creation.
'''
marksList=['hi', 1 , 2, 'hello', 99, 0.5 , 45]
print(len(marksList))

print(marksList)
print(marksList[:])

print(marksList[3])

print(marksList[0:4])      #0 to 3
print(marksList[:4])       #0 to 3

print(marksList[1:6])      #1 to 5


print(marksList[1:-2])      
print(marksList[1:len(marksList)-2])      


print(marksList[-4:-2])      
print(marksList[len(marksList)-4:len(marksList)-2])      

#List Comprehension:

listC1 = [i*i for i in range(10)]
print(listC1)

listC2 = [i*i for i in range(10) if i%2==0]
print(listC2)

#_____________________________________________________________________________________________

#list to string
word_list = ['Hello,', 'World', 'my', 'name', 'is', 'sourin.']
str = ' '.join(word_list)
print(str)

#take a list input and print it
a = [int(input()) for i in range(3)]
print(a)

#take a list input in one line and print it
a = input("Enter elements separated by spaces: ").split()
print(a)


