lst=[]
n=int(input("Enter how many numbers of element do you want:\t"))
for i in range(0,n):
    print("Value of index %d"%(i))
    x=int(input("Enter the number"))
    lst.append(x)
print(lst)
print("sum of a list is",sum(lst))
