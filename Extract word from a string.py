str1 = "Python program to interchange first and last elements in a list"
lst1 = str1.split()
lst2 = []
remove = input("enter the alphabet that you want o extract:- ")
for i in lst1:
    if i[0].lower() == remove or i[0].lower() == remove:
        lst2.append(i)

print(f"\nThe extracted words:-{lst2}")
print(f"\nOriginal string:- {str1}")
