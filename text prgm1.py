# Q- Write a program to accept string/sentences from the user till the user enters “END” to.
# Save the data in a text file and then display only those sentences which begin with an uppercase alphabet
def user():
    with open("text file1.txt",'w') as file:
        while True:
            user1 = input("Enter: ")
            file.write(f"{user1}\n")
            if user1 == 'END':
                break
            else:
                continue
    with open("text file1.txt",'r') as file:
        Read = file.readlines()
        for i in Read:
            if i[0].isupper():
                print(i,end="")

if __name__ == "__main__":
    user()
