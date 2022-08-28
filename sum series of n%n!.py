import math
def Add(b):
    lst1 = []
    for i in range(1, b+1):
        s = math.factorial(i)
        t = i/(s)
        lst1.append(t)
    Sum = sum(lst1)
    return Sum
n2 = int(input("enter  range:-"))
print(Add(n2))