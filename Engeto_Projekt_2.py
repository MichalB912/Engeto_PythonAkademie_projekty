"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Michal Boček
email: michal.678@seznam.cz
discord: Michal B.#2426
"""


import random

rounds = 8
game_on = True


def greet():
    '''
    Greets user and gives instructions to play.
    '''
    print(
        f'''
        Let\'s play Bulls and Cows.
        Guess a four-digit number, all digits unique, not beginning with "0".
        You have 8 tries.
        If you guess correct number and position, you get a "bull".
        If you guess correct number only, you get a "cow".
        Get 4 bulls to win!
        '''
        )


def create_number():
    '''
    Creates four digits number for user to guess
    '''
    number = random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], k=4)

    if len(number) != len(set(number)) or number[0] == 0:
        create_number()
    elif number == None:
        create_number()
    else:
        number = "".join([str(i) for i in number])
        return number


def player_ranking():
    '''
    Based on residual value in global variable "rounds" evaluate user's skill (very good, good, average, etc.)
    '''

    if rounds >= 6:
        evaluation = "excellent!"
    elif 4 <= rounds < 5:
        evaluation = "good!"
    elif 2 <= rounds < 4:
        evaluation = "average."
    else:
        evaluation = "not so good..."

    return evaluation


secret_number = create_number()
greet()
bulls = 0
cows = 0



while game_on and rounds > 0:
    
    user_guess = input("Guess a number: ")
    rank = player_ranking()

    if len(user_guess) == len(set(user_guess)) and user_guess[0] != "0" and len(user_guess) == 4 and user_guess.isdigit():
        rounds -=  1
        for i, n in enumerate(user_guess):
            if n in secret_number and user_guess[i] == secret_number[i]:
                bulls += 1
            if n in secret_number and user_guess[i] != secret_number[i]:
                cows += 1
        if cows == 1 and bulls == 1:
            print(f"You have {cows} cow and {bulls} bull.")
        elif bulls == 1:
            print(f"You have {cows} cows and {bulls} bull.")
        elif cows == 1:
            print(f"You have {cows} cow and {bulls} bulls.")
        else:
            print(f"You have {cows} cows and {bulls} bulls.")
        bulls = 0
        cows = 0
        if user_guess == secret_number:
            print(f"Correct! You have guessed the right number with {rounds} rounds remaining :-)! That is {player_ranking()}")
            game_on = False
        elif rounds == 0:
            print(f"""You have failed to guess a secret number :-( 
                Number was {secret_number}""")
            game_on = False
    else:
        print("Invalid number format, guess again")
        continue


