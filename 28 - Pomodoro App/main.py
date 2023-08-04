import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT = ("Arial", 30, "bold")
CHECK_SYMBOL = "✓"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
time_left = 0

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #


def timer():
    countdown()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(time=WORK_MIN, loop_count=0, start_over=False, checkmark_text=""):
    second = time % 60
    minute = time // 60
    text_2 = f"{minute:02d}:{second:02d}"

    if time > 0:
        canvas.delete("timer")
        canvas.create_text(103, 130, text=text_2, fill="white", font=FONT, tags="timer")
        window.after(1000, countdown, time - 1, loop_count, start_over, checkmark_text)
    else:
        if loop_count == 6:
            start_over = True
            loop_count = 0
            checkmark_text += CHECK_SYMBOL
            checkmark.config(text=checkmark_text)
            time = LONG_BREAK_MIN
            timer_label.config(text="Long Break")
        elif loop_count % 2 == 0 and start_over is False:
            loop_count += 1
            checkmark_text += CHECK_SYMBOL
            checkmark.config(text=checkmark_text)
            timer_label.config(text="Short Break")
            time = SHORT_BREAK_MIN
        elif start_over is True:
            start_over = False
            checkmark_text = ""
            checkmark.config(text=checkmark_text)
            timer_label.config(text="Work")
            time = WORK_MIN
        elif loop_count % 2 == 1:
            start_over = False
            loop_count += 1
            timer_label.config(text="Work")
            time = WORK_MIN

        canvas.delete("timer")
        canvas.create_text(103, 130, text=text_2, fill="white", font=FONT, tags="timer")
        window.after(1000, countdown, time, loop_count, start_over, checkmark_text)


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodoro App")
window.config(bg=YELLOW, padx=100, pady=50)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(102, 114, image=tomato_img)
canvas.create_text(103, 130, text="00:00", fill="white", font=FONT, tag="timer")
canvas.grid(column=1, row=1)

timer_label = tk.Label(text="Timer", bg=YELLOW, foreground=GREEN, font=FONT)
timer_label.grid(column=1, row=0)

start_button = tk.Button(text="Start", bg=YELLOW, foreground=GREEN, font=FONT)
start_button.config(activebackground=YELLOW, activeforeground="white", borderwidth=0)
start_button.config(command=timer)
start_button.grid(column=0, row=3)

checkmark = tk.Label(text="", bg=YELLOW, foreground=GREEN, font=FONT)
checkmark.grid(column=1, row=3)

reset_button = tk.Button(text="Reset", bg=YELLOW, foreground=GREEN, font=FONT)
reset_button.config(activebackground=YELLOW, activeforeground="white", borderwidth=0)
reset_button.grid(column=2, row=3)


window.mainloop()
