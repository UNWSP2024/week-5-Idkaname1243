# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as

#     247

# + 129

# ------

# The program should allow the student to enter the answer.
# If the answer is correct, a message of congratulations should be displayed.
# If the answer is incorrect a message showing the correct answer should be displayed.
# The program must use a function that accomplishes part of the needed tasks.
import random
def math_question():
    p1 = random.randint(1,1000)
    p2 = random.randint(1,1000)
    p1 = str(p1)
    p2 = str(p2)
    print("    "+p1)
    print("+")
    print("    "+p2)
    print("________")
    p1 = int(p1)
    p2 = int(p2)
    answer = p1+p2
    student_answer = int(input("enter your anwer here:   "))
    if student_answer == answer:
        print("good job!")
    elif student_answer != answer:
        answer = str(answer)
        print("try again the answer was "+answer)
        answer = int(answer)
while 0 == 0:
    math_question()
