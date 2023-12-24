import random
c=0
flag=False
while flag==False:
    n=input("enter 5 letter word (all chars  in lowercase):- ")
    if len(n)!=5:
        print("invalid entry! enter 5 letter word")
    else:
        w=["apple","chain","chair","blood","block","wealth","health","table","cable","drink","dress","drive","clock","brain","black","brown","adult","march","match","north","horse","house","union","uncle","south","glass","grass","bright","hotel","light","march","motor","night","party","tower","power","prize","radio","photo","store","motel","phone","lemon","melon","water","watch","stone","place","pride","share"]
        r=random.randrange(0,len(w))
        if n==w[int(r)]:
            print(" you won the game ")
            flag=True
        else:
            c=c+1
            if c>5:
                print("still no match you lose the game")
                flag=True
            else:
                print("no match try again")
                s=str(w[r])
                cn=0
                for i in range(5):
                    if s[i]==n[i]:
                        cn=cn+1
                if cn>1:
                    print("word chosen by system",end=":- ")
                    for i in range(5):
                        if s[i]==n[i]:     
                            print(s[i],end="")
                        else:
                            print(("\033[4m" + str(s[i]) + "\033[0m"),end="")
                    print()
                    continue    
    