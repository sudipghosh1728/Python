lst=[]
odd_list=[]
even_list=[]
n=int(input("Enter how many numbers do you want to take :\t"))
print("Enter the elements:\n")
for i in range(0,n):
    x=int(input())
    lst.append(x)
    print(lst,end="\n")
print("The list is :\t",(lst))
for i in range(0,len(lst)):
    if (lst[i]%2==0):
        even_list.append(lst[i])
        a=[*set(even_list)]
    else:
        odd_list.append(lst[i])
        b=[*set(odd_list)]
print("Even elements are :\t",(a))
print("Odd elements are :\t",(b))
print("Sum of all even elements :\t",sum(a))
print("Sum of all odd elements :\t",sum(b))
