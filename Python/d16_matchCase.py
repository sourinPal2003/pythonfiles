#match case look like switch case

choice = int(input("enter a number:"))

match choice:
    case 2:
        print("Abc")
    case 4:
        print("Mno")
    case 6:
        print("Xyz")
    case _ if(choice%2!=0):
        print("enter a valid choice and even number only")
    case _:
        print("enter a valid choice.")
    