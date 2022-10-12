lst=[]
n=int(input("Enter how many numbers do you want to take:\n"))
print("Enter the elements :\n")
for i in range(0,n):
    x=int(input())
    lst.append(x)
print(lst)
print(lst[2:5])
