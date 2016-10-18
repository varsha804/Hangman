import urllib2
from urllib2 import urlopen
import requests
from random import randint


print "~The Hangman Game~"

def mainMenu():
	flag = True
	choice = 0
	while flag:

		print "Select an option and then start playing!"
		print "1. You pick the word and the computer will guess"
		print "2. The computer picks a word and you will guess"
		print "3. Categories (type '4' for more information)"
		print "4. Word Bank"
		choice = raw_input("My choice: ")
		if choice == "1" or choice == "2" or choice == "3" or choice == "4" or choice == "5":
			flag = False
		else:
			flag = True
	return choice

def draw(numSpaces, usedArr):
	count = 0
	if numSpaces == []:
		print "Please enter a word which has at least one character"
		return
	unused_letters_1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
	unused_letters_2 = ["J", "K", "L", "M", "N", "O", "P", "Q", "R"]
	unused_letters_3 = ["S", "T", "U", "V", "W", "X", "Y", "Z"]
	used_letters_1 = usedArr
	print "   ______"
	print "   |     |		 Unused Letters:"
	print "   |     |		",
	for char in unused_letters_1:
		print char,
	print "          "
	print "         |		",
	for char in unused_letters_2:
		print char,
	print "          "
	print "         |		",
	for char in unused_letters_3:
		print char,
	print "          "
	print "         |"
	print "         |		 Used Letters:",
	print "          "
	print "         |		",
	for char in used_letters_1:
		print char,
	print "          "
	print "         |		"
	print "  --------------"
	
	print '\n'
	print "  ",
	# while (count < numSpaces):
	# 	print "_ ",
	# 	count = count + 1
	# print '\n'
	for i in numSpaces:
		print i,
	print '\n'

option = mainMenu()
if option == "1":
	print "You pick the word and the computer will guess"
elif option == "2":
	print "2. The computer picks a word and you will guess"
elif option == "3":
	print "3. Categories (type '5' for more information)"
elif option == "5":
	print "So the way this works is that you will choose a \n category from which the computer will generate a \n word for you to guess!"
elif option == "4":
	print "4. Computer picks word from word bank and you will guess"
'''what to do when user guesses a word (in)correctly:
	# rotate letter 180 (is this possible?)
	# remove from list on the side and create a "used letters" or  "wrong/correct
	# letters" lists
'''

if option == "1":
	print "How many letters is the word you're thinking of?"
	num = input("Length: ")
	size = ['_ '] * num
	used_letters = []
	draw(size, used_letters)
if option == "2":
	size = ['_ '] * 5;
	# dummy size
	used_letters = []
	draw(size, used_letters)
	count = size;
	while (count != 0):
		guess = raw_input("What's your guess? ")
if option == "4":
	word_bank = ["caterpillar", "restaurant", "movie", "reindeer", "frog", "piccolo"]
	word = word_bank[randint(0, len(word_bank) - 1)]
	size = ['_ '] * len(word)
	char_list = []
	used_letters = []
	turns = 0
	pressedEnter = False
	draw(size, used_letters)
	# turns is the number of tries the user has until game is over (takes 9 to draw the person)
	while size != char_list and turns < 9:
		guess = raw_input("Guess a letter: ",)
		if guess == word:
			# if user tries to guess the whole word (and she's correct)
			size = char_list
			draw(size, used_letters)
			print "Woah, you got that in only " + str(turns) + " tries!",
		if guess == "":
			# if user just presses enter, it won't count as a turn
			print "Please enter a letter"
			pressedEnter = True
			turns = turns - 1
		if guess.upper() in used_letters:
			# if user has already guessed this letter
			draw(size, used_letters)
			print "You've already guessed this letter (or phrase if you're being cocky :P )!"
			turns = turns - 1
			# this doesn't count as a turn
		
		else:
			# if user guesses a new letter
			print "Your guess: " + guess.upper()
			char_list = list(word)
			used_letters.append(guess.upper())
			position = -1
			exists = False
			# check if letter exists in word
			for char in char_list:
				position += 1
				# for each letter in the word
				if guess == char:
					exists = True
					# if guessed letter matches letter in the word
					size[position] = char
					# update the blank spaces
			if exists == True:
				# if it does exist
				draw(size, used_letters)
				print "Correct!"
			if exists == False and pressedEnter == False:
				# if it does not exist
				draw(size, used_letters)
				print "Wrong!"
		
		turns += 1
		#if word == "" or word
		if (9 - turns) != 1:
			print "You have " + str(9 - turns) + " tries left!"
		else:
			print "You have 1 try left!"
	if size == char_list:
		print "~Nice!~"
	else:
		print "Game Over D:" + '\n' + "The word was '" + word + "'!"

# r = requests.get("https://wordsapiv1.p.mashape.com/words/")
# print "yodel"
# print r.text
