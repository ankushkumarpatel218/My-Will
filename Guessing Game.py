import random
import os

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

if os.path.isfile('score.txt') == False:
    with open('score.txt', 'w') as Score:
        Score.write(str(guesses))
else:
    pass
with open('score.txt', 'r') as Score:
      Read = Score.read()
      if int(Read) > guesses:
          print(f"you broke the highest score")
          with open('score.txt', 'w') as Score:
              Score.write(str(guesses))
      else:
          pass


