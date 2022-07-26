from tkinter import *
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
# **************************** Pick a Word ****************************
words_df = pd.read_csv("data/french_words.csv")
words_dict = words_df.to_dict(orient="records")


def get_word():
    word = choice(words_dict)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=word["French"])


# **************************** UI Setup ****************************
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=get_word)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
know_button = Button(image=check_image, highlightthickness=0, command=get_word)
know_button.grid(row=1, column=1)

get_word()

window.mainloop()
