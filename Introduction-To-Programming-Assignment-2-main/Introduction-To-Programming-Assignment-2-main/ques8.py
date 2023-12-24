while True:
    import json
    with open("pages.txt") as file1:
            file=file1.read()
            dic=json.loads((file))
    n=int(input("enter the value of N:- "))
    N=[]
    l1=[]
    l2=[]
    l2_=[]
    l2__=[]
    I=[]
    k=[]
    for i in dic.values():
        l1.append(i[0])
    for i in dic.values():
        l2.append(i[1])
        a=set(i[1])
        l2_.append(a)
        l2__.append(len(a))
    for i in dic:
        i=int(i)
        c=0
        for j in range(len(l1)):
            b=l2[j].count(i)
            if b!=0:
                c=c+l1[j]/l2__[j]
        I.append(c)
        k.append(i)
    print()
    if n==1:
        print("page with highes importance")
    else:
        print("pages with highest importance")
    d=sorted(I,reverse=True)
    e=(d[:n])
    for i in e:
        f=I.index(i)
        print(k[f])    