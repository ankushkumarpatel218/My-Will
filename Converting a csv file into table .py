from prettytable import PrettyTable
import csv

with open("Lib.csv","r") as csv2:

    read1 = csv.reader(csv2)
    header1 = next(read1)
    table1 = PrettyTable(header1)
    for i in read1:
        table1.add_row(i)
    print(table1)