l=[56]
for M in l:
    l1=[]
    l2=[]
    l3=[]
    n=400/8
    m=120/2
    x=int(min(n,m))
    for x in range(0,x+1):
        a=1
        y_1=int((400-8*x)/2)
        y_2=int((120-2*x)/1)
        y=(min(y_1,y_2))
        
        if a<=M:
            p=90*x+25*y
        else:
            p=100*x+30*y    
        l1.append(p)
        l2.append(x)
        l3.append(y)
        a=a+1
    t1=max(l1)
    t2=l1.index(t1)
    t3=l2[t2]
    t4=l3[t2]
    print("When the value of M is-: ",M,"-----    Max Profit, no of tables ,no of chairs: ", t1,"  ",t3,"  ",t4,)