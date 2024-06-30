# Define a decorator that accepts functions with arguments
def myDecorator(fn):
    def wrapper(*args, **kwargs):
        print('Before function something happens')
        fn(*args, **kwargs)
        print('After function something happens')
    return wrapper

# Decorate a function
@myDecorator
def sum(a, b):
    print(a + b)

# Decorate another function
@myDecorator
def diff(a, b):
    print(a - b)

# Call the decorated functions
sum(10, 8)
print('------------------------------------------------------')
diff(10, 8)
