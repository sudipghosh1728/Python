n=int(input("Enter the number"))
s=0
temp=n
while(n>0):
    f=1
    r=n%10
    for j in range(1,r+1):
        f=f*j
    s=s+f
    n=n//10
if(s==temp):
    print("It is a peterson number\n")
else:
    print("It is not a petrson number \n")
