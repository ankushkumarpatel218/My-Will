list1 = []
n = int(input("enter length of the list:-"))

for i in range(n):
    num1 = int(input("enter a number:-"))
    list1.append(num1)
even = []
odd = []
for j in list1:
    if j % 2 == 0:
        even.append(j)
    else:
        odd.append(j)
print(f"\nThe Given List:-{list1}")
print(f"\nList of Even numbers:-{even}")
print(f"\nList of Odd numbers:-{odd}")
