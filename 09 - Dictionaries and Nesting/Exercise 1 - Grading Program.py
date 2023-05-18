import os
os.system("cls")

def grading_scores(student_scores):
    student_grades = {}
    for student in student_scores:
        if student_scores[student] <= 70:
            student_grades[student] = "Fail"

        elif student_scores[student] <= 80:
            student_grades[student] = "Acceptable"

        elif student_scores [student] <= 90:
            student_grades[student] = "Exceeds Expectations"

        elif student_scores[student] > 90:
            student_grades[student] = "Outstanding"
    return student_grades

student_scores = {
    "Dog": 91,
    "Cat": 82,
    "Mouse": 100,
    "Bird": 74,
    "Wolf": 68,
}

student_grades = grading_scores(student_scores)
print(student_grades)