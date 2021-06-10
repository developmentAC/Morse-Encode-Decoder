#!/usr/bin/env python3
""" Program to using generator functions for encoding / decoding text into / from morse code."""


from collections import Counter
import sys, random

DATE = "9 June 2021"
VERSION = "iii"
AUTHOR = "Oliver Bonham-Carter"
AUTHORMAIL = "obonhamcarter@allegheny.edu"
THISPROG = sys.argv[0].replace("./","")
WHATISTHIS_p1 = "\n\tA Morse encoder and decoder program."
WHATISTHIS_p2 = "\tUse option '-h' for more glorification about this amazing project!\n"


# Bold colour list
colour_list =['\033[1;30m',
'\033[1;31m',
'\033[1;32m',
'\033[1;33m',
'\033[1;34m',
'\033[1;35m',
'\033[1;36m',
'\033[1;37m',
'\033[1;90m',
'\033[1;91m',
'\033[1;92m',
'\033[1;93m',
'\033[1;94m',
'\033[1;95m',
'\033[1;96m']

BIYellow = '\033[1;93m'     # Yellow
BIGreen='\033[1;92m'      # Green
BIBlue='\033[1;94m'       # Blue
BICyan='\033[1;96m'       # Cyan
BIRed='\033[1;91m'        # Red
BIWhite='\033[1;97m'      # White
White='\033[0;37m'        # White



banner1_str = """
	███╗   ███╗ ██████╗ ██████╗ ███████╗███████╗
	████╗ ████║██╔═══██╗██╔══██╗██╔════╝██╔════╝
	██╔████╔██║██║   ██║██████╔╝███████╗█████╗
	██║╚██╔╝██║██║   ██║██╔══██╗╚════██║██╔══╝
	██║ ╚═╝ ██║╚██████╔╝██║  ██║███████║███████╗
	╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝
	███████╗███╗   ██╗ ██████╗ ██████╗ ██████╗ ███████╗    ██╗
	██╔════╝████╗  ██║██╔════╝██╔═══██╗██╔══██╗██╔════╝   ██╔╝
	█████╗  ██╔██╗ ██║██║     ██║   ██║██║  ██║█████╗    ██╔╝
	██╔══╝  ██║╚██╗██║██║     ██║   ██║██║  ██║██╔══╝   ██╔╝
	███████╗██║ ╚████║╚██████╗╚██████╔╝██████╔╝███████╗██╔╝
	╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝
	██████╗ ███████╗ ██████╗ ██████╗ ██████╗ ███████╗██████╗
	██╔══██╗██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗
	██║  ██║█████╗  ██║     ██║   ██║██║  ██║█████╗  ██████╔╝
	██║  ██║██╔══╝  ██║     ██║   ██║██║  ██║██╔══╝  ██╔══██╗
	██████╔╝███████╗╚██████╗╚██████╔╝██████╔╝███████╗██║  ██║
	╚═════╝ ╚══════╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝

"""
# banner ref: https://manytools.org/hacker-tools/ascii-banner/


# The dictionary of Morse code. keys = alphabet chars, values = code.
morse_dict = {'A': '.-',     'B': '-...',   'C': '-.-.',
              'D': '-..',    'E': '.',      'F': '..-.',
              'G': '--.',    'H': '....',   'I': '..',
              'J': '.---',   'K': '-.-',    'L': '.-..',
              'M': '--',     'N': '-.',     'O': '---',
              'P': '.--.',   'Q': '--.-',   'R': '.-.',
     	      'S': '...',    'T': '-',      'U': '..-',
              'V': '...-',   'W': '.--',    'X': '-..-',
              'Y': '-.--',   'Z': '--..',
              '0': '-----',  '1': '.----',  '2': '..---',
              '3': '...--',  '4': '....-',  '5': '.....',
              '6': '-....',  '7': '--...',  '8': '---..',
              '9': '----.',  ' ':'/'     ,  '.':'.-.-.-',
              ',':'--..--',  ':':'---...',  '?':'..--..',
              "'":'.----.',  '-':'-....-',  '/':'-..-.',
              '@': '.--.-.', '=':'-...-',   '(':'-.--.',
              ')':'-.--.-',  '+':'.-.-.',   '!':'-.-.--',
              ';':'-.-.-'
        }

def get_platformType():
	"""Function to dermine the OS type."""
	platforms = {
	'darwin' : 'OSX',
	'win32'  : 'Windows',
	'linux1' : 'Linux',
	'linux2' : 'Linux'}
	if sys.platform not in platforms:
		return sys.platform
	return platforms[sys.platform]
#end of get_platformType()

