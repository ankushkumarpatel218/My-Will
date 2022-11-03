
x = int(input('Enter number: '))
list1 = []
for i in range(1, x):
    if x % i == 0:
        list1.append(i)

if sum(list1)==x:
    print(f'{x} is a Perfect Number ')

else:
    print(f'{x} is not a Perfect Number ')
