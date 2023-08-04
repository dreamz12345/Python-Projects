import tkinter as tk


def kmh_to_mph(kmh: float) -> float:
    mph = round((kmh * 0.621371), 2)
    return mph


def mph_to_kmh(mph: float) -> float:
    kmh = round((mph * 1.609344), 2)
    return kmh


def user_input_correct(user_input: str) -> bool:
    try:
        float(user_input)
        return True
    except ValueError:
        return False


def mode() -> bool:
    if c_way.get() == K:
        return "km/h to mph"
    else:
        return "mph to km/h"


def change_mode():
    if mode() == "km/h to mph":
        label_top.config(text=K)
        label_bot.config(text=M)
        user_entry.delete(first=0, last="end")
        result.config(text=STARTING_CALC_VALUE)
    elif mode() == "mph to km/h":
        label_top.config(text=M)
        label_bot.config(text=K)
        user_entry.delete(first=0, last="end")
        result.config(text=STARTING_CALC_VALUE)


def calculate():
    user_input = user_entry.get()
    if user_input_correct(user_input):
        value = float(user_input)
        if mode() == "km/h to mph":
            mph = kmh_to_mph(value)
            result.config(text=mph)
        elif mode() == "mph to km/h":
            kmh = mph_to_kmh(value)
            result.config(text=kmh)
    else:
        result.config(text="Wrong input!")


font: tuple = ("Arial", 20, "normal")
STARTING_CALC_VALUE: int = 0
LEFT: str = "e"
K: str = "km/h"
M: str = "mph"

window = tk.Tk()
window.title(f"Conversion: {K} -> {M} || {M} -> {K}")
window.config(width=500, height=500)
window.config(padx=50, pady=50)

c_way = tk.StringVar(window, value=K)

k_to_m_button = tk.Radiobutton(font=font, text=f"{K} -> {M}")
k_to_m_button.config(variable=c_way, value=K, command=change_mode)
k_to_m_button.grid(column=1, row=0)

m_to_k_button = tk.Radiobutton(font=font, text=f"{M} -> {K}")
m_to_k_button.config(variable=c_way, value=M, command=change_mode)
m_to_k_button.grid(column=1, row=1)

user_entry = tk.Entry(font=font)
user_entry.config(justify="right")
user_entry.grid(column=1, row=2)

equal_sign = tk.Label(font=font)
equal_sign.config(text="=")
equal_sign.grid(column=0, row=3)

result = tk.Label(font=font)
result.config(text=STARTING_CALC_VALUE)
result.grid(column=1, row=3, sticky=LEFT)

label_top = tk.Label(text=K, font=font)
label_top.grid(column=2, row=2)

label_bot = tk.Label(text=M, font=font)
label_bot.grid(column=2, row=3)

button = tk.Button(font=font)
button.config(text="Calculate", command=calculate)
button.grid(column=1, row=4)

window.mainloop()
