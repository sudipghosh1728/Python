lst=[]
n=int(input("Enter how many numbers do you want to input:\n"))
for i in range(0,n):
    x=int(input())
    lst.append(x)
print(lst)
sm=0
for i in range(0,n):
    sm=sm+lst[i]
print(sm)
