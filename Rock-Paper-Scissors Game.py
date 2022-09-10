import random
import pyttsx3

engine = pyttsx3.init("sapi5")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

game = ["Rock", "Paper", "Scissors"]
list2 = []
for i in range(3):
    ran = random.choice(game)
    print("1. Rock   2.Paper   3.scissors")
    ch = int(input("enter your choice:- "))
    if ch == 1:
        user = "Rock"
        if user == ran:
            print("\nYou: Rock\nComputer: Rock\n")
            print("Draw!\n")
            speak("Draw!")
            list2.append("Draw!")
        elif ran == "Scissors":
            print("\nYou: Rock\nComputer: Scissors\n")
            print("You Won!\n")
            speak("You Won!")
            list2.append("You Won!")
        elif ran == "Paper":
            print("\nYou: Rock\nComputer: Paper\n")
            print("You lose!\n")
            speak("You Lose!")
            list2.append("You lose!")

    elif ch == 2:
        user = "Paper"
        if user == ran:
            print("\nYou: Paper\nComputer: Paper\n")
            print("Draw!\n")
            speak("Draw!")
            list2.append("Draw!")
        elif ran == "Rock":
            print("\nYou: Paper\nComputer: Rock\n")
            print("You Won!\n")
            speak("You Won!")
            list2.append("You Won!")
        elif ran == "Scissors":
            print("\nYou: Paper\nComputer: Scissors\n")
            print("You lose!\n")
            speak("You Lose!")
            list2.append("You lose!")

    elif ch == 3:
        user = "Scissors"
        if user == ran:
            print("\nYou: Scissors\nComputer: Scissors\n")
            print("Draw!\n")
            speak("Draw!")
            list2.append("Draw!")
        elif ran == "Paper":
            print("\nYou: Scissors\nComputer: Paper\n")
            print("You Won!\n")
            speak("You Won!")
            list2.append("You Won!")
        elif ran == "Rock":
            print("\nYou: Scissors\nComputer: Rock\n")
            print("You lose!\n")
            speak("You Lose!")
            list2.append("You lose!")
if list2.count("You lose!") == 2:
    speak("you lost the match !")
    print("you lost the match !")
elif list2.count("You Won!") <= 2:
    speak("you Won the match !")
    print("you Won the match !")
elif list2.count("Draw!") == 1 and list2.count("You Won!") == 1 and list2.count("You lose!") == 1:
    speak("No one Wins!")
    print("No one Wins!")
elif list2.count("Draw!") == 3:
    speak("No one Wins!")
    print("No one Wins!")

elif list2.count("You lose!") == 3:
    speak("you lost the match !")
    print("you lost the match !")

