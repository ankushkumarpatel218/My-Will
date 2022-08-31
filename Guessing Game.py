import random

rand_num = random.randint(1, 100)
guesses = 0
while True:
    user = int(input("user number:"))
    if user != rand_num:
        if user > rand_num:
            print("your are close, enter a smaller number\n")
            guesses += 1
        elif user < rand_num:
            print("your are close, enter a larger number\n")
            guesses += 1
        continue
    else:
        print(f"Correct! You guessed it right in {guesses} guesses\n")
        break
