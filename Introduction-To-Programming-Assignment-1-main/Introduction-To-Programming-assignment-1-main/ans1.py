def _1(n):
    l1=[1,2,3,4,5,6,7,8,9]
    l2=["One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
    a=l1.index(n)
    A=str(l2[a])
    return A
def _2(n):
    l1=[2,3,4,5,6,7,8,9]
    l2=["Twenty","Thirty","Fourty","Fifty","Sixty","Seventy","Eighty","Ninety"]
    a=l1.index(n)
    A=str(l2[a])
    return A
def __1(n):
    l1  =[0,1,2,3,4,5,6,7,8,9]
    l2=["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
    a=l1.index(n)
    A=str(l2[a])
    return A
while True:
    m=int(input("enter no b/w 0 and 100 : "))
    if m<100:
        if m==0:
            print("Zero")
        else:
            s=str(m)
            l=len(s)
            for i in range(-1,-l-1,-1):
                n=int(s[i])
                b=abs(i)
                if b==1:
                    if n==0:
                        o=""
                    else:
                        o=_1(n)    
                elif b==2: 
                    if n!=1:
                        if n==0:
                            t=""
                        else:
                            t=_2(n) 
                    else:
                        t=__1(int(s[-1]))
                        o=""        
            if l==1:
                print(o)
            elif l==2:
                print(t,o) 
    else:
        print("Invalid entry! enter no. lesser than 100 i.e. upto 99 and greater than or equal to zero:-") 
        print()                                                