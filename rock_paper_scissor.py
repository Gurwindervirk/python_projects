import random
user_wins = 0
computer_wins = 0

options = ["rock", "paper","scissor"]

while True:
    user_input = input(" Enter Rock/Paper/Scissor or Q to quit. ").lower()

    if user_input == "q":
        break
    if user_input not in options:
        continue
    computer_picked = random.randint(0,2)
    computer_picked = options[computer_picked]

    print("Computer picked",computer_picked)

    if user_input == "rock" and computer_picked == "scissor":
        print("You won!")
        user_wins += 1
    elif user_input == "scissor" and computer_picked =="paper":
        print("You won!")
        user_wins += 1
    elif user_input == "paper" and computer_picked == "rock":
        print("You won!")
        user_wins += 1
    elif user_input == computer_picked:
        print("draw")
    else :
        print("Computer won!")
        computer_wins += 1

print("You won",user_wins,"times.")
print("Computer won", computer_wins,"times.")
print("GoodBye!")