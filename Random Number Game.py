import random

def game():
    print("Welcome to the Number-guessing Game!")
    choice = input("Please select your difficulty: \n[E] Easy(1-digits) \n[M] Medium(2/3-digits) \n[H] Hard(4-digits) \n[I] Impossible(Up to 6-digits) \nYour option:")
    
    def easy():
        numbers  = random.randint(0, 9)
        guessednumber = int(input("Guess the number: "))

        def lowinput():
            prompt = input(f"Sorry, your guess is too low. \nThe correct number is {numbers} \nDo you want to try again? \n[Y] Yes       [N] No \nYour option:")

            if prompt == "y":
                game()
            else:
                print("Thank you for playing, have a nice day!")
        
        def correctinput():
            prompt1 = input(f"Congratulations! You guessed the number correctly! \nYour guess is {numbers} \nDo you want to try again? \n[Y] Yes       [N] No \nYour option:")

            if prompt1 == "y":
                game()
            else:
                print("Thank you for playing, have a nice day!")

        def highinput():
            prompt2 = input(f"Sorry, your guess is too high. \nThe correct number is {numbers} \nDo you want to try again? \n[Y] Yes       [N] No \nYour option:")

            if prompt2 == "y":
                game()
            else:
                print("Thank you for playing, have a nice day!")

        if guessednumber < numbers:
            lowinput()
        elif guessednumber == numbers:
            correctinput()
        else:
            highinput()


    def medium():
        numbers1  = random.randint(0, 999)
        guessednumber1 = int(input("Guess the number: "))
        
        def lowinput1():
            prompt3 = input(f"Sorry, your guess is too low. \nThe correct number is {numbers1} \nDo you want to try again? \n[Y] Yes       [N] No \nYour option:")

            if prompt3 == "y":
                game()
            else:
                print("Thank you for playing, have a nice day!")
        
        def correctinput1():
            prompt4 = input(f"Congratulations! You guessed the number correctly! \nYour guess is {numbers1} \nDo you want to try again? \n[Y] Yes       [N] No \nYour option:")

            if prompt4 == "y":
                game()
            else:
                print("Thank you for playing, have a nice day!")

        def highinput1():
            prompt5 = input(f"Sorry, your guess is too high. \nThe correct number is {numbers1} \nDo you want to try again? \n[Y] Yes       [N] No \nYour option:")

            if prompt5 == "y":
                game()
            else:
                print("Thank you for playing, have a nice day!")

        if guessednumber1 < numbers1:
            lowinput1()
        elif guessednumber1 == numbers1:
            correctinput1()
        else:
            highinput1()

    def hard():
        numbers2  = random.randint(0, 9999)
        guessednumber2 = int(input("Guess the number: "))
        
        def lowinput2():
            prompt6 = input(f"Sorry, your guess is too low. \nThe correct number is {numbers2} \nDo you want to try again? \n[Y] Yes       [N] No \nYour option:")

            if prompt6 == "y":
                game()
            else:
                print("Thank you for playing, have a nice day!")
        
        def correctinput2():
            prompt7 = input(f"Congratulations! You guessed the number correctly! \nYour guess is {numbers2} \nDo you want to try again? \n[Y] Yes       [N] No \nYour option:")

            if prompt7 == "y":
                game()
            else:
                print("Thank you for playing, have a nice day!")

        def highinput2():
            prompt8 = input(f"Sorry, your guess is too high. \nThe correct number is {numbers2} \nDo you want to try again? \n[Y] Yes       [N] No \nYour option:")

            if prompt8 == "y":
                game()
            else:
                print("Thank you for playing, have a nice day!")

        if guessednumber2 < numbers2:
            lowinput2()
        elif guessednumber2 == numbers2:
            correctinput2()
        else:
            highinput2()

    def impossible():
        numbers3  = random.randint(0, 999999)
        guessednumber3 = int(input("Guess the number: "))
        
        def lowinput3():
            prompt9 = input(f"Sorry, your guess is too low. \nThe correct number is {numbers3} \nDo you want to try again? \n[Y] Yes       [N] No \nYour option:")

            if prompt9 == "y":
                game()
            else:
                print("Thank you for playing, have a nice day!")
        
        def correctinput3():
            prompt0 = input(f"Congratulations! You guessed the number correctly! \nYour guess is {numbers3} \nDo you want to try again? \n[Y] Yes       [N] No \nYour option:")

            if prompt0 == "y":
                game()
            else:
                print("Thank you for playing, have a nice day!")

        def highinput3():
            promptx = input(f"Sorry, your guess is too high. \nThe correct number is {numbers3} \nDo you want to try again? \n[Y] Yes       [N] No \nYour option:")

            if promptx == "y":
                game()
            else:
                print("Thank you for playing, have a nice day!")

        if guessednumber3 < numbers3:
            lowinput3()
        elif guessednumber3 == numbers3:
            correctinput3()
        else:
            highinput3()

    if choice == "e":
        easy()
    elif choice == "m":
        medium()
    elif choice == "h":
        hard()
    elif choice == "i":
        impossible()
    else:
        print("It seems like you just chose a medium level, good luck with that!")
        medium()

game()
