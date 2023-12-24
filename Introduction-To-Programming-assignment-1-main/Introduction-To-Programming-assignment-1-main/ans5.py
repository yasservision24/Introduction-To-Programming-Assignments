# factorial function
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return(f)

# cosine function
def cos(n):
    s=0
    for i in range(0,50):#actually this series continues till infinity as defined by taylor's theorem but here i am taking it till 50 as it is also sufficient
        a=fact(2*i)
        b=(-1)**i
        c=2*i
        s=(s)+(((b)*(n**c))/a)
    return(s)

# sine function
def sin(n):
    s=(0)
    for i in range(0,50):#actually this series continues till infinity as defined by taylor's theorem but here i am taking it till 50 as it is also sufficient
        a=fact(2*i+1)
        b=(-1)**i
        c=2*i+1
        s=(s)+(((b)*(n**c))/a)
    return(s)

# user input, computation and print
while True:
    n=float(input("enter angle of inclination in degree-: "))
    base=float(input("enter distance between pole and person in metre-: "))
    n=n*(3.14/180)
    print("Distance between person and the top of pole-: " , base/cos(n),"metre")
    print("height of pole-: " ,base*(sin(n)/cos(n)),"metre")
    print()
    print()
