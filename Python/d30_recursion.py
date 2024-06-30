def factorial(n):
    if(n==0 or n==1):
        return 1
    return n*factorial(n-1)


a=factorial(13)
print(a)


def fibonachi(a,b,term):
    if term==0:
        return
    
    c=a+b
    print(c,end=" ")
    fibonachi(b,c,term-1)


fibonachi(0,1,10)
