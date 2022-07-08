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

#Write your code below this line 👇

user_play = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
plays = [rock,paper,scissors]
user_play = plays[user_play]
comp_play = plays[random.randint(0, 2)]
match_result = ''

if user_play == rock and comp_play == rock:
  match_result = 'draw'
elif user_play == rock and comp_play == paper:
  match_result = 'comp win'
elif user_play == rock and comp_play == scissors:
  match_result = 'user win'
elif user_play == paper and comp_play == rock:
  match_result = 'user win'
elif user_play == paper and comp_play == paper:
  match_result = 'draw'
elif user_play == paper and comp_play == scissors:
  match_result = 'comp win'
elif user_play == scissors and comp_play == rock:
  match_result = 'comp win'
elif user_play == scissors and comp_play == paper:
  match_result = 'user win'
elif user_play == scissors and comp_play == scissors:
  match_result = 'draw'

print(user_play)
print(f"Computer chose:\n{comp_play}")
if match_result.startswith('d'):
  print('Draw')
elif match_result.startswith('u'):
  print('You win!')
else:
  print('You lose')