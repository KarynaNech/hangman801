#%%
import random

#define the list of words to use for the game and picka random one of them
words=['apple', 'pear', 'nectarine', 'peach', 'pineapple']
word=random.choice(words)
#%%
def check_guess(guess):
    #this function checks if a variable guess is present in the word defined above
    guess=guess.lower()
    if guess in word:
        print(f'Good guess! {guess} is in the word.')
    else:
        print(f"Sorry, {guess} is not in the word. Try again." )

# %%
def round_of_hangman():
    #this function iterates iuser input until it's a single letter and then checks if it is in the word
    while True:
        guess=input('Please select a letter')
        #check if guess is indeed a letter
        if len(guess)==1 and guess.isalpha():
            break
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')
    check_guess(guess)

# %%
round_of_hangman()
# %%
