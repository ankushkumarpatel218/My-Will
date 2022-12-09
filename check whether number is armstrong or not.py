x = int(input('Enter number: '))
list1 = []
for i in str(x):
    n1 = int(i) ** 3
    list1.append(n1)

Sum = sum(list1)

if Sum == int(x):
    print(f'{x} is an Armstrong Number')

else:
    print(f'{x} is not an Armstrong Number')

