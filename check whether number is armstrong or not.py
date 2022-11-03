x = input('Enter number: ')
list1 = []
for i in x:
    n = int(i)
    n1 = n**3
    list1.append(n1)

Sum = sum(list1)

if Sum == int(x):
    print(f'{x} is an Armstrong Number')

else:
    print(f'{x} is not an Armstrong Number')

