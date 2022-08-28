import csv

from prettytable import PrettyTable

csvfile = open("Anime1.csv", 'r', newline='')
read = csv.reader(csvfile)

header = next(read)
table = PrettyTable(header)
for i in read:
    table.add_row(i)
print(table)