list1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

print(f"\nList before removing duplicates: {list1}")
for i in list1:
    dup = list1.count(i)
    if dup>1:
        for j in range(dup-1):
            list1.remove(i)
print(f"\nList after removing duplicates: {list1}")
