lst1=[]
lst2=[]
lst3=[]
n=int(input("Enter how many numbers do you want to take:\n"))
print("Enter the elements :\n")
for i in range(0,n):
    x=int(input())
    lst1.append(x)
print(lst1)
n=int(input("Enter how many numbers do you want to take:\n"))
print("Enter the elements :\n")
for i in range(0,n):
    y=int(input())
    lst2.append(y)
lst3=lst1[2:5]+lst2
print(lst3)
