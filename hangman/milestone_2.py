#%%
import random

my_fav_fruit=['apple', 'pear', 'nectarine', 'peach', 'pineapple']
print(my_fav_fruit)

fruit=random.choice(my_fav_fruit)
print(fruit)
# %%
#The following code takes an input from the user and verifies if it is a single letter
user_input=input('Please choose a single letter')
if len(user_input)==1 and user_input.isalpha():
    print('Goog guess!')
    user_letter=user_input
else:
    print("Oops! That is not a valid input.")


# %%
