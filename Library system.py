import csv
import pandas
from prettytable import PrettyTable

Book_name = []
issue = []
with open("Library1.csv",'r') as csv1:
    read = csv.DictReader(csv1)
    for i in read:
        Name=i["Book name"].title()
        Book_name.append(Name)
        Issue = i["number of issues"]
        issue.append(Issue)

for I in range(len(issue)):
    issue[I] = int(issue[I])

Data = {}

if len(Book_name) == len(issue):
    for i in range(len(Book_name)):
        if Book_name[i] not in Data:
            Data[Book_name[i]] = 0

        Data[Book_name[i]] += issue[i]

    new_dict = {k: [v] for k, v in Data.items()}

    df = pandas.DataFrame(new_dict)

    new_df = df.T

    new_df.rename(columns={0:"Total number of issues"},inplace=True)


    new_df.to_csv("Library2.csv")


    new_df1 = pandas.read_csv("Library2.csv")
    new_df2 = new_df1.sort_values(['Total number of issues'], ascending=False)
    new_df2.rename(columns={"Unnamed: 0": "Book Name"}, inplace=True)
    new_df2.to_csv("Library3.csv",index=False)
else:
    print("Data is incomplete, Please Check Your Csv file")

with open("Library3.csv", 'r') as csvfile:
    read = csv.reader(csvfile)

    header = next(read)
    table = PrettyTable(header)
    for i in read:
        table.add_row(i)
    print(table)
