str1 = input("enter a string: ")

vowels = []
consonants = []
uppercase = []
lowercase = []

for i in str1:
    if i.lower() in ['a', 'e', 'i', 'o', 'u']:
        vowels.append(i)

    elif i.lower() not in ['a', 'e', 'i', 'o', 'u']:
        consonants.append(i)

    else:
        print("its special character! ")

for s in str1:
    if s.isupper():
        uppercase.append(i)

    elif s.islower():
        lowercase.append(i)

print(f"""
The number of vowels: {len(vowels)}
The number of consonants: {len(consonants)}
The number of uppercase: {len(uppercase)}
The number of lowercase: {len(lowercase)}
""")