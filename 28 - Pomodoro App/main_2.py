import tkinter as tk


class Pomodoro:
    PINK = "#e2979c"
    RED = "#e7305b"
    GREEN = "#9bdeac"
    YELLOW = "#f7f5dd"
    FONT = ("Arial", 30, "bold")
    CHECK_SYMBOL = "✓"
    WORK_MIN = 25
    SHORT_BREAK_MIN = 5
    LONG_BREAK_MIN = 20

    def __init__(self) -> None:
        self.set_window()
        self.set_canvas()
        self.set_timer_label()
        self.set_start_button()
        self.set_reset_button()
        self.set_check_mark()
        self.window.mainloop()

    def set_reset_button(self):
        self.reset_button = tk.Button(
            text="Reset", bg=self.YELLOW, foreground=self.GREEN, font=self.FONT
        )
        self.reset_button.config(
            activebackground=self.YELLOW, activeforeground="white", borderwidth=0
        )
        self.reset_button.grid(column=2, row=3)

    def set_window(self):
        self.window = tk.Tk()
        self.window.title("Pomodoro App")
        self.window.config(bg=self.YELLOW, padx=100, pady=50)

    def set_canvas(self):
        self.canvas = tk.Canvas(
            width=200, height=224, bg=self.YELLOW, highlightthickness=0
        )
        self.tomato_img = tk.PhotoImage(file="tomato.png")
        self.canvas.create_image(102, 114, image=self.tomato_img)
        self.canvas.create_text(
            103, 130, text="00:00", fill="white", font=self.FONT, tag="timer"
        )
        self.canvas.grid(column=1, row=1)

    def set_start_button(self):
        self.start_button = tk.Button(
            text="Start", bg=self.YELLOW, foreground=self.GREEN, font=self.FONT
        )
        self.start_button.config(
            activebackground=self.YELLOW, activeforeground="white", borderwidth=0
        )
        self.start_button.grid(column=0, row=3)

    def set_timer_label(self):
        self.timer_label = tk.Label(
            text="Timer", bg=self.YELLOW, foreground=self.GREEN, font=self.FONT
        )
        self.timer_label.grid(column=1, row=0)

    def set_check_mark(self):
        self.check_mark = tk.Label(
            text="checkmark",
            bg=self.YELLOW,
            foreground=self.GREEN,
            font=self.FONT,
        )
        self.check_mark.grid(column=1, row=3)

    def print_asdasd(self):
        print("lol")


pomodoro = Pomodoro()
