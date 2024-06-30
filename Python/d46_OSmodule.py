import os

# if not os.path.exists("os data"):
#     os.mkdir("os data")

# os.rename("os data","os data using d46")

# for i in range(1,11):
#     os.mkdir(f"os data using d46/tut{i}")



# myfoldersList = os.listdir("os data using d46")
# print(myfoldersList)


print("in which location i am in:",os.getcwd())
os.chdir("C:/Users/souri/OneDrive/Desktop")
print("in which location i am in after change:",os.getcwd())