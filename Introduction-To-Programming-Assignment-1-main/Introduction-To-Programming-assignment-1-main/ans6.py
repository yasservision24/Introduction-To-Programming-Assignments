# defining function
def star_pattern(n):  
    def space(n):
        for i in range(1,2*n-1):
            print(" ",end="")
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end="")
        space(n)
        n=n-1
        for k in range(1,i+1):
            print("*",end="")
        print() 

# user input , calling function and printing pattern      
while True:
    
    n=int(input("enter no-: "))
    print()
    star_pattern(n) 
    print()
    print()