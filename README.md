# Hangman Game

Welcome to the Hangman Game! This Python program, `hangman.py`, allows you to play the classic word-guessing game. You'll be provided with a hidden word, and you need to guess it one letter at a time while managing your available lives. Below, you'll find details on the program's functionality, usage, and author information.

## Program Files

- `hangman.py`: The main program file containing the Hangman game code.

## How the Game Works

1. You start the game by choosing the size of the word to be guessed (ranging from 3 to 12 letters) and the number of lives you have (between 1 and 10). If you don't specify, default settings are used (any word size and 5 lives).

2. The program selects a random word from the dictionary based on your preferences.

3. You are given a set number of lives, and an empty display shows you the letters you've guessed correctly and the letters you haven't guessed yet.

4. Guess one letter at a time. If your guess is correct, the letter will be revealed in the word. If you guess wrong, you lose one life.

5. Continue guessing until you've guessed the word correctly, or you've run out of lives.

6. The game ends with a win or loss message. You can choose to play again.

## How to Play

1. Run the game by executing `hangman.py` using a Python interpreter.

2. You'll be prompted to set the word size and the number of lives.

3. Guess letters by entering them one at a time when prompted.

4. Keep guessing until you either win or run out of lives.

5. After each game, you can choose to play again.

## Example Gameplay

Here's an example of how the game might be played:

```plaintext
Welcome to the Hangman Game!

Please choose a size of a word to be guessed [3 - 12, default any size]:
5
The word size is set to 5.

Please choose a number of lives [1 - 10, default 5]:
6
You have 6 lives.

Letters chosen:

__ __ __ __ __  lives: OOOOOO

Please choose a new letter > a
You guessed wrong, you lost one life.
Letters chosen: A

__ __ __ __ __  lives: OOOOO

Please choose a new letter > e
You guessed right!
Letters chosen: A, E

E __ __ __ E  lives: OOOOO

Please choose a new letter > t
You guessed wrong, you lost one life.
Letters chosen: A, E, T

E __ __ __ E  lives: OOOOX

Please choose a new letter > l
You guessed wrong, you lost one life.
Letters chosen: A, E, T, L

E __ __ __ E  lives: OOOXX

Please choose a new letter > m
You guessed wrong, you lost one life.
Letters chosen: A, E, T, L, M

E __ __ __ E  lives: OOXXX

Please choose a new letter > o
You guessed right!
Letters chosen: A, E, T, L, M, O

E __ __ O E  lives: OOXXX

Please choose a new letter > n
You guessed right!
Letters chosen: A, E, T, L, M, O, N

E N __ O E  lives: OOXXX

Please choose a new letter > s
You guessed right!
Letters chosen: A, E, T, L, M, O, N, S

E N __ O E  lives: OOXXX

Please choose a new letter > d
You guessed right!
Letters chosen: A, E, T, L, M, O, N, S, D

E N D O E  lives: OOXXX

Congratulations!!! You won! The word is "ENDOE."

Would you like to play again [Y/N]?
n
Goodbye!
```

## Author Information

This Hangman game was created by Kriti Bhargava. 

## Acknowledgments

- The Hangman game is a classic word-guessing game enjoyed by people of all ages.
Please feel free to contribute to or improve this game by submitting pull requests or reporting issues. Enjoy playing Hangman, and happy coding!
