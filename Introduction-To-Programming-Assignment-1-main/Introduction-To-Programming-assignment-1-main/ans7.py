def savings(cost):
    r=0.5/100
    monthly_allowance=20000
    sf=0.1*20000
    t=1
    month=1
    p=2000
    saved=2000
    while saved<cost:
        saved=(saved)*(1+r*t)+2000
        month=month+1
    print("months needed to buy the laptop of",cost, "is-: ",month)
    print()
    print("amount left after buyting laptop at the end of",month,"months is-: ",saved-cost)
while True:
    cost=float(input("enter laptop cost-: "))  
    print()
    savings(cost)
    print() 
    print()    