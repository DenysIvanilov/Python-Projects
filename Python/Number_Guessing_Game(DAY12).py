import random

logo = '''
  _   _   _    _   __  __   ____    ______   _____                    
 | \ | | | |  | | |  \/  | |  _ \  |  ____| |  __ \                   
 |  \| | | |  | | | \  / | | |_) | | |__    | |__) |                  
 | . ` | | |  | | | |\/| | |  _ <  |  __|   |  _  /                   
 | |\  | | |__| | | |  | | | |_) | | |____  | | \ \                   
 |_| \_|  \____/  |_|  |_| |____/  |______| |_|  \_\                  


   _____   _    _   ______    _____    _____   _____   _   _    _____ 
  / ____| | |  | | |  ____|  / ____|  / ____| |_   _| | \ | |  / ____|
 | |  __  | |  | | | |__    | (___   | (___     | |   |  \| | | |  __ 
 | | |_ | | |  | | |  __|    \___ \   \___ \    | |   | . ` | | | |_ |
 | |__| | | |__| | | |____   ____) |  ____) |  _| |_  | |\  | | |__| |
  \_____|  \____/  |______| |_____/  |_____/  |_____| |_| \_|  \_____|
'''


def play():
    print(logo)
    print('Welcome to the Number Guessing Game')
    print("I'm thinking about a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        guesses = 10
    else:
        guesses = 5
    number = random.randint(1, 100)
    while True:
        if guesses == 0:
            print("You lost. You have spent all your guesses and didn't get the number.\n")
            break
        print(f"You have {guesses} guesses remaining to guess a number")
        user_guess = int(input("Make a guess: "))
        if user_guess == number:
            print(f"You got it. The number was {number}!\n")
            break
        elif user_guess > number:
            print("Too high.\n")
        else:
            print("Too low.\n")
        guesses -= 1
    play_again = input("Do you want to play again? 'y' or 'n': ")
    if play_again == 'y':
        play()


play()
