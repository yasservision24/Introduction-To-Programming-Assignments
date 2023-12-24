wts=[(10,5),(10,5),(10,5),(20,10),(50,15),(100,20),(100,20),(100,20)]
l=[]
t=[]
g=[]
file=open("IPmarks.txt")
file1=open("IPgrades.txt","w")
data=file.read()
data1=data.split("\n")
for i in (data1):
    l.append([i])
n=(len(l))
for i in range(n):
    l[i]=(l[i][0].split(","))
for i in range(n):
    r=0
    for j in range(1,len(l[i])):
    	r=r+(((float(l[i][j]))/(wts[j-1][0]))*(wts[j-1][1]))
    t.append((round(r,3)))
for i in t:
    if i>80:
        g.append("A")
    elif i>70:
        g.append("A-")
    elif i>60:
        g.append("B")    
    elif i>50:
        g.append("B-")
    elif i>40:
        g.append("C")    
    elif i>35:
        g.append("C-") 
    elif i>30:
        g.append("D")
    elif i<=30:
        g.append("F")  
file1.write("roll_no, total_marks , grade")     
file1.write("\n")   
for i in range(n):
    file1.writelines(str((l[i][0],t[i],g[i])))
    file1.write("\n")
file.close()
file1.close()    
print("file (IPgrades.txt) created")
    
    
    