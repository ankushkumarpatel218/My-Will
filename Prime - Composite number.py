print("******************\n1. Prime number\n2. Composite number\n******************")
choice = input("Enter What do you want to find: ")
print("**********************")
lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))
print("**********************")
for i in range(lower, upper+1):
    list1 = []
    for j in range(1, upper+1):
        if i % j == 0:
            list1.append(j)
    if choice == '1':
        if len(list1) == 2:
            print(f"The Prime numbers between {lower} and {upper} are {i}")
    elif choice == '2':
        if len(list1) > 2:
            print(f"The Composite numbers between {lower} and {upper} are {i}")

