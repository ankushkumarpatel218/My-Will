# Write a python program to create a CSV file “Student.rec” with following students records:
# RollNo	Name	Marks
import csv

with open("csvfile.csv",'w') as csvfile:
    header = ['Roll no.', 'Name', 'Mark']
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()
    data = {}
    while True:
        Roll = input("enter roll no. ")
        name = input("Enter name: ")
        Mark = input("Enter Marks: ")
        data['Roll no.'] = Roll
        data['Name'] = name
        data['Mark'] = Mark
        writer.writerow(data)
        if input("Quit? [ * ] ") == '*':
            break
        else:
            continue

