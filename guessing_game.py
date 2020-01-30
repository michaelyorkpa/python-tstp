import random

number=random.randint(0,100)
guess = 0

while guess != "q":
    guess = input("Guess a number (or type q to quit):")
    if guess=="q":
        print("Thanks for playing")
        break
    try:
        guess=int(guess)
    except ValueError:
        print("Please enter a number or q to quit.")
        continue
    if guess==number:
        print("You guessed it!")
    else:
        print("Nope, that's wrong!")
