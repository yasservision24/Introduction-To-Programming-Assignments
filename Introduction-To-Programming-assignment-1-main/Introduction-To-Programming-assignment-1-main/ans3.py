n=1
d=0
x=5
y=5
while n>0:    
    n=int(input("enter distance: "))
    print("##journey end when distance is zero")
    print()
    if n<=25:
        y=y+n
        d=d+(n)
    elif n>=26 and n<=50:
        y=y-n
        d=d+(n)
    elif n>=51 and n<=75:
        x=x+n
        d=d+(n)    
    elif n>=76:
        x=x-n
        d=d+(n)
e=(((x-5)**2+(y-5)**2)**(1/2))
print("Total distance covered-:",d, "   Distance b/w final and initial position-:",e ,"   X coordinate-:",x,"   Y cooridinate-:" ,y)
print()

