from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from html import unescape
from ui import QuizzlerInterface

question_bank = []
for question in question_data:
    question_text: str = question["question"]
    question_text = unescape(question_text)
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_interface = QuizzlerInterface(quiz)
# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
