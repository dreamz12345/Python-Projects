import os
from time import sleep


def clear_screen():
    os.system("cls")



class QuizBrain:

    def __init__(self, q_list) -> None:
        self.question_number = 0
        self.score = 0
        self.question_list = q_list


    def still_has_questions(self) -> bool:
        number_of_questions = len(self.question_list)
        if self.question_number == number_of_questions:
            return False
        return True


    def next_question(self):
        clear_screen()
        current_question = self.question_list[self.question_number]
        text = current_question.text
        question_display_index = self.question_number + 1
        user_answer = input(f"Q.{question_display_index}: {text}"
                            f" ('True' or 'False'): ")
        correct_answer = current_question.answer
        self.check_answer(user_answer, correct_answer)
        print(f"Your score is: {self.score}/{question_display_index}\n")
        self.question_number += 1
        for remaining_time in range(5, 0, -1):
            print(f"Next question in {remaining_time}...", end="\r")
            sleep(1)


    def check_answer(self, user_anwser, correct_answer):
        if user_anwser.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That is the wrong answer.")
        print(f"The correct answer was: {correct_answer}.")
