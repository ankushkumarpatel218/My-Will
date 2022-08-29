list1 = []
n = int(input("enter length of the list:-"))

for i in range(n):
    num1 = int(input("enter a number:-"))
    list1.append(num1)
print(f"\nList before removing elements:-{list1}\n")
N = int(input("enter how many elements you want to remove:-"))
Remove = []
for j in range(N):
    remove = int(input("enter element that you want to remove:-"))
    Remove.append(remove)
for k in Remove:
    if k in list1:
        list1.remove(k)
    else:
        print(f"\n{k} is not in list1")
print(f'\nList after removing:-{list1}')
print(f"\nremoved elements:-{Remove}")