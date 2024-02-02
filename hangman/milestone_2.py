#%%
import random

word_list=['apple', 'pear', 'nectarine', 'peach', 'pineapple']
print(word_list)
# %%
word=random.choice(word_list)
# %%
print(word)
# %%
temp=input('Please choose a single letter')
if len(temp)==1 and temp.isalpha():
    print('Goog guess!')
    guess=temp
else:
    print("Oops! That is not a valid input.")
# %%
guess
# %%
