def pattern():
    global alphabets
    import string
    print("**********************\n1.Uppercase Alphabets\n2.Lowercase Alphabets\n**********************")
    choice = input("Enter your choice: ")
    if choice == '1':
        alphabets = list(string.ascii_uppercase)
    elif choice == '2':
        alphabets = list(string.ascii_lowercase)
    alphabets.insert(0, " ")
    n = int(input("Enter the no. of rows: "))
    if n <= 26:
        for i in range(1, n + 1):
            for j in range(1, (n - i) + 1):
                print(" ", end="")
            for k in range(1, i + 1):
                print(alphabets[k], end="")
            for s in range(i - 1, 0, -1):
                print(alphabets[s], end="")
            print("")
    else:
        print("enter number between range 1 - 26!")
        pattern()

if __name__ == "__main__":
    pattern()