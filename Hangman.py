import random
import time

L = ['dog', 'horse', 'falcon', 'anagram']
Word = list(random.choice(L))
H_Word = '_'*len(Word) #displays hidden word

guesses = ''

# Welcome player
name = input('Hello, what is your name? ')

# pauses
time.sleep(1)

print("Hello " + str(name) + ". Let's play Hangman!")

time.sleep(1.3)

print(H_Word)

time.sleep(1.3)

turns = 10

# make counters for letters
# and make a new hollow word
W = enumerate(Word)
new_Word = list('_' * len(Word))


# add guess to the new_Word
def change():
    for (counter, value) in W:
        if value == guess:
            new_Word[counter] = str(guess)


# while loop of the game
while new_Word != Word:
    guess = input("Take a guess: ").lower()
    if guess in Word:
        change()
        print(new_Word)
    else:
        print('Wrong')