list1 = []
n = int(input("enter length of the list:-"))

for i in range(n):
    num1 = int(input("enter a number:-"))
    list1.append(num1)
positive = []
negative = []
for j in list1:
    if j >= 0:
        positive.append(j)
    else:
        negative.append(j)
print(f"\nThe Given List:-{list1}")
print(f"\nList of positive numbers:-{positive}")
print(f"\nList of negative numbers:-{negative}")
