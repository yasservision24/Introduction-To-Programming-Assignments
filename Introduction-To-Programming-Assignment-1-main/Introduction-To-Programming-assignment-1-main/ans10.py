def f(x):
    f=x**3-10.5*(x**2)+34.5*x-35
    return f
    
def slope(x):
    dx=0.000001
    s=(f(x+dx)-f(x))/dx
    return s

def main(x):
    for i in range(1,101):
        if  f(x)>0.2 or f(x)<-0.2:
            #if slope(x)!=0:
            x=x-(f(x)/slope(x))
        else:
            print("root of function is-: ",x,"          or approx value of root is-: ",round((x),1))
            break
while True:
    print("## given function has three different roots, try with different xo to get them all, such as 1,2,3,4,5,5.3,46.25 or as per your choice")      
    x=float(input("enter value of xo -: "))
    print()
    print("value of function","at",x,"is-: ",f(x), "           or approx value is-:",round(f(x)))
    print()
    main(x)
    print()
    print()
    print()