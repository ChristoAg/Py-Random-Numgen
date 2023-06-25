import random

num1 = int(input("Please select your first number:"))
num2 = int(input("Please select your second number:"))

numbers  = random.randint(num1, num2)
guessednumber = int(input("Guess the number: "))

if guessednumber < numbers:
    print(f"Sorry, your guess is too low. \nThe correct number is {numbers}")
elif guessednumber == numbers:
    print(f"Congratulations! You guessed the number correctly! \nYour guess is {numbers}")
elif guessednumber > numbers:
    print(f"Sorry, your guess is too high. \nThe correct number is {numbers}")
else:
    print(f"Sorry, the number is out of range. \nRange: {num1} to {num2}")