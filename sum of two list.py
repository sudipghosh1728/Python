lst1=[2,6,8,4,9]
lst2=[]
lst3=[]
n=int(input("Enter how many numbers do you want to take :\t"))
for i in range(0,len(lst1)):
    x=int(input("Enter the number"))
    lst2.append(x)
print("First list is:\t",lst1)
print("Second list is:\t",lst2)
for i in range(0,len(lst2)):
    add=lst1[i]+lst2[i]
    lst3.append(add)
print("Summetion of two list index wise is:\t",lst3)


    
