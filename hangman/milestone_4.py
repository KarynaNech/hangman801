#%%

import random

class Hangman:
    '''
    This class represents the Hangman game. After initiating
    the class, use play() method to proceed with the game.

    Attributes:
    word_list (list): A list of words which can be used for the gamee
    num_of_lives (int): A number of lives the player has, 5 by default.
    word (str): For internal use, the word chosen by computer.
    word_user_view (str): A string of '_' and letters corresponding to
    the letters guessed already.
    unique_letters (int): For internal use, number of unique symbols in the word
    num_of_lives (int): Lifes remaining
    list_of_guesses (list): A ;ist of letters previously attempted by the user.
    
    '''
    def __init__(self,  word_list, num_lives=5):
        '''
        Refer to the class documentation.
        '''
        self.word=random.choice(word_list)
        self.word_as_list=list(self.word)
        num_of_letters=len(self.word)
        self.word_user_view=['_']*num_of_letters
        self.unique_letters=len(set(self.word))
        self.num_of_lives=num_lives
        self.word_list=word_list
        self.list_of_guesses=[]
    def check_guess(self, guess):
        '''
        This method checks if a letter in a variable guess is present
        in the word, and changes the relevant attributs respectibely.
        
        Args:
        guess (str): the letter to be checked
        '''
        guess=guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            #Change the user view of the word and show it to the user:
            for letter in range(len(self.word_as_list)):
                if self.word_as_list[letter]==guess:
                    self.word_user_view[letter]=guess
            print(self.word_user_view)
            #There is one less unique letter to guess now
            self.unique_letters-=1
        else:
            #The guess was incorrect, so we must substract one life
            self.num_of_lives-=1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_of_lives} lives left.")
      
    def play(self):
        '''
        This method imitates a turn of the game. It asks for user input
        iteratively until it is a single letter and calls the 
        check_guess() method in this case.
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
game=Hangman(['pear', 'dark', 'pain', 'pipe', 'card', 'name'])
# %%
game.play()

# %%
