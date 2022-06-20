import random

top_range = input("Enter a number: ")

if top_range.isdigit():
    top_range = int(top_range)
    if top_range <= 0:
        print("Please enter a larger number next time")
        quit()
else:
    print("Please enter a number next time")
    quit()
random_number = random.randint(0,top_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a Guess! ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter a number next time")
        continue
    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess < random_number:
        print("your guess is below the random number")
    else:
        print("your guess is above the random number.")

print("You made it in",guesses,"guesses")


