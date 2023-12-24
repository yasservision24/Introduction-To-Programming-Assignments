# function to sum the future population of each group
def future_pop(n):
    total=0
    population=[50,1450,1400,1700,1500,600,1200]
    r=2.5/100
    for p in population:
        g=p
        R=1+r
        year=0
        while year<n:
            g=g*R
            R=R-0.1/100
            year=year+1
            
        r=r-0.4/100    
        total=total+g
    return total


# user input, calling function and printing of result   
print("current world popultation (in millions) is-:  ",future_pop(0))
print()
Y=0
while future_pop(Y+1)>future_pop(Y):
    Y=Y+1
print("world population will peak at the end of    ",Y,"th","  year ")
print()
print("max population of world (in millions) will be-:  ",future_pop(Y))
print()

    
    