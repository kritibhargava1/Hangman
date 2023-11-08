# assignment: Programming Assignment 1
# author: Kriti Bhargava
# date: 01/22/2023
# file: hangman.py is a program that randomly selects a secret word for the player to guess from a list of words based off user inputs. Then the game is repeated as many time the user wants.
# input: (The use will be asked how long the word shall be and how many lives they want in numbers. They then guess letters one by one. At the end of the game they input weather they want to play again, a y for yes or n for no)
# output: (The program out puts the results of the game, if they won or lost, and if they want to play again)


from random import choice, random

dictionary_file = "dictionary.txt"  


def import_dictionary(filename):
    dictionary = {}
    max_size = 12

    with open(filename) as f:
        for line in f:
            line = line.replace(' ', '')
            line = line.replace('\n', '')

            if len(line) >= 12 and 12 in dictionary.keys():
                dictionary[12].append(line)
            elif len(line) >= 12 and 12 not in dictionary.keys():
                dictionary[12] = [line]
            elif len(line) in dictionary.keys():
                dictionary[len(line)].append(line)
            else:
                dictionary[len(line)] = [line]

    dictionary = dict(sorted(dictionary.items()))
    f.close()

    return dictionary



def print_dictionary(dictionary):
    max_size = 12

    print(dictionary)


def get_game_options():

    print(f'Please choose a size of a word to be guessed [3 - 12, default any size]:')

    num_letters = input()

    try:
        num_letters = int(num_letters)
        print(f'The word size is set to {str(num_letters)}.')

    except ValueError:
        num_letters = None
        print(f'A dictionary word of any size will be chosen.')

    if not (3 <= num_letters <= 12):
        num_letters = None
        print(f'A dictionary word of any size will be chosen.')

    elif num_letters == None:
        num_letters = num_letters
    
    print(f'Please choose a number of lives [1 - 10, default 5]:')

    num_lives = input()

    try:
        num_lives = int(num_lives)

    except ValueError:
        num_lives = 5
    if not (10 >= num_lives >= 1):
        num_lives = 5
    print(f'You have {num_lives} lives.')
    return (num_letters, num_lives)


if __name__ == '__main__':
    dictionary = import_dictionary(dictionary_file)

    print('Welcome to the Hangman Game!')

    while True:

        num_letters, num_lives = get_game_options()

        if num_letters:
            secret_word = choice(dictionary[num_letters]).lower()
        else:
            num_letters = choice(range(3, 13))
            secret_word = choice(dictionary[num_letters]).lower()
        curr_lives = num_lives
        empty = []
        ipt_letter = []
        right_letter = []
        
        for i in range(len(secret_word)):
            if secret_word[i] == '-':
                empty.append('-')
            else:
                empty.append('__')


                
        while True:

            print('Letters chosen: ', end='')

            if len(ipt_letter) > 0:
                for i in range(len(ipt_letter)-1):
                    print(ipt_letter[i].upper(), end=', ')
                print(ipt_letter[len(ipt_letter)-1].upper(), end='')

            print()

            for i in empty:
                print(i, end=' ')


            print(' lives:', curr_lives, end=' ')

            
            for i in range(num_lives - curr_lives):
                print('X', end='')

            for i in range(curr_lives):
                print('O', end='')
            

            print()

            if curr_lives == 0:
                print(f'You lost. The word is {secret_word.upper()}!')
                break
            elif '__' not in empty:
                print(f'Congratulations!!! You won! The word is {secret_word.upper()}!')
                break
            

            print(f'Please choose a new letter >')
            letter = input()
            while True:
                if not letter.isalpha() or len(letter) != 1:
                    print(f'Please choose a new letter >')
                    letter = input()
                elif letter in ipt_letter:
                    print(f'You have already chosen this letter.')
                    print(f'Please choose a new letter >')
                    letter = input()
                else:
                    if letter in secret_word:
                        print(f'You guessed right!')
                        right_letter.append(letter)
                    else:
                        print('You guessed wrong, you lost one life.')
                        curr_lives -= 1
                    ipt_letter.append(letter)
                    break
                
            for i in secret_word:
                if i in ipt_letter:
                    for j in range(len(secret_word)):
                        if secret_word[j] == i:
                            empty[j] = i.upper()

   
   
        print('Would you like to play again [Y/N]?')
        repeat = input().lower()
        if repeat != 'y':
            break
        else:
            continue