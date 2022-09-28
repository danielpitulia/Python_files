#!/usr/bin/env python3
# Short hangman game to run in terminal

import random
import re

list_of_words = ["greyhound", "goldenretriever", "bordercollie", "dalmatian", "jackrussel","terrier", "dachshund"]
count_fail = 0

hangman = [
    "\t O\t\t##",
    "\t\|/\t\t##",
    "\t | \t\t##",
    "\t/ \ \t\t##",
]

hang_pole = [
    "###########################",
    "\t #\t\t##",
    "\t\t\t##",
    "\t\t\t##",
    "\t\t\t##",
    "\t\t\t##",
    "\t\t\t##",
    "\t\t\t##",
    "\t\t\t##",
]
# Randomly choose a word from the list of alternatives
answer = list_of_words[random.randrange(0,len(list_of_words))]
answer_remaining = list(answer)		# List of characters in answer

# Define progress line: for example, the progress line is " _ _ _ _ _" if the word has 5 characters

progress = "_"*len(answer)
progress = list(progress)

print("Welcome to Hangman dog edition")
for line in hang_pole:
    print(line)

print("Try to guess the correct dog breed: ")
print("".join(progress), "\nHint: the breed can be two words put together without a space. Try to guess matching characters. If you guess the wrong character 10 times you lose.")

def find_matches(guess, answer):
    """ Search guess in answer using re.finditer, find indexes"""

    indx_matches = []
    matches = re.finditer(guess, answer)

    for m in matches:
        indx_matches.append(m.span()[0]) # Store index of match from m.span()[0]
    return indx_matches

while "_" in progress:
    guess = input()
    if guess in answer:
        indx = find_matches(guess, answer)
        for i in indx:
            answer_remaining[i] = ""
            progress[i] = guess

        for line in hang_pole:
            print(line)
        print("Correct guess: " + "".join(progress))
    else:
        count_fail +=1
        hang_pole[count_fail+1] = hangman[count_fail-1]

        for line in hang_pole:
            print(line)
        print("Wrong: " + guess + "\n" + "Times failed: " + str(count_fail) + "\n" + "Progress = " + "".join(progress))

    if(count_fail > 9):
        print("Sorry, you're dead :(")
        print("Enter any character to exit game")
        input()
        break
print("Well done! The correct dog breed is " + answer)
print("Enter any character to exit game")
input()
