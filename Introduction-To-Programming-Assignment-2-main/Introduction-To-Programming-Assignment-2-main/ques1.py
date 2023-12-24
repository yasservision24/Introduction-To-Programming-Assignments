menu = [("Samosa--------",15), ("Idli----------",30), ("Maggie--------",50), ("Dosa----------",70), ("Tea-----------",10), ("Coffee--------",20), ("Sandwich------",35), ("ColdDrink-----",25)]
I=[]
R=[]
N=[]
T=0
print("S.No.    ITEM         RATE")
print("1......-Samosa--------₹15")
print("2......-Idli----------₹30")
print("3......-Maggie--------₹50")
print("4......-Dosa----------₹70")
print("5......-Tea-----------₹10")
print("6......-Coffe---------₹20") 
print("7......-Sandwich------₹35")
print("8......-ColdDrink-----₹25")
print()
flag="+"
while flag=="+":
    print()
    m,n=(input("Enter S.No. of item,   Enter quantity:- ").split())
    m=int(m)
    n=int(n)
    if m>8 or m<1:
        print("Invalid entry!,Enter correct S.No. ")
        
    else:
        a=m-1 
        I.append(menu[a][0])
        R.append(menu[a][1])
        N.append(n)
        flag=input("Press (+) to add more items AND  (0) to exit:- ")
l=len(I)
if l>0:
    print()
    print()
    print("No.  ITEM          RATE    QUANTITY      TOTAL(₹)")
    for i in range(l):
        print(i+1,"  ",I[i],R[i],"......",N[i],".........",N[i]*R[i])
        T=T+N[i]*R[i]
    print()
    print("TOTAL   ","ITEMS--",sum(N),"   ₹--",T)
    print()    