"""
This section contains all imports
"""
import sys


# from pprint import pprint


def get_name():
    """
    Welcome message and get name from user
    """
    print("************************")
    print("       Hangman")
    print("Guess the word to win!")
    print("************************\n")

    while True:
        name_data = input("Enter your name here: ")

        if validate_data(name_data):
            print(f"Welcome {name_data} \n")
            break


def validate_data(name):
    """
    Validates user input for name
    """
    try:
        if name == "":
            raise ValueError("Please input a name \n")

    except ValueError as error:
        print(f"Try again. {error}")
        return False

    return True


def menu():
    print("Main Menu: \n")
    print("1. Instructions")
    print("2. Start Game")
    print("3. Exit \n")

    while True:
        player_choice = input("Please choose from the above menu: ")

        if player_choice == '1':
            instructions()
        elif player_choice == '2':
            print('Play Function')
        elif player_choice == '3':
            exit()
        else:
            print("Ooops, Please choose a valid option from the menu!")
            

def instructions():
    """
    This option shows the user the basic game instructions
    """
    print(
        "\n"
        "How to Play: \n\n"
        "The aim is to make the correct word by guessing "
        "the letters one at a time. \n\n1. To guess, "
        "type a letter of your choice and hit enter. \n2. If you "
        "are right the letter will appear on screen. \n3. If you "
        "are wrong the hangman will start to appear. \n4. You have "
        "6 attempts to guess correctly or its Game Over!! "
    )
    #Give option to play or return to menu.
    print("Are you ready to play Hangman?")

    #Test for valid selection made
    while True:
        lets_go = input("Press 1 for Yes or 2 for No: ")

        if lets_go == '1':
            print("Play Function")
        elif lets_go == '2':
            menu()
        else:
            print("Please make a valid choice.")


def exit():
    print("Thanks for playing Goodbye!")
    sys.exit()
    

def game():
    get_name()
    menu()


game()