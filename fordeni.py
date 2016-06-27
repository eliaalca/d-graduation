# DENIS GRADUATION PRESENT  CLUES
# general variables and functions
import time
import sys

string = "Hallo"
def write_slow (string):
	for letter in string:
		sys.stdout.write(letter)
		time.sleep(0.1)
	print " "
	
buhal = "Denis"
monkey = "Elia"
def beg(buhal,monkey):
	string = "Denis kisses Elia for clues =D"
	c_string = string.replace("Denis", color.GREEN+"Denis"+color.END).replace
	write_slow(string)
	
	
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'	

 
# START CODE

s = """Welcome to the Treasure Hunt Program! Answer the questions with "yes", "no" or "maybe" unless when asked otherwise. Good luck!!!""" 
b_s = s.replace("Treasure Hunt Program!", color.BOLD + color.UNDERLINE + color.PURPLE + "Treasure Hunt Program!" + color.END).replace("Good luck!!!", color.CYAN + color.BOLD +"Good luck!!!"+color.END)
write_slow (b_s)

for n in (5,4,3,2,1):
	S_number = str(n)
	number = S_number + "..."
	print number
	time.sleep(0.8)
print "Go!"


while True:
	Q = raw_input("Do you have any idea of what to do next?")
	if Q == "yes":
		string = "Well done, let's continue then!"
		write_slow(string)
		break
	elif Q == "maybe":
		beg(buhal,monkey)
		continue
	elif Q == "kissdone":
		string = "Numbers are not always numbers and order is not always followed. Mainly because some things are and some things are not."
		write_slow (string)
	else:
		string = "Monkey is sad because buhal misses imagination... revise the codes and have some positive thoughts."
		write_slow (string)
		
while True:
	present = raw_input("Where is the present?")
	if present == "suitcase":
		string = "Exactly! Go and open it."
		write_slow (string)
		break
	else:
		string = "Maybe you should review your notes again..."
		write_slow (string)
		
while True:
	Suitcase = raw_input ("Do you know how to to open it?")
	if Suitcase == "no":
		string = "Maybe a mirror would help you..."
		write_slow (string)
		break
	elif Suitcase == "maybe":
		beg(buhal,monkey)
		continue
	else:
		string = "Don't lie... or don't you dare breaking my lock!"
		write_slow (string)

print " "
string = "And sadly, this is the end of this amazing useful programm =)"
write_slow (string)