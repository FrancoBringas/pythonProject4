#import random
#participantes = input("quien va a participar?")
#names = participantes.split(", ")
#leng = len(names)
#print("el que pagara la cuenta es;"+names[random.randint(0,leng-1)])
# 🚨 Don't change the code below 👇
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

#Write your code below this line 👇
import random
objets = [rock, paper, scissors]
player = objets[int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))]
print(player)
print("Computer chose")
computer = random.choice(objets)
print(computer)
if player == rock and computer == paper or computer == scissors:
    print("You win")
elif player == paper and computer == rock:
    print("You win")
elif player == scissors and computer == paper:
    print("You win")
elif player == computer:
    print("tie")
else:
    print("You lose")