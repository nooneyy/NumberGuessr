from random import randint
import time
print("Number Guessr - coded by nooney\n-------------------------------\nWarning! This program is only compatible with Python 3!\n")
format = 'format is x-y'
while True:
    try:
        stringrange = input('Please input your range ({}): '.format(format))
        list = (stringrange.split('-'))
        for i in range(0, len(list)): 
            list[i] = int(list[i])
        list.sort()
        break
    except Exception as e:
        print("\nYou have entered entered invalid numbers. FYI Guessing of negative numbers is not supported. Please try again. Tried exiting? Please force quit.\n")

print("\nYou have selected a range of " + stringrange + ".")
while True:
    try:
        stringtries = input("\nPlease specify the amount of tries: ")
        tries = int(stringtries)
        if tries > 0:
            break
        else:
            print("\nThe amount of tries must be larger than 0. Please try again.")
    except ValueError:
        print("\nThis is not a number. Please try again.")
print("\nStarting game...\n")
time.sleep(2)
print("Generating random number...\n")
time.sleep(1)
x = randint(list[0], list[1])
ended = "false"
while ended == "false" and tries > 0:
    try:    
        while tries > 0:
            guessedint = input("You have " + str(tries) + " tries left.\n\nGuess: ")
            if int(guessedint) == x:
                print("\nCongratulations! You have guessed the correct number, " + str(x) + ", with " + str(tries) + " tries left!")
                ended = "true"
                tries = 0
                break
            else:
                print("\nThat wasn't quite right.\n")
                tries = tries - 1
        else:
            print("You lost. You have 0 tries left.\n")
            print("The number was: " + str(x))
    except ValueError:
        print("\nThis is not a number. Please guess again.\n")