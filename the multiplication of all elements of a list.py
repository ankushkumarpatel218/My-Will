def multiply(list2):
    mul = 1
    for k in range(len(list2)):
        num2 = list2.pop()
        mul *= num2
    return mul