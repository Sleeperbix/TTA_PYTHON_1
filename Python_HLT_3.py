#Random Number Guessing Game
import random

def main():
    #Generate random number
    theNumber = random.randint (1,100)
    #Set guess limit
    guesses = 6

    #print (theNumber)
    print ("Welcome to Guess the Number!\n")

    while guesses > 0:      

        print("You have", guesses, "attempt/s remaining.")
        guess = int(input("Enter your guess: "))

        if guess == theNumber:
            print("Well done! The number was ", theNumber, "\n")
            return 0
        else:
            if guess > theNumber:
                print(guess, "is higher!\n")
            if guess < theNumber:
                print(guess, "is lower!\n")
            guesses = guesses - 1

    print("Too bad! The number was ", theNumber)

main()