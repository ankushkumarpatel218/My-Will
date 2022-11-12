
x = int(input('Enter number: '))
list1 = []
for i in range(1,x+1):
    if x % i == 0:
        list1.append(i)
Len = len(list1)

if Len > 2:
    print(f"{x} is a composite number")
elif Len == 2:
    print(f"{x} is a prime number")
else:
    print(f'{x} is neither composite nor prime')