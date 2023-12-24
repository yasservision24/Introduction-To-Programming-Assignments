print()
def up(n):
    global p
    if n>0:
        for i in range(n):
            print("*",end=" ")
        for i in range(p):
            print(" ",end=" ")
        p=p+2
        for i in range(n):
            print("*",end=" ")
        print()
        n=n-1
        up(n)
def dp(m):
    global q
    if m<=n:
        for i in range(m):
            print("*",end=" ")
        for i in range(q):
            print(" ",end=" ")
        q=q-2
        for i in range(m):
            print("*",end=" ")
        print()
        m=m+1
        dp(m)
n=int(input("enter n:- "))
print(n)
print()
for i in range(2*n):
    print("*",end=" ")
print()
n=n-1
p=2
up(n)
t=n+1
m=2
q=2*(t-m)
dp(m)
for i in range(2*t):
    print("*",end=" ")
print()

