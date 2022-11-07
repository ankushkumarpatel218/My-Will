import pickle

# with open("practice.txt", 'wb') as file:
#     dict1 = {}
#     while True:
#         rollno = int(input("enter rollno. "))
#         name = input("enter name of the student:").title()
#         Marks = float(input("enter marks:"))
#         dict1["name"] = name
#         dict1["Roll no."] = rollno
#         dict1["Marks"] = Marks
#         pickle.dump(dict1, file)
#         print("\nData Entered Successfully!\n")
#         if input("quit?(*) ") == "*":
#             break
#         else:
#             continue
#
with open("practice.txt", 'rb') as file:
    try:
        file.seek(0)
        read = pickle.load(file)
        print(read)
    except EOFError:
        pass

with open("practice.txt", '+wb') as file:
    try:
        print(read)
        file.seek(0)
        rollno = int(input("enter roll number: "))
        marks = float(input('Enter the updated Marks: '))

        rec = {'Rollno': rollno, 'Name': read['name'], 'Marks': marks}
        pickle.dump(rec, file)
        file.seek(0)
        read = pickle.load(file)
        while read:
            print(read)

    except EOFError:
        pass