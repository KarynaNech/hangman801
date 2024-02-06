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

**__init__(self, word_list, num_lives)**: <br />
&emsp;    Parameters:<br />
&emsp;    ----------<br />
&emsp;    word_list: list<br />
&emsp;&emsp;       List of words to be used in the game<br />
&emsp;    num_lives: int <br />
&emsp;&emsp;        Number of lives the player has<br />
&emsp;    Attributes:<br />
&emsp;    ----------<br />
&emsp;    num_of_lives: int<br />
&emsp;&emsp;        A number of lives the player has, 5 by default<br />
&emsp;    __word: str<br />
&emsp;&emsp;        For internal use, the word chosen by computer<br />
&emsp;    __word_as_list: list<br />
&emsp;&emsp;        For internal use, the word chosen by computer as a list of letters<br />
&emsp;    word_user_view:<br />
&emsp;&emsp;        A string of '_' and letters corresponding to the letters guessed already<br />
&emsp;    _unique_letters: int<br />
&emsp;&emsp;        The number of unique symbols in the word<br />
&emsp;    num_of_lives: int<br />
&emsp;&emsp;        Lifes remaining<br />
    list_of_guesses: list<br />
        A list of letters previously attempted by the user. <br />
        

**check_guess(self, guess)**: checks is the guess is in the word.
In case it is, reduces *num_of_letters* by 1 and updates *word_user_view* to show the letters guessed.
In case it is now, reduces *num_of_lives* by 1. 
It also prints the message for the user to announce the outcome.

**play(self)**: iteratively asks the user for input to receive a single letter that is not in the *list_of_guesses*, and then calls **check_guess** function.

### License information
No license.
