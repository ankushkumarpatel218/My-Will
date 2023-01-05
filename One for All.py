import csv
# with open("Mycsvfile.csv", "w") as csvfile:
#     write = csv.writer(csvfile)
    # write.writerow(["Roll no.","Name","Marks"])
#     user = int(input("Enter number of student: "))
#     for i in range(user):
#         name = input("Enter Student name: ").title().strip()
#         Roll_no = int(input("Enter Roll number: "))
#         Marks = float(input("Enter the marks of the student: "))
#         Data = [name, Roll_no, Marks]
#         Stu_Data = []
#         Stu_Data.append(Data)
#         write.writerows(Stu_Data)
# print("\nDone!")

from prettytable import PrettyTable

with open("Mycsvfile.csv", "r") as csvfile:
    Read = csv.reader(csvfile)
    Header = next(Read)
    Table = PrettyTable(Header)
    for data in Read:
        print(data)
        
    

        