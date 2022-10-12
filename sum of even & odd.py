lst=[]
sum_even=0
sum_odd=0
print("Even numbers are:\t")
for i in range(0,n):
    if (lst[i]%2==0):
        print(lst[i])
    sum_even=sum_even+int(lst[i])
print("Sum of the even numbers")
print("Odd numbers are:\t")
for i in range(0,n):
    if(lst[i]%2!=0):
        print(list[i])
        sum_odd=sum_odd+int(lst[i])
print("Sum of odd numbers in the list is ", sum_odd)
