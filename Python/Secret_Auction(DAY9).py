import os
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print('Welcome to the secret auction program.')


def bid(more_bets=True):
    while more_bets:
        name = input('What is your name? ')
        bid = input('What is your bid in USD? ')
        bids = {}
        bids[name] = bid
        ask = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
        if ask == 'yes':
            os.system('clear')  # OR SUITABLE COMMAND FOR CLEARING THE TERMINAL/OUTPUT WINDOW
        elif ask == 'no':
            more_bets = False
            biggest = list(bids.items())[0][1]
            winner_name = list(bids.items())[0][0]
            for k, v in bids.items():
                if v > biggest:
                    biggest = v
                    winner_name = k
            print(f"The winner is {winner_name} with a bid of {biggest}.")


bid()