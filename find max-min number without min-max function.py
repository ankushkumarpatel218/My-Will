list1 = []
n = int(input("enter length of the list:-"))

for i in range(n):
    num1 = int(input("enter a number:-"))
    list1.append(num1)
list2 = sorted(list1)
print(f"\nthe given list: {list1}\n")
print(f"the maximum number of the list: {list2[-1]}\n")
print(f"the minimum of the list: {list2[0]}\n")
