list1 = ["Riya", "Ankush", "Satyajeet", "Akhil", "Ayush","Ankush", "Satyajeet", "Ayush", "Akhil", "ayush", "riya", "akhil", "ankush", "ayush"]


num2 = input("enter the element what you want to count:- ").title()
Count = 0
for j in list1:
    if j.title() == num2:
        Count += 1

print(f"the number of {num2} are:- {Count}")