def printWithColour(colCode_str, myMessage_str):
	"""A function to print with colour for Unix and MacOS."""
	platform_str = get_platformType()
	if platform_str.lower() == "linux" or platform_str.lower() == "osx":
		myMessage_str = colCode_str + myMessage_str + BIWhite
		# print(colCode_str + myMessage_str + BIWhite)
	else: # Windows does not seem to like these colourcodes
		# print(myMessage_str)
		pass
	return myMessage_str
# end of printWithColour()


def bannerScreen(myCount_int):
	"""prints a charming and colourful little message for the user"""
	# report the perceived OS type
	platform_str = get_platformType()

	if platform_str.lower() == "linux" or platform_str.lower() == "osx":
		for i in range(myCount_int):
			randomColour_str = random.choice(colour_list) # choose a random colour to display the title screen.
			print(randomColour_str + banner1_str + BIWhite)
	else:
		print(banner1_str)
#end of bannerScreen()

def helper():
	"""Cheap online help; how to use the program"""
	bannerScreen(1) # print up one banner screen
	print(WHATISTHIS_p1)
	h_str1 = "\t"+DATE+" | version: "+VERSION
	h_str2 = "\t"+AUTHOR +"\n\tmail: "+AUTHORMAIL
	print("\t"+len(h_str2) * "-")
	print(h_str1)
	print("\t"+len(h_str2) * "-")
	print(h_str2)
	print("\t"+len(h_str2) * "-")
	print(f"\t [+] \U0001f600  USAGE: {THISPROG}")
	print(f"\n\t [+] For example:\n\t $ python3 {THISPROG}")
	print("\n\t [+] You will then be asked to enter your message to convert to Morse code")
	print("\t     or you can enter your encoded message to convert back into text.\n\t     Wonderful, right!?")

#end of helper()


def myMorseEncoder(msg_str):
	""" function to create a generator to yield each letter in morse code"""

	if len(msg_str) == 0: #nothing to do!
		print("\tNothing to do...")
		exit(1)

#	print("\n\t Encoding ...\n")
	mesg_str = printWithColour(BICyan, "\n\tEncoding ... \n")
	print(mesg_str)

	out_str = ""
	for i in msg_str:
		try:

			tmp1_str = printWithColour(BIGreen, f"\t {i}")
			tmp2_str = printWithColour(BIRed, "->")
			tmp3_str = printWithColour(BIBlue, f"{morse_dict[i.upper()]}")
			print(f"{tmp1_str} {tmp2_str} {tmp3_str}")

			out_str = out_str + morse_dict[i.upper()] + " "
		except KeyError:
			print(f"\t [-] Skipping: {i}")
	yield out_str
#end of myMorseEncoder()


def myMorseDecoder(msg_str):
	""" function to decode the morse code into the original text characters"""

	if len(msg_str) == 0: #nothing to do!
		print("\tNothing to do...")
		exit(1)
	mesg_str = printWithColour(BICyan, "\n\tDecoding ... \n")
	print(mesg_str)

	msg_list = msg_str.split() # make a list from the string. seperate by spaces
	out_str = "" # build the text string on this
	for i in msg_list:
		for letter in morse_dict:
			if morse_dict[letter] == i: # is this a char of Morse code?

				tmp1_str = printWithColour(BIBlue, f"\t{morse_dict[letter]}")
				tmp2_str = printWithColour(BIRed, "->")
				tmp3_str = printWithColour(BIGreen, f"{letter}")
				print(f"{tmp1_str} {tmp2_str} {tmp3_str}")

				out_str += letter
	yield out_str
#end of myMorseDecoder()


def isMorseCode(in_str):
	""" Function to determine whether the input is code or text"""
	# Are the only chars in text from Morse code?
	if len(Counter(in_str)) <= 4 and "-" in in_str and "." in in_str or "/" in in_str:
		return True
	else:
		return False
#end isMorseCode()


def begin():
	"""Driver function"""
	msg_str = input('\tInput your message (either in text or in Morse code) : ')
	out_str = ""
	if isMorseCode(msg_str) != True:

		out_str = myMorseEncoder(msg_str)

	else: # is morse code

		out_str = myMorseDecoder(msg_str)
	mesg_str = printWithColour(BIYellow, "\n\tYour Message: ")
	print(mesg_str,next(out_str))

#end of begin()


def getArguments(argv_list):
	""" A function to determine what parameters have been entered"""
	for i in range(len(argv_list)):
		argv_list[i] = argv_list[i].upper()

	if "-H"  in argv_list:
		helper()
	else:
		print(WHATISTHIS_p1)
		print(WHATISTHIS_p2)
		begin()



if __name__ == '__main__':
	getArguments(sys.argv[1:])
