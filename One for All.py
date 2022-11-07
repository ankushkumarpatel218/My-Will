with open('text file.txt','r') as file:
    Read = file.readlines()
    for i in Read:
        line = i.split()
        for j in line:
            print(f"#{j}", end="")
        print("")
        