import prettytable
import csv
import pandas

Gender = []
number_of_emp = []
with open("Employ.csv", 'r') as Emp:
    Read = csv.DictReader(Emp)
    for i in Read:
        gender = i["Gender"].upper()
        Gender.append(gender)
for i in Gender:
    Count = Gender.count(i)
    number_of_emp.append(Count)

    if Count > 1:
        for j in range(Count-1):
            Gender.remove(i)

data = {Gender[0]: number_of_emp[0], Gender[1]: number_of_emp[1]}

new_dict = {k: [v] for k, v in data.items()}

df = pandas.DataFrame(new_dict)
df1 = df.T
df1.rename(columns={0: "number of Employs"}, inplace=True)

df1.to_csv("count emp AC To Gender.csv")
df2 = pandas.read_csv("count emp AC To Gender.csv")
df2.sort_values("number of Employs")
df2.rename(columns={"Unnamed: 0": "Gender"}, inplace=True)
df2.to_csv("count emp.csv", index=False)

with open("count emp.csv", 'r') as csvfile:
    read = csv.reader(csvfile)
    header = next(read)
    table = prettytable.PrettyTable(header)
    for i in read:
        table.add_row(i)
    print(table)
