list1 = [(), ('ram','15','8'), (), ('laxman', 'sita'),('krishna', 'akbar', '45'), ('',''),()]
print(f"\nList before removing empty tuple:-{list1}\n")
Empty_Tup = list1.count(())
for i in range(Empty_Tup):
    list1.remove(())
print(f"List after removing empty tuple:-{list1}")
