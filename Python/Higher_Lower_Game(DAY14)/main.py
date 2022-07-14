import random
from art import logo, vs
from game_data import data

print(logo)
end_game = False
A = data[random.randint(0, len(data) - 1)]
B = data[random.randint(0, len(data) - 1)]
score = 0
while not end_game:
    A_followers = A["follower_count"] * 1000000
    B_followers = B["follower_count"] * 1000000
    A_has_more = A_followers > B_followers
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
    print(f"{vs}\n")
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}\n")
    guess = input("Who has more followers? Type 'A' or 'B': ").capitalize()
    if (guess == 'A' and A_has_more == True) or (guess == 'B' and A_has_more != True):
        score += 1
        print(f"\nYou're right! Current score: {score}.\n")
        if guess == 'A':
            A = A
            B = data[random.randint(0, len(data) - 1)]
        elif guess == 'B':
            A = B
            B = data[random.randint(0, len(data) - 1)]
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        end_game = True
