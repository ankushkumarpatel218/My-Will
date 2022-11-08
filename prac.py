import pickle

with open("practice.txt", 'rb') as file:
    try:
        rollno = int(input("enter roll number: "))
        file.seek(0)
        read = pickle.load(file)
        if read['Roll no.'] == rollno:
            print(read)

    except EOFError:
        pass
    print("""""")