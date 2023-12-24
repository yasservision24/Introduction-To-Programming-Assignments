c=[]
l1=[]
l2=[]
dict={}
n=int(input("enter no. of students:- "))
print(".....................................................")
print()
for i in range(1,n+1):
    d={}
    print("____________________________________________________________________________________________________")
    name=input("yearbook of STUDENT_"+str(i)+" So enter name of STUDENT_"+str(i)+" :- ")
    print("----------------------------------------------------")
    l1.append(name)
    for j in range(1,n+1):
        if j==i:
            pass
        else:
            name2=input("name of STUDENT_"+str(j)+" for regestering  sign"+" in the yearbook of STUDENT_"+str(i)+" :- ")
            d[name2]=int(input("enter (1) for signed & (0) for unsigned:- "))
    dict[i]=d
    count=0
    for C in d.values():
        if C==1:
            count=count+1
    c.append(count)                                        
    
    
    print("____________________________________________________________________________________________________")
    print()
    print()
ind=[index for index,item in enumerate(c) if item==max(c)]
for i in (ind):
    print("student",("\033[4m" + str(l1[i]) + "\033[0m"),"has collection of",("\033[4m" + str(c[i]) + "\033[0m"),"signs which is highest collection of sign in a batch")
ind1=[index for index,item in enumerate(c) if item==min(c)] 
print("=====================================================================================")
for i in (ind1):
    
    print("student",("\033[4m" + str(l1[i]) + "\033[0m"),"has collection of",("\033[4m" + str(c[i]) + "\033[0m"),"signs which is lowest collection of sign in a batch")   