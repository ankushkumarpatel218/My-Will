num1 = int(input("enter a number:"))
n = int(input("enter length of the series:"))
series = []
for i in range(n+1):
    if i % 2 == 0:
        num2 = num1 ** i
        series.append(num2)
    else:
        num2 = num1 ** i
        num3 = -num2
        series.append(num3)
Sum = sum(series)
print(f"1 - {num1}**1 + {num1}**2-... + {num1}**{n} = {Sum}")