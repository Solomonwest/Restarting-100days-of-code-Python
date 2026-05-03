import random

# Task 6 Rock Paper Scissors

human_choice = int(input("What do you choose? type 0 for rock, 1 for paper, or 2 for scissors: "))

computer_choice = random.randint(0,2)



if human_choice == 0:
    print("You chose Rock")
elif human_choice == 1:
    print("You chose paper")
elif human_choice == 2:
    print("You choose scissors")
else:
    print("Invalid Input")


if computer_choice == 0:
    print("computer chose Rock")
elif computer_choice == 1:
    print("computer chose paper")
elif computer_choice == 2:
    print("computer choose scissors")
else:
    print("Invalid Input")


if human_choice == 0 and computer_choice == 0:
    print("It's a Draw")
if human_choice == 0 and computer_choice == 1:
    print("You lose")
if human_choice == 0 and computer_choice == 2:
    print("You win")
if human_choice == 1 and computer_choice == 0:
    print("You win")
if human_choice == 1 and computer_choice == 1:
    print("It's a Draw")
if human_choice == 1 and computer_choice == 2:
    print("You lose")
if human_choice == 2 and computer_choice == 0:
    print("You lose")
if human_choice == 2 and computer_choice == 1:
    print("You win")
if human_choice == 2 and computer_choice == 2:
    print("It's a Draw")

