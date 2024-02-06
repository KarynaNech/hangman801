#%%
import random

class Hangman:
    '''
    This class represents the Hangman game. After initiating
    the class, use play() method to proceed with the game.

    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has

    Attributes:
    ----------
    num_of_lives: int
        A number of lives the player has, 5 by default
    __word: str
        For internal use, the word chosen by computer
    __word_as_list: list
        For internal use, the word chosen by computer as a list of letters
    word_user_view:
        A string of '_' and letters corresponding to the letters guessed already
    _unique_letters: int
        The number of unique symbols in the word
    num_of_lives: int
        Lifes remaining
    list_of_guesses: list
        A list of letters previously attempted by the user.
    '''
    def __init__(self,  word_list, num_lives=5):
        '''
        Refer to the class documentation.
        '''
        self.__word=random.choice(word_list)
        self.__word_as_list=list(self.__word)
        num_of_letters=len(self.__word)
        self.word_user_view=['_']*num_of_letters
        self._unique_letters=len(set(self.__word))
        self.num_of_lives=num_lives
        self.word_list=word_list
        self.list_of_guesses=[]
    def check_guess(self, guess):
        '''
        Checks if a letter in a variable guess is present
        in the word, and changes the relevant attributs respectibely.
        
        Args:
        -----
        guess: str
            the letter to be checked
        '''
        guess=guess.lower()
        if guess in self.__word:
            print(f'Good guess! {guess} is in the word.')
            #Change the user view of the word and show it to the user:
            for letter in range(len(self.__word_as_list)):
                if self.__word_as_list[letter]==guess:
                    self.word_user_view[letter]=guess
            print(self.word_user_view)
            #There is one less unique letter to guess now
            self._unique_letters-=1
        else:
            #The guess was incorrect, so we must substract one life
            self.num_of_lives-=1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_of_lives} lives left.")
      
    def play(self):
        '''
        Imitates a turn of the game. Asks for user input iteratively until it 
        is a single letter and calls the check_guess() method in this case.
        '''
        while True:
            guess=input('Please select a letter')
            guess=guess.lower()
            #check if guess is indeed a letter
            if not (len(guess)==1 and guess.isalpha()): #checks if it is a single letter
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

# %%
def play_game(word_list):
    '''
    Executes the Hangman game. Initiates the class Hangman and calls the play() 
    method until the user has either lost or won the game, and prints the result.

    Parameters:
    ----------
    word_list: list
        The list of the words on which the game is played
    '''
    num_of_lives=5
    game=Hangman(word_list, num_of_lives)
    while True:
        #End the game if we ran out of lives
        if game.num_of_lives==0:
            print('You\'ve lost!')
            break
        #Continue the game if there are lives remaining and letters to guess
        elif game._unique_letters>0:
            game.play()
        #End the game if the user guessed all of the words 
        else:
            print('Congratulations. You won the game!')
            break


# %%
#Some list of words (foods) to play the game
word_list=[
    'apple', 'bacon', 'bread', 'broil', 'cakes', 'candy', 'chili', 'chips', 'cream', 'crepe',
    'curry', 'dough', 'fruit', 'grape', 'grill', 'herbs', 'honey', 'jelly', 'juice', 'kebab',
    'lemon', 'mango', 'melon', 'mints', 'nacho', 'olive', 'onion', 'pasta', 'peach', 'pearl',
    'pesto', 'pizza', 'prawn', 'quail', 'salad', 'salsa', 'sauce', 'steak', 'sugar', 'sushi',
    'tacos', 'toast', 'trout', 'tunas', 'udons', 'vegan', 'wheat', 'wings', 'wrap', 'yogur',
    'zesty', 'bagel', 'basil', 'berry', 'blini', 'brisk', 'cacao', 'carob', 'cedar', 'chard'
]
play_game(word_list)
# %%
