
num=int(input("Enter a number bellow 100:"))

if num>100:
    raise ValueError("Error! the number is not bellow 100.")

##code.........
print("Your number is ",num)









### MAKE A customError class:

class CustomError(Exception):
  "custom error occurs"
  pass

try:
  age=int(input(('Enter your age: ')))
  if(age<18):
     raise CustomError

except CustomError:
   print("you are not alligible")
  # code...
  






