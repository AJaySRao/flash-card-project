from tkinter import *


BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card Project")
window.config(padx=50, pady=50)

canvas = Canvas(width=800, height=526, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")
canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=1)

# card_back = PhotoImage(file="images/card_back.png")
# canvas.create_image(400, 263, image=card_back)
# canvas.pack()

button = Button(image=right, highlightthickness=0)
button.grid(row=1, column=0, ANCHOR=CENTER)

button = Button(image=wrong, highlightthickness=0)
button.grid(row=1, column=1,)

window.mainloop()