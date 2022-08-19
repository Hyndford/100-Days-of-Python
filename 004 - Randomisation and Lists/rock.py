import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# print(choices[player])

# computer = random.randint(0, 2)
# print("Computer chose:")
# print(choices[computer])

# if player == 0:
#     if computer == 0:
#         print("Draw")
#     elif computer == 1:
#         print("Lose")
#     else:
#         print("Win")
# elif player == 1:
#     if computer == 0:
#         print("Win.")
#     elif computer == 1:
#         print("Draw")
#     else:
#         print("Lose")
# else:
#     if computer == 0:
#         print("Lose")
#     elif computer == 1:
#         print("Win")
#     else:
#         print("Draw")

if player < 0 or player > 2: 
    print("You typed an invalid number, you lose!") 
else:
    print(choices[player])

    computer = random.randint(0, 2)
    print("Computer chose:")
    print(choices[computer])


    if player == 0 and computer == 2:
        print("You win!")
    elif computer == 0 and player == 2:
        print("You lose")
    elif computer > player:
        print("You lose")
    elif player > computer:
        print("You win!")
    elif computer == player:
        print("It's a draw")
        