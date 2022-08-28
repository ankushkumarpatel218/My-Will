list1 = []

n = int(input("enter limit:-"))
for i in range(1,n+1):
    num1 = 1/(i**3)
    list1.append(num1)
total = sum(list1)
print(total)