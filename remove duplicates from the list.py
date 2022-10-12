lst=[]
lst1=[]
n=int(input("Enter how many numbers of element do you want to take:\t"))
for i in range(0,n):
    x=int(input("Enter the elements"))
    lst.append(x)
print("The list is :",lst)
for i in lst:
    if i not in lst1:
        lst1.append(i)
lst=lst1
print("List after removing duplicates",lst)
