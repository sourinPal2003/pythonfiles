def workfn(a,b=20):
    c=1000*a+b
    print(c)

workfn(100)
workfn(50,90)
workfn(b=20,a=40)

def avg(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print(sum/len(numbers))


avg(10,100)
avg(10,40,90,100)