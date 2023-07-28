#hangman
import random

word_list = ["cancion", "papa", "roto", "computadora", "marciano"]
chk = 0
##selection of word and set size
seed = random.randint(0,(len(word_list)-1))
word = word_list[seed]
#print("word:",word)
word_len = len(word)

#print hangman init

print(f"The word length is {word_len}")
print('_ '*word_len)
letter = input("please select a letter: ")


## Check input it only a letter and transform to lowercase.
while chk == 0:
    if len(letter) == 1: 
      lenght = True
      if letter.islower() and letter.isalpha() == True:
        chk = 1
      else: letter = input("please insert a lowercase or letter: ")
    else: letter = input("please just one a letter: ")

    
## Check letter on a word in order to play

spell = list(word)
 
print(spell)
