import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"

data_file = "data/french_words.csv"
french_word = pandas.read_csv(data_file)

f2e = french_word.to_dict(orient='records')

current_card = 0


def next_card():
    global current_card
    current_card = random.choice(f2e)
    canvas.itemconfig(title, text='French')
    canvas.itemconfig(word, text=current_card['French'])
    print(current_card['French'])
    f = window.after(3000, flip)
    print(current_card['English'])


def flip():
    global current_card
    canvas.itemconfig(card, image=card_back)
    canvas.itemconfig(title, text='English', fill='white')
    canvas.itemconfig(word, text=current_card['English'], fill='white')

#---------------------------------------------------UI Setup------------------------------------------------------
window = Tk()
window.title("Flash Card Project")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#images------------------------------------------------------------------
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")

#canvas------------------------------------------------------------------
canvas = Canvas(width=800, height=526)

#Image position on canvas------------------------------------------------
card = canvas.create_image(400, 263, image=card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2, sticky='EW')

#text on canvas----------------------------------------------------------
title = canvas.create_text(400, 140, text="French", font=("Ariel", 40, 'italic'))
word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, 'bold'))

#buttons
button1 = Button(image=right, highlightthickness=0, command=next_card)
button1.grid(row=1, column=0)

button2 = Button(image=wrong, highlightthickness=0, command=next_card)
button2.grid(row=1, column=1)

next_card()

window.mainloop()
