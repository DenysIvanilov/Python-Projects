import pandas as pd

nato = pd.read_csv("nato_phonetic_alphabet.csv")

letter_nato = {row.letter: row.code for index, row in nato.iterrows()}

word = input("Enter a word: ").upper()
output = [letter_nato[letter] for letter in word]
print(output)
