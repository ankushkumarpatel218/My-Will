import math
num1 = int(input("enter a number:"))
n = int(input("enter length of the series:"))

series = []
for i in range(1, n+1):
    if i % 2 == 0:
        num2 = (num1**i)/math.factorial(i)
        num3 = -num2
        series.append(num3)
    else:
        num2 = (num1 ** i) /math.factorial(i)
        series.append(num2)
Sum_series = sum(series)
print(f"{num1} - {num1}**2/2! + {num1}**3/3! ... {num1}**{n}/{n}!: {Sum_series}")
