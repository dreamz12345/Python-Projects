import tkinter as tk
import time
import json
import random


class TestTypingSpeed:

    def __init__(self) -> None:
        self.start_timer: time.time = None
        self.number_of_characters: int = 0
        self.list_of_characters: list = None
        self.user_typed_characters: list = None
        self.text_loaded_from_file: dict = None
        self.text_selected: str = None

    def count_time_difference(self):
        stop_timer = time.time()
        time_difference = stop_timer - self.start_timer
        return time_difference

    def import_text_from_file(self):
        with open("text.json", "r") as text:
            self.text_loaded_from_file = json.load(text)

    def select_random_text_from_texts(self):
        select_random_text = random.randint(
            1, len(self.text_loaded_from_file["TypingSpeedTexts"])
        )

        select_random_text = str(select_random_text)
        self.text_selected = self.text_loaded_from_file["TypingSpeedTexts"][
            select_random_text
        ]
        self.list_of_characters = list(self.text_selected)


def main():
    def print_user_entry(*args):
        print(var.get())
        label_bot.delete(1.0, tk.END)
        label_bot.insert(index=1.0, chars=var.get())

    def fill_var_from_entry(*args):
        new_test.user_typed_characters = list(label_bot.get(1.0, tk.END))
        new_test.user_typed_characters.pop(-1)

        for index, letter in enumerate(new_test.user_typed_characters):
            remove_exessive_tags = "1." + str(len(new_test.user_typed_characters))
            assign_tag = "1." + str(index)
            if letter == new_test.list_of_characters[index]:
                label_bot.tag_remove("wrong", assign_tag)
                label_bot.tag_add("right", assign_tag)
                label_top.tag_remove("wrong", assign_tag)
                label_top.tag_add("right", assign_tag)
            else:
                label_bot.tag_remove("right", assign_tag)
                label_bot.tag_add("wrong", assign_tag)
                label_top.tag_remove("right", assign_tag)
                label_top.tag_add("wrong", assign_tag)
            label_top.tag_remove("right", remove_exessive_tags, tk.END)
            label_top.tag_remove("wrong", remove_exessive_tags, tk.END)

    def start_counting_time():

        if new_test.start_timer is None:
            new_test.start_timer = time.time()

    def count_words_per_minute():

        if new_test.user_typed_characters is not None:
            start_counting_time()
            time_diff = new_test.count_time_difference()
            if time_diff != 0:
                word_per_minute = (
                    (len(new_test.user_typed_characters) / time_diff) * 60 / 5
                )
                word_per_minute = str(round(word_per_minute, 1))
                words_per_minute = word_per_minute + " words per minute."
                label_time.config(text=words_per_minute)
                print(time_diff)

        label_time.after(100, count_words_per_minute)

    new_test = TestTypingSpeed()
    new_test.import_text_from_file()
    new_test.select_random_text_from_texts()
    print(new_test.list_of_characters)

    font: tuple = ("Arial", 14, "normal")

    window = tk.Tk()
    window.title("Typing Speed Test")
    window.config(width=800, height=800)
    window.config(padx=50, pady=50)

    index1 = "1.192"

    label_top = tk.Text()
    label_top.insert(index=1.0, chars=new_test.text_selected)
    label_top.grid(column=0, row=1)
    label_top.config(font=font, state="disabled", border=0, bg="#F0F0F0")
    label_top.config(wrap="word", height=15)
    # label_top.tag_add("wrong", index1)
    label_top.tag_configure("right", foreground="green")
    label_top.tag_configure("wrong", foreground="red")

    var = tk.StringVar()

    # user_entry = tk.Entry(textvariable=var, font=font)
    # user_entry.config(justify="right", width=80)
    # user_entry.grid(column=0, row=2)

    label_time = tk.Label(text="0.0 words per minute.", font=font)
    label_time.grid(column=0, row=0)

    label_bot = tk.Text()
    label_bot.grid(column=0, row=2)
    label_bot.config(font=font, border=0, bg="#F0F0F0")
    label_bot.config(wrap="word", height=10)
    label_bot.bind("<KeyRelease>", fill_var_from_entry)
    label_bot.tag_configure("right", foreground="green")
    label_bot.tag_configure("wrong", foreground="red")
    label_bot.focus()

    # tk.StringVar.trace_add()

    count_words_per_minute()

    window.mainloop()


if __name__ == "__main__":
    main()
