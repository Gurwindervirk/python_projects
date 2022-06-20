answer = input("Would you like to play? ").lower()

if answer == "yes":
    print("Okay lets play")
else:
    quit()

answer = input("What CPU stands for? ").lower()
value = 0
if answer =="central processing unit":
    print("Correct")
    value += 1
else:
    print("Incorrect!")

answer = input("What RAM stands for? " ).lower()
if answer == "random access memory":
    print("Correct")
    value += 1
else:
    print("Incorrect!")

answer = input("What PSU stands for? ").lower()

if answer == "power supply unit":
    print("Corect")
    value+=1
else:
    print("Incorrect")
answer = input("What GPU stands for? ").lower()

if answer == "graphics processing unit":
    print("Correct")
    value += 1
else:
    print("Incorrect!")

print(f" You have scored {value/4*100} %")