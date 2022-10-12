lst=[]
n=int(input("Enter how many numbers of element do you want"))
for i in range(0,n):
    print("Value of index %d"%(i))
    x=int(input("Enter the number"))
    x=x*10
    lst.append(x)
print(lst)

