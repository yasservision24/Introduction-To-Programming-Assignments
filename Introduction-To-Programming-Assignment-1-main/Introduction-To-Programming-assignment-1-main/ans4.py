while True:
    import math
    a=float(input("enter starting time-: "))
    if 140000-2100*a<=0:
        print("out of domain,the domain of given the function is 66.666,")
        continue
    b=float(input("enter end time-: "))
    if 140000-2100*b<=0:
        print("out of domain,the domain of given the function is 66.666,")
        continue
    if a>b:
        print("end timme can not be greater than entry time") 
        continue   
    d=0
    t=0.25
    while a<=b:
        c=a+t
        v1=2000*(math.log(140000/(140000 - 2100*a))) - 9.8*a
        v2=2000*(math.log(140000/(140000 - 2100*c))) - 9.8*c
        d=d+(((v1+v2)/2)*t)
        a=c
    print("total distance travelled-: ",d)
    print()    

