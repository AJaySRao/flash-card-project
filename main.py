import random
from tkinter import *
import pandas
from tkinter import messagebox
import os

BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
f2e = {}
#-------------------------------------------------Exception Handling----------------------------------------------------
try:
    data_file = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    old_data = pandas.read_csv("data/french_words.csv")
    f2e = old_data.to_dict(orient='records')
else:
    f2e = data_file.to_dict(orient='records')

#-------------------------------------------------functions-------------------------------------------------------------
def next_card():
    global current_card, flip_time, f2e
    window.after_cancel(flip_time)
    try:
        current_card = random.choice(f2e)
        canvas.itemconfig(title, text='French', fill='black')
        canvas.itemconfig(word, text=current_card['French'], fill='black')
        canvas.itemconfig(card, image=card_front)
        #print(current_card['French'])
        flip_time = window.after(2000, flip)
        #print(current_card['English'])
    except IndexError:
        messagebox.showinfo(title="Congratulation", message=" You've learned all the words!")
        file = 'data/words_to_learn.csv'
        if(os.path.exists(file) and os.path.isfile(file)):
            os.remove(file)



def flip():
    canvas.itemconfig(card, image=card_back)
    canvas.itemconfig(title, text='English', fill='white')
    canvas.itemconfig(word, text=current_card['English'], fill='white')


def is_known():
    f2e.remove(current_card)
    #print(current_card)
    #print(len(f2e))
    data = pandas.DataFrame(f2e)
    data.to_csv('data/words_to_learn.csv', index=False)
    next_card()

#------------------------------------------------------UI Setup---------------------------------------------------------
window = Tk()
window.title("Flash Card Project")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_time = window.after(2000, func=flip)
#images------------------------------------------------------------------
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")

#canvas------------------------------------------------------------------
canvas = Canvas(width=800, height=526)

#Image position on canvas------------------------------------------------
card = canvas.create_image(400, 263, image='')
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2, sticky='EW')

#text on canvas----------------------------------------------------------
title = canvas.create_text(400, 140, text="", font=("Ariel", 40, 'italic'))
word = canvas.create_text(400, 263, text="", font=("Ariel", 65, 'bold'))

#buttons-----------------------------------------------------------------
right_button = Button(image=right, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=0)

cross_button = Button(image=wrong, highlightthickness=0, command=next_card)
cross_button.grid(row=1, column=1)

next_card()

window.mainloop()
