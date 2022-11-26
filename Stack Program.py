def push(stack):
    roll = int(input("\nEnter the roll no. of the student: "))
    name = input("Enter the name of the student:")
    marks = float(input("Enter the marks of the students: "))
    student = (roll, name, marks)
    stack.insert(0, student)
    print("\nStudent Data has been Pushed!\n")


def pop(stack):
    if len(stack) > 0:
        stack.pop()
        print("\nStudent data has been Popped out!\n")
    else:
        print("\nThere is no data to be pop!\n")


def display(stack):
    print(f"\n{stack}\n")


stack = []


def Stack():
    print("****************************\n"
          "1. Show the Stack\n"
          "2. Push data into the stack\n"
          "3. Pop data from the stack\n"
          "****************************")

    choice = input("Enter the Stack Operation: ")
    if choice == '1':
        display(stack)
        Stack()

    elif choice == '2':
        push(stack)
        Stack()

    elif choice == '3':
        pop(stack)
        Stack()


if __name__ == "__main__":
    Stack()
