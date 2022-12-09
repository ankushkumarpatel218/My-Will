lower_val = int(input("Enter lower limit: "))
upper_val = int(input("Enter upper limit: "))

for i in range(lower_val, upper_val+1):
    list1 = []
    for j in range(1,i+1):
        if i % j == 0:
            list1.append(j)
    if len(list1) == 2:
        print(f"the prime number between {lower_val} and {upper_val} are: {i}")


