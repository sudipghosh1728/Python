L=[]
n=int(input("enter how many numbers do you want to take:\n"))
for i in range(0,n):
    x=int(input())
    L.append(x)
print("The List Is=",L)
for i in range(0,n):
    if(L[i]%2==0):
        print(L[i],"is even")
    else:
        print(L[i],"is odd")
        
    
