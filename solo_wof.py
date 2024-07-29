import random as r
import math as m


def get_phrase():
    """Fetch a random phrase from the phrases file."""
    with open('C:/Users/hansm/OneDrive/Documents/Coding/Python/phrases.txt') as doc:
        lines = doc.read().split('\n')
    lines.pop()
    random_number = m.floor(r.random()*len(lines))
    phrase = lines[random_number]
    return phrase


def spin_the_wheel():
    """Simulates spinning the wheel."""
    wheel_list = [500, 500, 500, 500, 500, 550, 600, 600, 600, 600, 650, 650, 650, 700, 700, 700, 800, 900, 2500, 'BANKRUPT', 'BANKRUPT']
    random_number = m.floor(r.random()*21)
    spin = wheel_list[random_number]
    return spin


def get_board(round_number, board_list, round_consonants, round_vowels, balance):
    """Prints the current state of the board."""
    round_consonant_string = ""
    round_vowel_string = ""
    board = ""
    for n in round_consonants:
        round_consonant_string += n
    for n in round_vowels:
        round_vowel_string += n
    for n in board_list:
        board += n
    text = f'${balance:,}'
    print(f":::::::::::::::::::::::::::::::::::::::::: ROUND {round_number} of 4 ::")
    print(f"::{board: ^54}::")
    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    print(f"::   {round_consonant_string}   ::   {round_vowel_string}   ::{text.rjust(11)} ::")
    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")


def setup():
    """Re-initializes the game's state for a new round."""
    balance = 0
    round_consonants = 'BCDFGHJKLMNPQRSTVWXYZ'
    round_vowels = 'AEIOU'
    original_phrase = get_phrase()
    phrase_list = list(original_phrase.upper())
    board_list = []
    for n in phrase_list:
        if n in round_consonants or n in round_vowels:
            board_list.append('_')
        else:
            board_list.append(n)
    return phrase_list, original_phrase, board_list, round_consonants, round_vowels, balance


def option():
    """Prompts the user for an action."""
    print("What would you like to do?")
    print("  1 - Spin the wheel")
    print("  2 - Buy a vowel")
    print("  3 - Solve the puzzle")
    print("  4 - Quit the game")
    selection = input("Enter the number of your choice: ")
    while selection not in ['1', '2', '3', '4']:
        print(f'{selection} is an invalid choice.')
        print("What would you like to do?")
        print("  1 - Spin the wheel")
        print("  2 - Buy a vowel")
        print("  3 - Solve the puzzle")
        print("  4 - Quit the game")
        selection = input("Enter the number of your choice: ")
    return selection


def choice_1(phrase_list, board_list, round_consonants, round_vowels, balance):
    """Handles the spin the wheel action."""
    consonants = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
    if round_consonants == '                     ':
        print("There are no more consonants to choose.")
    else:
        spin = spin_the_wheel()
        if spin == 'BANKRUPT':
            print(f'The wheel landed on {spin}.')
            print(f'You lost ${balance:,}!')
            balance = 0
        else:
            print(f'The wheel landed on ${spin:,}.')

            pre_selected_consonant = str(input("Pick a consonant: ")) #this block collects and validates user inputted consonant
            selected_consonant = pre_selected_consonant.upper()
            while selected_consonant not in round_consonants or len(selected_consonant) != 1:
                if selected_consonant in round_vowels and selected_consonant != '':
                    print("Vowels must be purchased.")
                elif len(selected_consonant) != 1:
                    print("Please enter exactly one character.")
                elif selected_consonant in consonants and selected_consonant not in round_consonants:
                    print(f"The letter {selected_consonant} has already been used.")
                else:
                    print(f"The character {selected_consonant} is not a letter.")
                pre_selected_consonant = str(input("Pick a consonant: "))
                selected_consonant = pre_selected_consonant.upper()
            if selected_consonant in phrase_list:
                occurences = phrase_list.count(selected_consonant)
                for n in phrase_list:
                    if n == selected_consonant:
                        indexes = phrase_list.index(selected_consonant)
                        board_list[indexes] = selected_consonant
                        phrase_list[indexes] = '1'
                balance += spin*occurences
                if occurences == 1:
                    print(f'There is 1 {selected_consonant}, which earns you ${spin:,}.')
                else:
                    print(f'There are {occurences} {selected_consonant}\'s, which earns you ${spin*occurences:,}.')
            else:
                print(f'I\'m sorry, there are no {selected_consonant}\'s.')
            round_consonants = round_consonants.replace(selected_consonant, ' ')
    return phrase_list, board_list, round_consonants, round_vowels, balance


