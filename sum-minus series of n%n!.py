import math
def bankai(a):
    lst1 = []
    for i in range(1, a + 1):
        if i % 2 == 0:
            s = math.factorial(i)
            t = i/(s)
            t1 = -(t)
            lst1.append(t1)
        else:
            s = math.factorial(i)
            t = i / (s)
            lst1.append(t)
    Sum = sum(lst1)
    return Sum
n2 = int(input("enter  range:-"))
print(bankai(n2))