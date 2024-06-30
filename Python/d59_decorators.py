## Define a decorator
def myDecorator(fn):
    def wrapper():
        print('Before function something happen')
        fn()
        print('After function something happen')
    return wrapper


## decorate a function
@myDecorator
def say():
    print("Hi! how are you?")


##call the decorated functions
say()

