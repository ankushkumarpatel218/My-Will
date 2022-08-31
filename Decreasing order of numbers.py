def order(num1, num2, num3):
    list1 = []
    list1.append(num1)
    list1.append(num2)
    list1.append(num3)
    list2 = sorted(list1, reverse=True)
    max = f"{list2[0]} > {list2[1]} > {list2[2]}"
    return max

NUM1 = int(input("enter a number:"))
NUM2 = int(input("enter a number:"))
NUM3 = int(input("enter a number:"))
print(f"\ndecreasing order of the numbers: {order(NUM1, NUM2, NUM3)}")