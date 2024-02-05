#%%
import random

class Hangman:
    def __init__(self,  word_list, num_lives=5):
        self.word=random.choice(word_list)
        num_of_letters=len(self.word)
        self.word_guessed=['_']*num_of_letters
        self.num_letters=len(set(self.word))
        self.num_of_lives=num_lives
        self.word_list=word_list
        self.list_of_guesses=[]
    def check_guess(self, guess):
        guess=guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            for letter in range(len(self.word)):
                if self.word[letter]==guess:
                    self.word_list[letter]==guess
            self.num_letters-=1
        else:
            self.num_of_lives-=1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_of_lives} lives left.")
      
    def ask_for_input(self):
        while True:
            guess=input('Please select a letter')
            #check if guess is indeed a letter
            if not (len(guess)==1 and guess.isalpha()):
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
print(game.word_guessed)
# %%
game.ask_for_input()

# %%
