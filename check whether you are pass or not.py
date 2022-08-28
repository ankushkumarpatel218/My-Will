lst1 = []

for i in range(6):
    mark = int(input("enter:-"))
    lst1.append(mark)
Sum = sum(lst1)
total = (Sum/600)*100
print(total)
if total > 90:
    print("jio Topper")
elif total <= 90:
    print("bola tha")
elif total <=80:
    print("good")
elif total <= 70:
    print("thik h")
elif total<=60:
    print("bhai ye le chai wale job ka form")
else:
    print("pata nhi kaun si gali do tereko")