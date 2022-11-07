# GCD - Greatest Common Divisor

a = int(input("enter num: "))
b = int(input("enter num: "))

if a > b:
    num1 = a
elif a < b:
    num1 = b
else:
    num1 = a

list1 = []
for i in range(1,num1+1):
    if a % i == 0 and b % i == 0:
        list1.append(i)
HCF = max(list1)
print(f"\nHCF of {a} and {b} is {HCF}")

LCM = (a*b)//HCF
print(f"\nLCM of {a} and {b} is {LCM}")

GCD = (a*b)//LCM
print(f"GCD of {a} and {b} is {GCD}")

