def peak():
    arr=[35,29,38,48,50]
    try:
        pos = int(input("Enter the index to see the element:"))
        print(f"{arr[pos]} is peeked.")
        return arr[pos]
    except:
        print("error occupied!")
        return 0
    finally:
        print("I am always exicuted even the function return.")


peak()



'''
OUTPUT:

no Error:
Enter the index to see the element:3
48 is peeked.
I am always exicuted even the function return.

Error:
Enter the index to see the element:sj
error occupied!
I am always exicuted even the function return.
'''
