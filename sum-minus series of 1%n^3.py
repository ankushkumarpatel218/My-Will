list1 = []

n = int(input("enter limit:-"))
for i in range(1,n+1):
    if i%2==0:
        num1 = 1/(i**3)
        num3 = -(num1)
        list1.append(num3)
    else:
        num2 = 1/(i**3)
        list1.append(num2)
total = sum(list1)
print(total)