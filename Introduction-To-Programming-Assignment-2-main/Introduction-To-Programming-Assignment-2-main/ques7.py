while True:
    import json # json does not consider single quote as string
    with open("addrbook.txt") as file1:
        file=file1.read()
        if file=="":
            dic={}
            print("book is empty!")
        else:    
            dic=json.loads((file))
            print("{")
            [print(key,':',value) for key, value in dic.items()]
            print("}")
        print()
        print()
        print("enter 1 to insert a new entry")
        print("enter 2 to delete an entry")
        print("enter 3 to find an  entry by a partial name")
        print("enter 4 to search entry by phone no")
        print("enter 5 to exit")
        a=int(input("enter your choice:- "))
        if a==1:
            n=(input("enter name:- "))
            p=input("enter phone:- ")
            l1=[]
            for i in dic.values():
                for j in i: 
                    if p in j.keys():
                        l=(i.index(j))
                        keys=[k for k, v in dic.items() if v==i]
                        st=(str(keys[0]))
                        l1.append(st)
            if len(l1)!=0:
                print("this phone no already exits in addressbook")
                print({st:(dic[st])[l]})
                print()
                print("..............................................................................................")
                continue
            em=input("enter email:- ")
            ad=input("enter address:- ")
           
            x=(ad,em)
            y={}
            y[p]=x
            if n not in dic.keys():
                l=[]
                l.append(y)
                dic[n]=l
            else:
                l=(dic[n]) 
                l.append(y)
                dic[n]=l
            with open("addrbook.txt","w") as file1:
                file1.write(json.dumps((dic))) 
                print()
                print("entry registered")
                print(".................................................................................................")
            continue
        elif a==2:
            n=(input("enter name to delete an entry:- "))
            if len(dic[n])>1:
                print("there are",len(dic[n]),"items","with the name",n,"so enter phone no of entry to be deleted")
                p=input("enter phone no:- ")
                for i in dic[n]:
                    print(i)
                    keys=[k for k,v in i.items()]
                    if str(keys[0])==p:
                        dic[n].remove(i)
            else:
                del dic[n] 
            with open("addrbook.txt","w") as file1:
                file1.write(json.dumps((dic)))
                print()
                print("entry deleted")
                print(".....................................................................................................")
            continue   
        elif a==3:
            n=input("enter partial name to get matching result:-")
            print()
            c={key: val for key, val in dic.items() if n in key}
            print(c)
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print(".....................................................................................................")
            print(".....................................................................................................")
            continue   
        elif a==4:
            p=input("enter phone no:- ")
            print()
            l2=[]
            for i in dic.values():
                for j in i: 
                    if p in j.keys():
                        l=(i.index(j))
                        keys=[k for k, v in dic.items() if v==i]
                        st=(str(keys[0]))
                        print({st:(dic[st])[l]})
                        l2.append(st)
            if len(l2)==0:
                print("this phone no is not in our addressbook")
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print(".....................................................................................................")
            print(".....................................................................................................")
            continue   
        elif a==5:
            exit() 