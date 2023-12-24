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
    m=int(input("enter no lesser than 100 crore: "))
    if m<1000000000:
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
                elif b==3:
                    if n==0:
                        h=""
                    else:
                        h=_1(n)+" Hundred"
                elif b==4:
                    if n==0:
                        th=""
                    else:
                        th=_1(n)+" Thousand"
                elif b==5:
                    if n!=1:
                        if n==0:
                            tth=""
                        else:
                            if int(s[-4])==0:
                                tth=_2(n)+" Thousand"
                            else:
                                tth=_2(n)
                    else:
                        tth=__1(int(s[-4]))
                        th=" Thousand"
                elif b==6:
                    if n==0:
                        lac=""
                    else:
                        lac=_1(n)+" Lac"
                elif b==7:
                    if n!=1:
                        if n==0:
                            tlac=""
                        else:
                            if int(s[-6])==0:
                                tlac=_2(n)+" Lac"
                            else:
                                tlac=_2(n)
                    else:
                        tlac=__1(int(s[-6]))+" Lac"
                        lac=""
                elif b==8:
                    if n==0:
                        cr=""
                    else:
                        cr=_1(n)+" Crore"
                elif b==9:
                    if n!=1:
                        if n==0:
                            tcr=""
                        else:
                            if int(s[-8])==0:
                                tcr=_2(n)+" Crore"
                            else:
                                tcr=_2(n)  
                    else:
                        tcr=__1(int(s[-8]))
                        cr=" Crore"                    
            if l==1:
                print(o)
            elif l==2:
                print(t,o)
            elif l==3:
                print(h,t,o)       
            elif l==4:
                print(th,h,t,o)       
            elif l==5:
                print(tth,th,h,t,o)
            elif l==6:
                print(lac,tth,th,h,t,o)       
            elif l==7:
                print(tlac,lac,tth,th,h,t,o)            
            elif l==8:
                print(cr,tlac,lac,tth,th,h,t,o)       
            elif l==9:
                print(tcr,cr,tlac,lac,tth,th,h,t,o)
                print()        
    else:
        print("invalid entry! enter lesser than 100 crores")
        print()          