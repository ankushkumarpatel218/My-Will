list1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
list2 = [101, 210, 130, 20, 120, 30]
list3 = []
if len(list2)>len(list1):
    for i in list1:
        if i in list2:
            list3.append(i)
    print(f"common elements:{list3}")
elif len(list2)<len(list1):
    for i in list2:
        if i in list1:
            list3.append(i)
    print(f"common elements:{list3}")
else:
    for i in list1:
        if i in list2:
            list3.append(i)
    print(f"common elements:{list3}")




