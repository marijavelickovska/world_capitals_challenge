# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import dataQuiz

quiz_questions = dataQuiz.quiz_questions
#print(quiz_questions)

def show_welcome():
    print("="*40)
    print("Welcome to the World Capitals Challenge")
    print("="*40)



def show_introduction():
    print("\n--- Introduction ---")
    print("\nThis is a quiz where you will be asked about the capital cities of various countries.")
    print("Try to answer as many questions correctly as you can!\n")
    back_to_main_menu()



def show_how_to_play():
    print("\n--- How to Play ---")
    print("\n1. You will be asked to name the capital of a given country.")
    print("2. Four possible capital cities will be offered, labeled A, B, C, and D.")
    print("3. Type the letter (A, B, C, or D) that corresponds to the correct capital and press Enter.")
    print("4. You will receive feedback after each question.")
    print("5. At the end, you'll see your final score.\n")
    back_to_main_menu()



def start_quiz():
    print("\nStarting the quiz...\n")


def back_to_main_menu():
    back = input("If you want to go back to the main menu, enter 'yes'\n")

    if back == "yes":
        main_menu()


    
def validate_input(choice): 
    try:
        if int(choice) not in range(1,5):
            raise ValueError("You need to enter a number from 1 to 4")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True
    


def main_menu():
    while True:
        show_welcome()
        print("\nPlease select an option:")
        print("1. Introduction")
        print("2. How to Play")
        print("3. Start Quiz")
        print("4. Exit\n")

        choice = input("Enter your choice (1-4): \n")

        if validate_input(choice):
            if choice == "1":
                show_introduction()
            elif choice == "2":
                show_how_to_play()
            elif choice == "3":
                start_quiz()
            elif choice == "4":
                print("Goodbye!")
                return False
            else:
                print("Invalid choice. Please enter a number from 1 to 4.\n")


main_menu()
