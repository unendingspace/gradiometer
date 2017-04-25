# tools for processing user inputs

from os import system
from time import time
from datetime import datetime

def ynPrompt(text):
	usr = raw_input(text + " (y/n) ")
	usr = usr.lower()
	if (usr == 'y' or usr == 'yes'):
		return 1
	elif (usr == 'n' or usr == 'no'):
		return 0
	else:
		print "Invalid input; please try again"
		print 
		return ynPrompt(text)

def getRootName(filename):
	slash = -1
	for i in range(0, len(filename)):
		if filename[i] == '/':
			slash = i
	return filename[slash+1:]

def sendFilesToCluster(filelist, runstuff):

	print "To save files, you need a UCN cluser login."
	if not ynPrompt("Do you have a username and password ready?"):
		return 1

	username = ''

	while username == '':
		tmp = raw_input("Please enter your UCN cluster username: ")
		print
		print "Username:", tmp
		print
		if ynPrompt("Is this correct? "):
			username = tmp
		else:
			print

	timestamp = datetime.fromtimestamp(time()).strftime('%H.%M-%d.%m.%Y')

	files = ' '.join(filelist)
	dest = username + "@khione.triumf.ca:/ucnscr/" + username + "/gradiodata/" + timestamp + "/"

        extra = ''

        if ynPrompt('Would you like to append anything to the destination folder name?'): 
		while extra == '':
			print
			temp = raw_input('What would you like to add? ')
			for i in range(0, len(temp)):
				if temp.isalnum():
					extra = temp
				else:
					print
					print "Sorry, alphanumeric characters only"
		dest = dest[:-1] + extra + '/'

	print
	print "Sending files to", dest
	print
	print "You will have to enter your password several times."
	print

	if runstuff:
		system('ssh ' + username + '@khione.triumf.ca \'mkdir -p /ucnscr/' + username + '/gradiodata/' + timestamp + extra + '\'')

	for item in filelist:
		system('scp ' + item + ' ' + dest)
