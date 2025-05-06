# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import dataQuiz

quiz_questions = dataQuiz.quiz_questions
print(quiz_questions)

def show_welcome():
    print("="*40)
    print("Welcome to the World Capitals Challenge")
    print("="*40)




def show_introduction():
    print("\n--- Introduction ---")
    print("This is a quiz where you will be asked about the capital cities of various countries.")
    print("Try to answer as many questions correctly as you can!\n")



def show_how_to_play():
    print("\n--- How to Play ---")
    print("1. You will be asked to name the capital of a given country.")
    print("2. Four possible capital cities will be offered, labeled A, B, C, and D.")
    print("3. Type the letter (A, B, C, or D) that corresponds to the correct capital and press Enter.")
    print("4. You will receive feedback after each question.")
    print("5. At the end, you'll see your final score.\n")


show_welcome()
show_introduction()
show_how_to_play()