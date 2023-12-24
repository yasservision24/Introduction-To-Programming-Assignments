# demand function
def demand(p):
    d=10-1.02*p
# supply function
    return d
def supply(p):
    s=1+1.06*p
    return s      
p=1
while round(demand(p),1)!=round(supply(p),1):
    p=p+p*0.05
print()
print("equilibrium price is-:",p,"    rounded equilibrium price is-:",round((p),1))
print()
print("demand at equilibrium is -:",demand(p),"    approx demand at equilibrium is-:",round(demand(p),1),)
print()
print("supply at equilibrium-:",supply(p),"     approx demand at equilibrium is-:",round(supply(p),1))    
    