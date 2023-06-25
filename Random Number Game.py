import random

print("Welcome to the Number-guessing Game!")
choice = input("Please select your difficulty: \n[E] Easy(1-digits) \n[M] Medium(2/3-digits) \n[H] Hard(4-digits) \n[I] Impossible(Up to 6-digits)")

def easy():
    numbers  = random.randint(0, 9)
    guessednumber = int(input("Guess the number: "))

    if guessednumber < numbers:
        print(f"Sorry, your guess is too low. \nThe correct number is {numbers} \nDo you want to try again?")
    elif guessednumber == numbers:
        print(f"Congratulations! You guessed the number correctly! \nYour guess is {numbers}")
    else:
        print(f"Sorry, your guess is too high. \nThe correct number is {numbers} \nDo you want to try again?")

def medium():
    numbers1  = random.randint(0, 999)
    guessednumber1 = int(input("Guess the number: "))

    if guessednumber1 < numbers1:
        print(f"Sorry, your guess is too low. \nThe correct number is {numbers1} \nDo you want to try again?")
    elif guessednumber1 == numbers1:
        print(f"Congratulations! You guessed the number correctly! \nYour guess is {numbers1}")
    else:
        print(f"Sorry, your guess is too high. \nThe correct number is {numbers1} \nDo you want to try again?")

def hard():
    numbers2  = random.randint(0, 9999)
    guessednumber2 = int(input("Guess the number: "))

    if guessednumber2 < numbers2:
        print(f"Sorry, your guess is too low. \nThe correct number is {numbers2} \nDo you want to try again?")
    elif guessednumber2 == numbers2:
        print(f"Congratulations! You guessed the number correctly! \nYour guess is {numbers2}")
    else:
        print(f"Sorry, your guess is too high. \nThe correct number is {numbers2} \nDo you want to try again?")

def impossible():
    numbers3  = random.randint(0, 999999)
    guessednumber3 = int(input("Guess the number: "))

    if guessednumber3 < numbers3:
        print(f"Sorry, your guess is too low. \nThe correct number is {numbers3} \nDo you want to try again?")
    elif guessednumber3 == numbers3:
        print(f"Congratulations! You guessed the number correctly! \nYour guess is {numbers3}")
    else:
        print(f"Sorry, your guess is too high. \nThe correct number is {numbers3} \nDo you want to try again?")

if choice == "e":
    easy()
elif choice == "m":
    medium()
elif choice == "h":
    hard()
elif choice == "i":
    impossible()
