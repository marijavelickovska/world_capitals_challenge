import time
import random
import dataQuiz 


quiz_questions = random.sample(dataQuiz.quiz_questions, 15)
score = 0


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
    ask_to_play_quiz()


def show_how_to_play():
    print("\n--- How to Play ---")
    print("\n1. You will be asked to name the capital of a given country.")
    print("2. Four possible capital cities will be offered, labeled A, B, C, and D.")
    print("3. Type the letter (A, B, C, or D) that corresponds to the correct capital and press Enter.")
    print("4. You will receive feedback after each question.")
    print("5. At the end, you'll see your final score.\n")
    ask_to_play_quiz()


def validate_yes_no_input(yes_no_answer):
    try:
        if yes_no_answer not in ("yes", "no"):
            raise ValueError("You must enter exactly 'yes' or 'no'")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True

    
def validate_choice_input(choice, options): 
    try:
        if not choice.strip().lower() in options:
            raise ValueError(f"You need to enter a valid option")
    except ValueError as e:
        print(f"{choice} is Invalid: {e}, please try again\n")
        return False

    return True


def handle_yes_no_response(yes_no_answer):
    if validate_yes_no_input(yes_no_answer):
        if yes_no_answer == "yes":
            start_quiz() 
        elif yes_no_answer == "no":
            main_menu()
        else:
            print("Please enter a valid answer (yes or no).\n")



def ask_to_play_quiz():
    yes_no_answer = input("Would you like to take the quiz? Enter yes/no\n").lower()
    clear()
    handle_yes_no_response(yes_no_answer)



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
    print(f"Your score is: {score}\n")


def end_quiz():
        clear()
        print("-"*40)
        print("You completed the quiz!")
        print("-"*40)
        print(f"Your final score is {score}/15\n")
        print("-"*40)
        yes_no_answer = input("Would you like to play again? Enter yes/no\n").lower()
        clear()
        handle_yes_no_response(yes_no_answer)



def start_quiz():
    print("\nStarting the quiz...\n")
    time.sleep(1)
    index = 1
    for question in quiz_questions:
        print(f"Question {index}/15")
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
            index += 1
            correct_answer = question["correct_answer"]
            user_text = question["answers"][user_answer]
            correct_text = question["answers"][correct_answer]
            country = question["country"]
            check_if_correct(user_answer, correct_answer, user_text, correct_text, country)
        if index == len(quiz_questions):
            end_quiz()
            
   
   
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
