n = int(input("enter how many time you want to enter student data: "))
dict_list = []
for j in range(1, n+1):
    dict1 = {}
    roll = int(input("enter roll number: "))
    name = input("enter name of student: ")
    marks = float(input("enter student marks: "))
    dict1['Roll Number'] = roll
    dict1['Name'] = name
    dict1['Marks'] = marks
    dict_list.append(dict1)

for i in dict_list:
    if i["Marks"] >= 75:
        print(f"The students who have marks more than 75:\n{i}")
    else:
        pass
