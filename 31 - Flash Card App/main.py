import tkinter as tk
import pandas
import random


def is_not_empty(iterable_object):
    return len(iterable_object) > 0


def user_right():
    if is_not_empty(words_list):
        words_list.remove(current_word)
        if is_not_empty(words_list):
            next_word()
    else:
        canvas.after_cancel(timer)
        canvas.itemconfig(word, text="Well Done!")


def user_wrong():
    if is_not_empty(words_list):
        next_word()


def next_word():
    global current_word
    global timer
    canvas.after_cancel(timer)
    current_word = random.choice(words_list)
    canvas.itemconfig(image_widged, image=FRONT_IMAGE)
    canvas.itemconfig(language, text="French")
    canvas.itemconfig(word, text=current_word["French"])
    timer = canvas.after(3000, show_answer)


def show_answer():
    canvas.itemconfig(image_widged, image=BACK_IMAGE)
    canvas.itemconfig(language, text="English")
    canvas.itemconfig(word, text=current_word["English"])


BG_COLOR = "#B1DDC6"

words_list = pandas.read_csv("data/french_words.csv").to_dict(orient="records")
current_word = random.choice(words_list)

window = tk.Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BG_COLOR)

FRONT_IMAGE = tk.PhotoImage(master=window, file="images/card_front.png")
BACK_IMAGE = tk.PhotoImage(master=window, file="images/card_back.png")

canvas = tk.Canvas(width=800, height=526)
canvas.config(bg=BG_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)
image_widged = canvas.create_image(400, 263, image=FRONT_IMAGE)
LANGUAGE_FONT = ("Ariel", 30, "italic")
language = canvas.create_text(400, 100, text="French", font=LANGUAGE_FONT)
WORD_FONT = ("Ariel", 60, "bold")
word = canvas.create_text(400, 253, text=current_word["French"], font=WORD_FONT)
timer = canvas.after(3000, show_answer)

correct_button = tk.Button()
CORRECT_BUTTON_IMAGE = tk.PhotoImage(file="images/right.png")
correct_button.config(image=CORRECT_BUTTON_IMAGE, bd=0, command=user_right)
correct_button.config(bg=BG_COLOR, activebackground=BG_COLOR)
correct_button.grid(column=0, row=1)

wrong_button = tk.Button()
WRONG_BUTTON_IMAGE = tk.PhotoImage(file="images/wrong.png")
wrong_button.config(image=WRONG_BUTTON_IMAGE, bd=0, command=user_wrong)
wrong_button.config(bg=BG_COLOR, activebackground=BG_COLOR)
wrong_button.grid(column=1, row=1)


window.mainloop()
