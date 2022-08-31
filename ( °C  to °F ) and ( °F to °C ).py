def Fahrenheit(temp):
    far = (temp * 9/5) + 32
    return far

def Celsius(temp):
    cel =(temp * 5/9) - 32
    return cel
print("1. Celsius to farenheit\n2. Farenheit to Celsius\n")
while True:
    ch = input("enter your choice: ")
    if ch == "1":
        cel = float(input("enter temperature in Celsius:- "))
        print(f"\n{cel}°C = {Fahrenheit(cel)}°F")

    elif ch == "2":
        far = float(input("enter temperature in Fahrenheit:- "))
        print(f"\n{far}°F = {Celsius(far)}°C")
    CH = input("\nDo You want to Quit?( * )- ")
    if CH == '*':
        break
    else:
        continue

