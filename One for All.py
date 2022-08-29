list1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
list2 = list1.copy()
print(f"Original list:-{list2}\n")

for i in list1:
    Dup = list1.count(i)
    if Dup>1:
        for j in range(Dup):
            list1.remove(i)
for i in list2:
    for k in list1:
        list2.remove(k)

# print(f"Only Duplicate Elements:-{list2}\n")
print(f"Non duplicate elements:-{list1}")
