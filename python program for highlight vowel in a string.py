str1 = input("enter a string:-")

for i in str1:
    if i in list("aeiouAEIOU"):
        str1 = str1.replace(i,i.upper())
print(str1)