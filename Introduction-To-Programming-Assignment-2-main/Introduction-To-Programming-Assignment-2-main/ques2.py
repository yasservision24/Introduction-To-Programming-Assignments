A=[]
B=[]
C=[]
gr=[]
g=["A+","A","A-","B","B-","C","C-","D","F"]
count=0
flag=True
while flag==True:
    a=input("enter course no.:- ")
    if a=="":
        flag=False
        print()
    else:
        b=int(input("enter no. of credits:- "))
        c=input("enter grade received:- ")
        print()
        if c not in g:
            print("invalid grade")
            print()
            continue
        else:
            gr.append(c)
            C_={"A+":10,"A":10,"A-":9,"B":8,"B-":7,"C":6,"C-":5,"D":4,"F":2}
            c=C_[c]
            A.append(a)
            B.append(b)
            C.append(c)
            count=count+b*c
for i in range(len(A)):
    print("Course no.-",A[i],"    NO. of credits-",B[i],"     Grade-",gr[i])
s=round((float(count/sum(B))),2)  
print()
print("CGPA:- ","{:.2f}".format(s))