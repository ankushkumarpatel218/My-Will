with open("practice.txt", 'r') as file:
    words = [i for i in file.read().split()]
    len_word = [len(j) for j in words]
    max_len_word = max(len_word)
    for k in words:
        if len(k) == max_len_word:
            print(f"the longest word in the file: {k} having {max_len_word} letters") 
            