def choice_2(phrase_list, board_list, round_consonants, round_vowels, balance):
    """Handles the buy a vowel action."""
    vowels = ['A','E','I','O','U']
    if balance < 250:
        print("You need at least $250 to buy a vowel.")
    elif round_vowels == '     ':
        print('There are no more vowels to buy.')
    else:
        pre_selected_vowel = str(input("Pick a vowel: ")) #this block collects and validates user inputted consonant
        selected_vowel = pre_selected_vowel.upper()
        while selected_vowel not in round_vowels or len(selected_vowel) != 1:
            if selected_vowel in round_consonants and selected_vowel != '':
                print("Consonants cannot be purchased.")
            elif len(selected_vowel) != 1:
                print("Please enter exactly one character.")
            elif selected_vowel in vowels and selected_vowel not in round_vowels:
                print(f"The letter {selected_vowel} has already been purchased.")
            else:
                print(f"The character {selected_vowel} is not a letter.")
            pre_selected_vowel = str(input("Pick a vowel: "))
            selected_vowel = pre_selected_vowel.upper()
        if selected_vowel in phrase_list:
            occurences = phrase_list.count(selected_vowel)
            for n in phrase_list:
                if n == selected_vowel:
                    indexesv = phrase_list.index(selected_vowel)
                    board_list[indexesv] = selected_vowel
                    phrase_list[indexesv] = ' '
            if occurences == 1:
                print(f'There is 1 {selected_vowel}.')
            else:
                print(f'There are {occurences} {selected_vowel}\'s.')
        else:
            print(f'I\'m sorry, there are no {selected_vowel}\'s.')
        balance -= 250
        round_vowels = round_vowels.replace(selected_vowel, ' ')
    return phrase_list, board_list, round_consonants, round_vowels, balance


def choice_3(phrase_list, original_phrase, board_list, balance, total):
    """Handles the solve the puzzle action."""
    board = ""
    for n in board_list:
        board += n
    print('Enter your solution.')
    print(f'  Clues: {board}')
    guess = str(input(f'  Guess: '))
    guess_upper = guess.upper()
    if list(guess_upper) == list(original_phrase.upper()):
        print('Ladies and gentlemen, we have a winner!')
        if balance > 1000:
            pass
        else:
            balance = 1000
        print(f'You earned ${balance:,} this round.')
        total += balance
    else:
        balance = 0
        print(f'I\'m sorry. The correct solution was:')
        print(f'{original_phrase.upper()}')
        print(f'You earned ${balance:,} this round.')
    return phrase_list, original_phrase, board_list, balance, total


def main():
    """Main game loop."""
    total = 0
    quitter = 0

    for n in range(1, 5):
        if quitter == 1:
            break
        selection = 0
        round_number = n
        phrase_list, original_phrase, board_list, round_consonants, round_vowels, balance = setup()
        while selection != '3':
            get_board(round_number, board_list, round_consonants, round_vowels, balance)
            selection = option()
            if selection == '1':
                phrase_list, board_list, round_consonants, round_vowels, balance = choice_1(phrase_list, board_list, round_consonants, round_vowels, balance)

            elif selection == '2':
                phrase_list, board_list, round_consonants, round_vowels, balance = choice_2(phrase_list, board_list, round_consonants, round_vowels, balance)

            elif selection == '3':
                phrase_list, original_phrase, board_list, balance, total = choice_3(phrase_list, original_phrase, board_list, balance, total)

            elif selection == '4':
                balance = 0
                print(f'You earned ${balance:,} this round.')
                quitter = 1
                break
    print('Thanks for playing!')
    print(f'You earned a total of ${total:,}.')


if __name__ == '__main__':
    main()
