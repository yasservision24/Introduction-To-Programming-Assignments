l=[]
dic={}
with open("data.txt","r") as f:
    for line in f:
        a,b,c,d = line.strip().split(',') 
        l.append((a,b,c,d))
l.sort(key=lambda x: x[3])
items=l
l1=[]
for i,item in enumerate(items):
    if item[1] == "ENTER":
        if (i == 0 or item[1] != items[i-1][1]):
            l1.append(item)
    else:
        l1.append(item)
l2=[]
for i,item in enumerate(l1):
    if item[1] == "EXIT":
        if i == len(items) - 1 or item[1] != items[i + 1][1]:
            l2.append(item)
    else:
        l2.append(item)
l=l2.copy()
for a,b,c,d in l:
    if a not in dic:
        dic[a] = []
    dic[a].append((b,c,d))
while True:
    print("press 1 to get record of student and current status")
    print("press 2 to get record of all students entered during a paricular time interval")
    print("press 3 to get record of all students who entered and exited through a particular gate")
    n=(input("enter your choice:- "))
    if n=="":
        break
    elif n=="1":
        name=input("enter name:- ")
        name=name.title()
        if name not in dic:
            print("student does not exist")
            
        else:
            with open("output.txt", 'w') as F:
                for item in dic[name]:
                    F.write((str(item).strip())+ '\n')
                print("record file of ",name," is generated as output.txt")
            t=input("enter current time:- ")
            t=" "+t
            print(name,end=" ")
            m="is not in campus"
            for i in range(len(dic[name])):
                if i!=len(dic[name])-1:
                    if dic[name][i][0]==" ENTER" and dic[name][i][2]<=t:
                        if dic[name][i+1][2]>=t:
                            m="is in campus"
                            break
                else:
                    if dic[name][i][0]==" ENTER" and dic[name][i][2]<=t:
                        m="is in campus"
                        break
            print(m)
    elif n=="2":
        en=[]
        ex=[]
        t1=input("enter start time:- ")
        t2=input("enter end time:- ")
        t1=" "+t1
        t2=" "+t2
        for i,j in dic.items():
            for k in range(len(j)):
                if j[k][0]==" ENTER":
                    if j[k][2]>=t1 and j[k][2]<=t2:
                        en.append(i)
                        break 
        for i,j in dic.items():
            for k in range(len(j)):
                if j[k][0]==" EXIT":
                    if j[k][2]>=t1 and j[k][2]<=t2:
                        ex.append(i)
                        break 
        with open("output.txt", 'w') as F:
                F.write(("students entered during this time"+ '\n'))
                for item in en:
                    F.write((str(item).strip())+ '\n')
                F.write((" "+ '\n'))
                F.write(("students exited during this time"+ '\n'))
                for item in ex:
                    F.write((str(item).strip())+ '\n')
        print("file create")  
    elif n=="3":
        ga_en=0
        ga_ex=0
        g=input("enter gate no.:- ")
        g=" "+g
        for i,j in dic.items():
            for k in range(len(j)):
                if  j[k][0]==" ENTER":
                    for k in range(len(j)):
                        if j[k][1]==g:
                            ga_en=ga_en+1
        for i,j in dic.items():
            for k in range(len(j)):
                if  j[k][0]==" EXIT":
                    for k in range(len(j)):
                        if j[k][1]==g:
                            ga_ex=ga_ex+1
        with open("output.txt", 'w') as F:
                F.write(("No of times students entered through the gate"+str(g)+"are:- "+str(ga_en)+'\n'))
                F.write((" "+ '\n'))
                F.write(("No of times students exited through the gate"+str(g)+"are:- "+str(ga_ex)+'\n'))
        print("file created")       
            
        