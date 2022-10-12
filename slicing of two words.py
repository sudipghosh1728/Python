
str = input("Enter 2 words -\t")
for i in range(0,len(str)):
    if (str[i] == " "):
        break
str = str[i+1:] + str[i] + str[:i]
print(str)
