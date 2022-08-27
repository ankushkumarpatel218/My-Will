import pandas as pd

from prettytable import PrettyTable
import csv

df = pd.read_csv('File.csv')
df.set_index("sno.", inplace=True)
list1 = []
while True:
    rng1 = int(input("enter starting range:-"))
    rng2 = int(input("enter end range"))
    for i in range(rng1,rng2+1):
        list1.append(i)
    df1 = df.loc[list1]
    df1.to_csv("lib.csv")
    with open("lib.csv", "r") as csv1:
        read = csv.reader(csv1)

        header = next(read)
        table = PrettyTable(header)
        for i in read:
            table.add_row(i)
        print(table)