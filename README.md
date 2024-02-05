# Hangman

### Table of Contents, if the README file is long
### A description of the project: what it does, the aim of the project, and what you learned

Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.
This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 


### Installation instructions
Just run milestone_4.py with a prefferable python interreter. 
### Usage instructions
### File structure of the project
% milestone_3.py contains functins check_guess which checks if the letter is in the word and and ask_user_input, which requires a user input and calls out the check_guess function.

class Hangman is called to play the Hangman gme. It contains the following methods:

**__init__(self, word_list, num_lives)**: defines the following attributes:
    *self.word_list* - a list of words the game is based on
    *self.word* - a randomly chosen word from the list
    *self.word_guessed* - a string of '_' and letters representing known and unknown letters in the word
    *self.num_letters* - a number of unique letters in the word the user has to guess
    *self.list_of_guesses* - a list of all letters the user has already tried
    *self.num_of_lives* - number of lives remaining (5 by default)
        

**check_guess(self, guess)**: checks is the guess is in the word, and respectively reduces num_letters by 1 in case it is & reduces num_of_lives by 1 if it is not. It also prints the message for the user to infor of their outcome.

**ask_for_input(self)**: iteratively asks the user for input to receive a single letter, and then calls **check_guess** function.

### License information
