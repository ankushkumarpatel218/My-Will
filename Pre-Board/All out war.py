# with open("TextFile.txt", "w") as file:
#     Lines = []
#     while True:
#         line = input("Write to file: ")
#         Lines.append(f"{line}\n")
#         if input("Quit(*)") == "*":
#             break
#         else:
#             continue
#
#     file.writelines(Lines)

# import pickle
# with open("BinaryFile.dat", 'wb') as bfile:
#     data = {}
#     while True:
#         name = input("Enter name: ")
#         roll = int(input("Enter the roll number: "))
#         marks = float(input("Enter the marks : "))
#         data['Roll no.'] = roll
#         data["Name"] = name
#         data['Mark'] = marks
#         pickle.dump(data, bfile)
#         if input("Quit(*)") == "*":
#             break
#         else:
#             continue

# with open("BinaryFile.dat", 'rb') as bfile:
#     try:
#         while True:
#             data = pickle.load(bfile)
#             print(f"the roll number: {data['Roll no.']}")
#             print(f"the student name: {data['Name']}")
#             print(f"the marks: {data['Mark']}")
#             print("___________________________")
#     except Exception:
#         pass

# import csv
# from prettytable import PrettyTable
#
# # with open("csvfile.csv", 'w') as csvfile:
# #     write = csv.writer(csvfile)
# #     write.writerow(["Roll No.", "Name", "Marks"])
# #     while True:
# #         line = []
# #         roll = int(input("Enter a line: "))
# #         name = input("Enter a name: ").title()
# #         marks = float(input("Enter a marks: "))
# #         line.append(roll)
# #         line.append(name)
# #         line.append(marks)
# #         write.writerow(line)
# #         if input("Quit(*)") == "*":
# #             break
# #         else:
# #             continue
#
#
# with open("csvfile.csv", 'r') as csvfile:
#     Reader = csv.reader(csvfile)
#     header = next(Reader)
#     table = PrettyTable(header)
#     for i in Reader:
#         if len(i) > 0:
#             table.add_row(i)
#         else:
#             pass
#     print(table)


# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list2 = list1
# list2.append(10)
# print(list1)

# def Changeval(M,N):
#     for i in range(N):
#         if M[i] % 5 ==0:
#             M[i]//=5
#         elif M[i] %3 ==0:
#             M[i]//=3
# L = [25,8,75,12]
# if __name__ == "__main__":
#     Changeval(L,4)
# for i in L:
#     print(i, end='#')

# STACK

# def push(stack):
#     if len(stack)+1 > 5:
#         print("Stack overflow!")
#     else:
#         element = input("Push an element: ")
#         stack.insert(0, element)
#         print("Element has been pushed!")
#
#
# def pop(stack):
#     if len(stack) == 0:
#         print("Stack underflow!")
#     else:
#         stack.pop(0)
#         print()
#
# def peek(stack):
#     if len(stack) == 0:
#         print("Stack is Empty!")
#     else:
#         print(f"The Peek Element: {stack[0]}")
#
#
# def display(stack):
#     if len(stack) == 0:
#         print("Stack is Empty!")
#     else:
#         print(stack)
#
#
# def isempty(stack):
#     if len(stack) == 0:
#         print("Stack is Empty!")
#     else:
#         print("Stack is not empty!")
#
#
# def isfull(stack):
#     if len(stack) != 0:
#         print("Stack is Full!")
#     else:
#         print("Stack is not full!")
#
# stack = []
# def main():
#     choice = input("Enter")
#     if choice == "1":
#         push(stack)
#         main()
#     elif choice == "2":
#         pop(stack)
#         main()
#     elif choice == "3":
#         peek(stack)
#         main()
#     elif choice == "4":
#         display(stack)
#         main()
#     elif choice == "5":
#         isempty(stack)
#         main()
#     elif choice == "6":
#         isfull(stack)
#         main()
# if __name__ == "__main__":
#     main()


# with open("TextFile.txt", 'r') as file:
#     I = []
#     E = []
#     Read = file.read()
#     for i in Read:
#         if i.lower() == 'e':
#            E.append(i)
#         elif i.lower() == 'i':
#             I.append(i)
#     print(f"The number of I or i : {len(I)}")
#     print(f"The number of E or e : {len(E)}")

g = ('hello'[4:1:-1])
print(g)