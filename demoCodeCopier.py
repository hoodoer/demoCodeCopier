#!/bin/python
#
#
# Simple script to copy blocks of code (e.g. functions)
# to the clip board when a number is entered (1, 2, 3)
# For demos where I'm building up code over time
# This script will copy the right code into the clipboard
# when I need it with minimal distrction from the talk
#
# This will put the code into the middle mouse button past
# buffer
#
# Drew Kirkpatrick
# drew.kirkpatrick@gmail.com
# @hoodoer
#

import os



def copyToClipboard(code):
	f = open("./tempFile.txt", "w+")

	f.write(code)
	f.close()

	cmd = "xclip -i ./tempFile.txt"
	os.system(cmd)


# First step in my demo, first 
# code I want to copy into my demo code
def one():
	code = """
	This is some
	Bit of multline
	code
	like so
	"""

	copyToClipboard(code)

	return "First code copied"

def two():
	return "Dos ahahahahaha"

def gimmeOuttaHere():
	exit()
	


def handleInput(input):
	switcher = {
        1: one,
        2: two,
        exit: gimmeOuttaHere,
        quit: gimmeOuttaHere
	}

	# Get the function from switcher dictionary
	func = switcher.get(input, lambda: "Invalid Input")
    # Execute the function
	print func()


def main():
	print "Starting demo code clipboard helper..."


	while True:
		userInput = input("Code to serve up in clipboard: ")
		handleInput(userInput)
		


if __name__ == "__main__":
    main()
