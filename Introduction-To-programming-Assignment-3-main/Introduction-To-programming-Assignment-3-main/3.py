l=["file1.txt","file2.txt","file3.txt","file4.txt","file5.txt"]
with open("scores.txt","w+") as xyz:
    abcd=xyz.read()
import re # re func is used to for repeatation
from collections import Counter
import random
for mi in l:
    with open(mi) as f:
        f1=f.read()
        main_c=0
        a=0
        b=0
        for i in f1:
            if i==".":
                a=a+1
            else:
                if a>0:
                    b=b+1
                    a=0
        if a>0:
            b=b+1
        main_c=main_c+b
        a=0
        b=0
        for i in f1:
            if i==",":
                a=a+1
            else:
                if a>0:
                    b=b+1
                    a=0
        if a>0:
            b=b+1
        main_c=main_c+b
        b=0
        for i in f1:
            if i==":":
                a=a+1
            else:
                if a>0:
                    b=b+1
                    a=0
        if a>0:
            b=b+1
        main_c=main_c+b
        b=0
        for i in f1:
            if i==";":
                a=a+1
            else:
                if a>0:
                    b=b+1
                    a=0
        if a>0:
            b=b+1
        main_c=main_c+b
        f1=re.sub(r'\.+', '.', f1)
        f1=re.sub(r'\,+', ',', f1)
        f1=re.sub(r'\:+', ':', f1)
        f1=re.sub(r'\;+', ';', f1)
        f1=re.sub(r'\-+', '-', f1)
        f2=f1.split(".")
        e1=f1.split()
        elst=[]
        for i in e1:
            i=i.strip()
            i=i.strip(".")
            i=i.strip(",")
            i=i.strip(":")
            i=i.strip(";")
            i=i.strip("-")
            elst.append(i)
        randm=random.sample(elst,5)
        snc=len(f2)
        i_cntr=0
        for i in f2:
            j=i.split()
            count=len(j)
            if count>35 or count>5:
                i_cntr=i_cntr+1
        f1=f1.replace("."," ")
        f1=f1.replace(","," ")
        f1=f1.replace(":"," ")
        f1=f1.replace(";"," ")
        f1=f1.replace("-"," ")
        w=f1.split()
      #  here w is  list but f1 is string
        tc=len(w)
        f1=f1.lower()
        w=f1.split()
        words=Counter(w)
        mst=(words.most_common(5)) #most common is function from itertools also remember to use counter(w) not len(w) as len(w)is int and int has no attributcalled most common
        m=0
        for i in mst:
            m=m+(i[1])
        F2=m/tc
        mst_cmmon=[]
        for i in mst:
            mst_cmmon.append(i[0])
        w=set(w)
        uc=len(list(w))
        F1=uc/tc
        F3=i_cntr/snc
        if tc>750:
            F5=1
        else:
            F5=0
        F4=main_c/tc
        result=4+F1*6+F2*6-F3-F4-F5
        with open("scores.txt","a") as r:
            r.write(mi+"\n")
            r.write("Scores:- "+str(result)+"\n")
            r.write("five most used words in descending order of usage are "+str(mst_cmmon)+"\n")
            r.write("five randomly selected words are "+str(randm)+"\n")
            r.write(""+"\n")       
print("scores file generated")