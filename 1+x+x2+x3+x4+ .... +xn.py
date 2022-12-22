num1 = int(input("enter a number:"))
n = int(input("enter length of the series:"))
series = []
for i in range(n+1):
    num2 = num1 ** i
    series.append(num2)
Sum = sum(series)
print(f"1+{num1}**1+{num1}**2+...+{num1}**{n} = {Sum}")


