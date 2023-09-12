import tkinter as tk


class QuizzlerInterface:
    # Constants
    THEME_COLOR: str = None

    # Variables
    window: tk.Tk = None
    score: int = None
    score_label: tk.Label = None
    my_canvas: tk.Canvas = None
    correct_button: tk.Button = None
    wrong_button: tk.Button = None

    def __init__(self) -> None:
        self.THEME_COLOR = "#375362"
        self.score = 0
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(bg=self.THEME_COLOR, padx=20, pady=20)
        self.ui_elements()
        self.window.mainloop()

    def ui_elements(self):
        # Labels
        self.score_label = tk.Label()
        label_text = f"Score: {self.score}"
        self.score_label.config(text=label_text, fg="white", bg=self.THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        # Canvas
        self.my_canvas = tk.Canvas()
        self.my_canvas.config(bg="white", width=300, height=250)
        self.my_canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

        # Buttons
        self.correct_button = tk.Button()
        self.CORRECT_BUTTON_IMAGE = tk.PhotoImage(file="images/true.png")
        self.correct_button.config(image=self.CORRECT_BUTTON_IMAGE)
        self.correct_button.config(bg=self.THEME_COLOR, bd=0)
        self.correct_button.config(activebackground=self.THEME_COLOR)
        self.correct_button.grid(column=0, row=2)

        self.wrong_button = tk.Button()
        self.WRONG_BUTTON_IMAGE = tk.PhotoImage(file="images/false.png")
        self.wrong_button.config(image=self.WRONG_BUTTON_IMAGE)
        self.wrong_button.config(bg=self.THEME_COLOR, bd=0)
        self.wrong_button.config(activebackground=self.THEME_COLOR)
        self.wrong_button.grid(column=1, row=2)
