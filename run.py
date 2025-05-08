import time
import dataQuiz 
from pprint import pprint

quiz_questions = dataQuiz.quiz_questions
score = 0
#pprint(quiz_questions)


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    print("\033c")


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
    


def validate_choice_input(choice, options): 
    try:
        if not choice.strip().lower() in options:
            raise ValueError(f"You need to enter a valid option")
    except ValueError as e:
        print(f"{choice} is Invalid: {e}, please try again\n")
        return False

    return True


def validate_back_input(word_yes):
    try:
        if not word_yes.isalpha() or word_yes.lower() != "yes":
            raise ValueError("You must enter exactly 'yes' to go back to the main menu")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True



def check_if_correct(user_answer, correct_answer, user_text, correct_text, country):
    global score
    #print(user_answer)
    #print(correct_answer)
    is_correct = "❌"
    if user_answer == correct_answer:
        score += 1
        is_correct = "✅"
        print(f"{is_correct} Correct: {correct_text} is the capital of {country}")
    else:
        print(f"Your Answer: {user_answer}. {user_text} {is_correct}")
        print(f"Correct Answer: {correct_text} is the capital of {country}")
    print(score)



def back_to_main_menu():
    word_yes = input("If you want to go back to the main menu, enter 'yes'\n")
    clear()

    if validate_back_input(word_yes):
        main_menu()
    else:
        back_to_main_menu()


def start_quiz():
    print("\nStarting the quiz...\n")
    time.sleep(2)
    for question in quiz_questions:
        print("-"*40)
        print(f"What is the capital of {question['country']}?")
        print("-"*40)
        print()
        for letter, answer in question["answers"].items():
            print(f"{letter}. {answer}")
        print()
        user_answer = input("Your answer (A, B, C or D): \n").strip().upper()
        clear()
        options = ["a", "b", "c", "d"]
        if validate_choice_input(user_answer, options):
            correct_answer = question["correct_answer"]
            user_text = question["answers"][user_answer]
            correct_text = question["answers"][correct_answer]
            country = question["country"]
            check_if_correct(user_answer, correct_answer, user_text, correct_text, country)
            
   
   
def main_menu():
    while True:
        show_welcome()
        print("\nPlease select an option:")
        print("1. Introduction")
        print("2. How to Play")
        print("3. Start Quiz")
        print("4. Exit\n")

        choice = input("Enter your choice (1-4): \n")
        clear()
        options = ["1", "2", "3", "4"]

        if validate_choice_input(choice, options):
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


if __name__ == "__main__":
    clear()
    main_menu()
