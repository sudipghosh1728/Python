lst=[]
n=int(input("Enter the number"))
for i in range(0,n):
    print("value is in the index %d"%(i))
    x=int(input("Enter the the number"))
    lst.append(x)
print(lst)
print("Sum of a list",sum(lst))
