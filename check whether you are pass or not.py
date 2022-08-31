def percent(Sum):
    total = (Sum/600)*100
    return total
lst1 = []
for i in range(6):
    mark = int(input("enter your marks:-"))
    lst1.append(mark)
Sum = sum(lst1)
total = percent(Sum)
print(f"\nTotal Percentage:{total}")
if total > 90:
    print("\njio Topper")
elif total <= 90:
    print("\nbola tha padhle!")
elif total <= 80:
    print("\ngood")
elif total <= 70:
    print("\nthik h")
elif total <= 60:
    print("\nbhai ye le chai wale job ka form")
else:
    print("\nSharma ji ke ladke ko dekh 99% laya h!")