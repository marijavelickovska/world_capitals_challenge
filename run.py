import time
import random
import sys # added to enable the use of sys.exit()
import dataQuiz
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


score = 0


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    print("\033c")


def show_welcome():
    """
    Displays a welcome message to the user when the program starts.
    """
    print("="*45)
    print(f"{Fore.YELLOW} Welcome to the World Capitals Challenge 🗺️")
    print("="*45)


def show_introduction():
    """
    Displays an introduction to the quiz,
    explaining the quiz and how to proceed.
    """
    print(f"{Fore.YELLOW}\n--- Introduction ---")
    print(
        "\nThis is a quiz where you will be asked about "
        "the capital cities of various countries."
    )
    print("Try to answer as many questions correctly as you can!\n")
    ask_to_play_quiz()


def show_how_to_play():
    """
    Displays instructions on how to play the quiz and how to proceed.
    """
    print(f"{Fore.YELLOW}\n--- How to Play ---")
    print("\n1. You will be asked to name the capital of a given country.")
    print(
        "2. Four possible capital cities will be offered,"
        "labeled A, B, C, and D."
    )
    print(
        "3. Type the letter (A, B, C, or D)"
        "that corresponds to the correct capital and press Enter."
    )
    print("4. You will receive feedback after each question.")
    print("5. At the end, you'll see your final score.\n")
    ask_to_play_quiz()


def exit_program():
    clear()
    print("-"*40)
    print(f"{Fore.YELLOW}Goodbye!")
    print("-"*40)
    print()
    sys.exit()


def validate_yes_no_input(yes_no_answer):
    """
    Validates the user's input to ensure it is either 'yes' or 'no'.
    Displays an error message for invalid input.
    """
    try:
        if yes_no_answer not in ("yes", "no"):
            raise ValueError(f"{Fore.RED}You must enter exactly 'yes' or 'no'")
    except ValueError as e:
        print(
            f"{Fore.RED} {yes_no_answer} is Invalid: {e},"
            "please try again\n")
        return False

    return True


def validate_choice_input(choice, options):
    """
    Validates the user's choice input to ensure
    it is one of the options: 'A', 'B', 'C', or 'D'.
    Displays an error message for invalid input.
    """
    try:
        if not choice.strip().lower() in options:
            raise ValueError(f"{Fore.RED} You need to enter a valid option")
    except ValueError as e:
        print(f"{Fore.RED} {choice} is Invalid: {e}, please try again\n")
        return False

    return True


def handle_yes_no_response(yes_no_answer):
    """
    Handles the user's yes/no response. First, validates the input.
    If valid, directs the user to the appropriate action
    (either the quiz or main menu) and returns true (to break the while loop).
    If the input is invalid, returns false (so the while loop can show
    the input again to ask for a valid response).
    """
    if validate_yes_no_input(yes_no_answer):
        if yes_no_answer == "yes":
            start_quiz()
            return True
        elif yes_no_answer == "no":
            main_menu()
            return True
    else:
        return False


def ask_to_play_quiz():
    """
    Asks the user if they would like to play the quiz by
    prompting for a yes/no response.
    Calls the handle_yes_no_response function to validate
    the input and direct the user based on their answer.
    """
    while True:
        yes_no_answer = input(
            "Would you like to take the quiz? Enter yes/no ⬇️\n"
        ).lower()
        clear()
        if handle_yes_no_response(yes_no_answer):
            break


def check_if_correct(
    user_answer,
    correct_answer,
    user_text,
    correct_text,
    country
):
    """
    Checks if the user's answer matches the correct answer.
    If correct, increases the score by 1 and displays the user's
    correct answer.
    If incorrect, shows the user's answer along with the correct one.
    At the end, prints the user's current score.
    """
    global score
    is_correct = "❌"
    if user_answer == correct_answer:
        score += 1
        is_correct = "✅"
        print(
            f"{Fore.GREEN}{is_correct} Correct: {Fore.RESET} {correct_text} "
            f"is the capital of {country}"
        )
    else:
        print(
            f"{Fore.RED}Your Answer: {Fore.RESET} {user_answer}.{user_text}"
            f"{is_correct}"
        )
        print(
            f"{Fore.GREEN}Correct Answer: {Fore.RESET} {correct_text} "
            f"is the capital of {country}"
        )
    print(f"{Style.BRIGHT}Your score is: {score}\n")


def end_quiz():
    """
    Displays a message that the quiz is complete and shows
    the user's final score.
    Prompts the user with an input asking if they would like to play again,
    then calls the function to handle the answer and redirects the user
    based on their response.
    """
    clear()
    print("*"*40)
    print(f"{Fore.YELLOW} You completed the quiz! 🏁")
    print("*"*40)
    print()
    print("-"*40)
    print(
        f"{Style.BRIGHT} Your final score is "
        f"{Fore.YELLOW}{score}{Fore.WHITE} / {Fore.GREEN}15"
    )
    print("-"*40)
    print()
    while True:
        yes_no_answer = input(
            "Would you like to play again? Enter yes/no ⬇️\n"
        ).lower()
        clear()
        if handle_yes_no_response(yes_no_answer):
            break


def start_quiz():
    """
    Starts the quiz by randomly selecting 15 out of 30 questions.
    For each question, displays four possible answers and prompts the user
    to enter their answer using A, B, C, or D.
    Validates the user's input using the validate_choice_input function.
    Increments the index to move to the next question and calls
    the check_if_correct function to evaluate the answer.
    At the end, checks if the index is equal to the
    total number of quiz questions and, if so, calls the end_quiz function.
    """
    print(f"{Fore.GREEN}\nStarting the quiz...\n")
    time.sleep(1)
    quiz_questions = random.sample(dataQuiz.quiz_questions, 15)
    index = 0
    while index < len(quiz_questions):
        question = quiz_questions[index]
        print(f"Question {index + 1}/15")
        print("-"*40)
        print(f"{Style.BRIGHT} What is the capital of {question['country']}?")
        print("-"*40)
        print()
        for letter, answer in question["answers"].items():
            print(f"{letter}. {answer}")
        print()
        user_answer = input(
            "Your answer (A, B, C or D): ⬇️ \n"
        ).strip().upper()
        clear()
        options = ["a", "b", "c", "d"]
        if validate_choice_input(user_answer, options):
            index += 1
            correct_answer = question["correct_answer"]
            user_text = question["answers"][user_answer]
            correct_text = question["answers"][correct_answer]
            country = question["country"]
            check_if_correct(
                user_answer,
                correct_answer,
                user_text,
                correct_text,
                country
            )
        if index == len(quiz_questions):
            end_quiz()


def main_menu():
    """
    Displays the welcome message and a list of menu options
    for the user to choose from.
    Prompts the user to enter a number between 1 and 4.
    Validates the user's input using the validate_choice_input function and,
    if valid, redirects them based on their selection.
    """
    while True:
        show_welcome()
        print("\nPlease select an option:")
        print("1. Introduction")
        print("2. How to Play")
        print("3. Start Quiz")
        print("4. Exit\n")

        choice = input("Enter your choice (1-4): ⬇️ \n")
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
                exit_program()
            else:
                print("Invalid choice. Please enter a number from 1 to 4.\n")


""" Clears the screen and starts the main menu when the
script is executed directly. """
if __name__ == "__main__":
    clear()
    main_menu()
