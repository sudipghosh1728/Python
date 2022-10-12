L=[]
n=int(input("Enter how many numbers of element do you want:\n"))
print("Enter the elements:\n")
for i in range(0,n):
    x=int(input())
    L.append(x)
print("The original list is=\n",L)
lst=sorted(L)
print("The second largest element is:\n")
print(lst[-2])
