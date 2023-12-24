tup1=((1,2),(5,6),(7,19),(9,2),(12,2),(5,3))
l1=[]
l2=[]
for i in tup1:
    l1.append(i+(1,))
x=int(input("enter cx:- "))
y=int(input("enter cy:- "))
t1=(x,0,0),
t2=(0,y,0),
t3=(0,0,1),
tup2=((t1)+(t2)+(t3))
for i in tup2:
    l2.append(i)
m=[]
for i in range(len(l1)):
    ml=[]
    m1=l1[i][0]*x
    m2=l1[i][1]*y
    m3=l1[i][2]*1
    ml.append(m1)
    ml.append(m2)
    ml.append(m3)
    m.append(ml)
print()
print(m)            