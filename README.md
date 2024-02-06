# Hangman

Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.
This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

### Installation instructions
Run milestone_5.py in a prefferable python interpeter. 

### Usage instructions
The game begins by calling a function play_game(). You will need to input letters as instructed by the program and
you will be informed of the outcome of your guesses by the program.

### File structure of the project
% milestone_5.py contains the class **Hangman** designed to play the Hangman game, and the function **play_game()** which calls the class to provide
the interface for a user. 

**Hangman** class contains the following methods:

**__init__(self, word_list, num_lives)**: defines the following attributes:
    *word_list (list)*: A list of words which can be used for the game
    *num_of_lives (int)*: A number of lives the player has, 5 by default
    *__word (str)*: For internal use, the word chosen by computer
    *word_user_view (str)*: A string of '_' and letters corresponding to
    the letters guessed already
    *__unique_letters (int)*: For internal use, number of unique symbols in the word
    *num_of_lives (int)*: Lifes remaining
    *list_of_guesses (list)*: A list of letters previously attempted by the user
        

**check_guess(self, guess)**: checks is the guess is in the word.
In case it is, reduces *num_of_letters* by 1 and updates *word_user_view* to show the letters guessed.
In case it is now, reduces *num_of_lives* by 1. 
It also prints the message for the user to announce the outcome.

**play(self)**: iteratively asks the user for input to receive a single letter that is not in the *list_of_guesses*, and then calls **check_guess** function.

### License information
No license.
