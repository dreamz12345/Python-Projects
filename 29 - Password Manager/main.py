import tkinter as tk
from tkinter import messagebox
import pandas
import os.path
import random
import list_of_letters as lol


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = lol.letters
    numbers = lol.numbers
    symbols = lol.symbols

    password = ""
    password_mixed = ""

    PASSWORD_LENGTH = 10
    AMOUNT_OF_NUMBERS = 4
    AMOUNT_OF_SYMBOLS = 3
    AMOUNT_OF_LETTERS = PASSWORD_LENGTH - (AMOUNT_OF_NUMBERS + AMOUNT_OF_SYMBOLS)

    for _ in range(0, AMOUNT_OF_LETTERS):
        random_number = random.randint(0, len(letters) - 1)
        password += letters[random_number]

    for _ in range(0, AMOUNT_OF_NUMBERS):
        random_number = random.randint(0, len(numbers) - 1)
        password += numbers[random_number]

    for _ in range(0, AMOUNT_OF_SYMBOLS):
        random_number = random.randint(0, len(symbols) - 1)
        password += symbols[random_number]

    for _ in range(0, PASSWORD_LENGTH):
        random_number = random.randint(0, len(password) - 1)
        password_mixed += password[random_number]
        password = password.replace(password[random_number], "", 1)

    password_entry.delete(0, "end")
    password_entry.insert(0, password_mixed)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def sort_passwords():
    df = pandas.read_csv("data.txt", sep=" ")
    df_sorted = df.sort_values(by="Website")
    df_sorted.to_csv("data.txt", index=False, sep=" ")


def clear_entries():
    website_entry.delete(0, "end")
    username_entry.delete(0, "end")
    password_entry.delete(0, "end")


def all_entries_filled(website, username, password):
    EMPTY = ""
    if website is not EMPTY:
        if username is not EMPTY:
            if password is not EMPTY:
                return True
    messagebox.showerror("Password Manager", "Please fill all entries!")
    return False


def should_save_data(website: str, username: str, password: str):
    question = (
        f"Website: {website}\n"
        f"Username: {username}\n"
        f"Password: {password}\n\n"
        f"Save this account?"
    )
    return messagebox.askyesno(title="Do you want to save?", message=question)


def save_data():
    website = website_entry.get().replace(" ", "")
    username = username_entry.get().replace(" ", "")
    password = password_entry.get().replace(" ", "")

    data = [
        {
            "Website": website,
            "Username": username,
            "Password": password,
        }
    ]
    df = pandas.DataFrame().from_dict(data)

    if all_entries_filled(website, username, password):
        if should_save_data(website, username, password):
            if not os.path.isfile("data.txt"):
                df.to_csv("data.txt", index=False, sep=" ")
                clear_entries()
                website_entry.focus()
            else:
                df.to_csv("data.txt", index=False, sep=" ", mode="a", header=False)
                sort_passwords()
                clear_entries()
                website_entry.focus()


def print_passwords():
    window_2 = tk.Toplevel(window)
    df = pandas.read_csv("data.txt", header=None, sep=" ")
    b = df.values.tolist()
    for index, row in enumerate(b):
        background_color = tk.Label(window_2, width=100, height=2, bg=BG_COLOR)
        background_color.grid(row=index, column=0, columnspan=3)
        for column in range(0, len(row)):
            str_var = tk.StringVar()
            str_var.set(row[column])
            text = tk.Entry(window_2, borderwidth=0, readonlybackground=BG_COLOR)
            if index == 0:
                text.config(font=("Arial", 15))
            text.config(textvariable=str_var, state="readonly", justify="center")
            text.grid(row=index, column=column, pady=10)


# ---------------------------- UI SETUP ------------------------------- #

RIGHT = "e"
LEFT = "w"
BG_COLOR = "white"

window = tk.Tk()
window.title("Password Manager")
window.config(padx=60, pady=60, bg=BG_COLOR)

canvas = tk.Canvas()
canvas.config(width=200, height=200, bg=BG_COLOR, highlightthickness=0)
canvas.grid(column=1, row=0)
logo = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)

website_label = tk.Label()
website_label.config(text="Website:", bg=BG_COLOR)
website_label.grid(column=0, row=1, sticky=RIGHT)

username_label = tk.Label()
username_label.config(text="Email/Username:", bg=BG_COLOR)
username_label.grid(column=0, row=2, sticky=RIGHT)

password_label = tk.Label()
password_label.config(text="Password:", bg=BG_COLOR)
password_label.grid(column=0, row=3, sticky=RIGHT)

website_entry = tk.Entry()
website_entry.config(width=51, bg=BG_COLOR)
website_entry.grid(column=1, row=1, columnspan=2, sticky=LEFT)
website_entry.focus()

username_entry = tk.Entry()
username_entry.config(width=51, bg=BG_COLOR)
username_entry.grid(column=1, row=2, columnspan=2, sticky=LEFT)

password_entry = tk.Entry()
password_entry.config(width=33, bg=BG_COLOR)
password_entry.grid(column=1, row=3, sticky=LEFT)

generate_password_button = tk.Button()
generate_password_button.config(text="Generate Password", command=generate_password)
generate_password_button.config(width=14, borderwidth=1, highlightbackground=BG_COLOR)
generate_password_button.grid(column=2, row=3, sticky=LEFT)

add_button = tk.Button()
add_button.config(text="Add", width=43, borderwidth=1, highlightbackground=BG_COLOR)
add_button.config(command=save_data)
add_button.grid(column=1, row=4, columnspan=2, sticky=LEFT)

print_passwords_button = tk.Button()
print_passwords_button.config(text="Stored Passwords", width=43, borderwidth=1)
print_passwords_button.config(command=print_passwords, highlightbackground=BG_COLOR)
print_passwords_button.grid(column=1, row=5, columnspan=2, sticky=LEFT)


window.mainloop()
