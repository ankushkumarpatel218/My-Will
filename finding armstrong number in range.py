# finding armstrong number in range

lower_limit = int(input("Lower limit: "))
upper_limit = int(input("Upper limit: "))

if lower_limit < upper_limit:
    for i in range(lower_limit, upper_limit+1):
        armstrong = []
        for j in str(i):
            num = int(j) ** 3
            armstrong.append(num)
        if sum(armstrong) == i:
            print(f"Armstrong number between {lower_limit}  and {upper_limit} are: {i}")



