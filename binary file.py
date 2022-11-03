import pickle

# with open("practice.txt", 'wb') as file:
#     dict1 = {}
#     while True:
#         name = input("enter name:")
#         rollno = input("enter rollno.")
#         Class = input("enter class")
#         dict1["name"] = name
#         dict1["Roll no."] = rollno
#         dict1["Class"] = Class
#         pickle.dump(dict1, file)
#         if input("quit?") == "*":
#             break
#         else:
#             continue
with open("practice.txt", 'rb') as file:
    try:
        while True:
                read = pickle.load(file)
                if read['Roll no.'] == '1' or read['Roll no.'] == '2':
                    print(f"name of the student: {read['name']}")
                    print(f"Roll no of the student: {read['Roll no.']}")
                    print(f"class of the student: {read['Class']}")
                    print("\n")
                else:
                    pass
    except EOFError:
        pass