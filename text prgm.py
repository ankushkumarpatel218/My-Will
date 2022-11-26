Write = []
Write1 = []
with open("text file.txt",'r') as file:
    Read = file.readlines()
    for i in Read:
        if 'a' in i:
            Write.append(i)
        elif 'a' not in i:
            Write1.append(i)
    with open('text file.txt','w') as file1:
        file1.writelines(Write1)
    with open('text file1.txt','w') as File:
        File.writelines(Write)
    print("Data has been transferred to another file!")
