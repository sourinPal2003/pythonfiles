
arr=[12,34,67,89]
try:
    pos = int(input("Enter the index to see the element:"))
    print(f"the element is {arr[pos]}")
except ValueError:
    print("Please input integer only")
except IndexError:
    print("Enter a valid index in between 0 to array_size-1")
except Exception as e:
    print('error occurs::',e)
else:
    print('no error occurs')

'''
OUTPUT:

No Error:
Enter the index to see the element:2
the element is 67

ValueError:
Enter the index to see the element:sp   
Please input integer only

IndexError:
Enter the index to see the element:9
Enter a valid index in between 0 to array_size-1


'''
