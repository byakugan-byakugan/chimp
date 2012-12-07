################################################
#Chi, the CSS and HTML Inspector
#
#Written by Carlos Bautista
#December 6, 2012
################################################

import sys
import re

def isInTokens(prop):
	for i in lstTokens:
		if prop == i:
			return 1
	return 0

def removeValues(list, value):
	return [val for val in list if val != value]

def cleanStrings(lst):
	for i in range(0, len(lst)):
		lst[i] = lst[i].replace(" ", "")
		lst[i] = lst[i].replace(":", "")

def printError(n):
		print("\033[1m\033[91merror found in: ")
		print("****************************[\033[0m")
		print(n)
		print("\033[1m\033[91m****************************]\033[0m")
		print('\n')

def printAll(lst, tCheck):	
	if tCheck == 1:
		for i in lst:
			if not isInTokens(i):
				printError(i)
	else:
		for i in lst:
			printError(i)

#Open target file and the token library
targetFile = open(sys.argv[1],'r')
targetFile = targetFile.read()
tokenLibrary = open('words.txt','r')
tokenLibrary = tokenLibrary.read()


#Compiles all regexes
#regSelectorGroups = re.compile('[a-zA-Z0-9.#]+ *\{[^}]*\}')
regProperties = re.compile('[a-z-]*:')
regTokens = re.compile('[a-z-]* +')
regBrackets = re.compile('[a-zA-z0-9*.-]* *\{[^}]*\{')
regColons = re.compile(':[^;]*:')
regAngles = re.compile('<[^>]*<[^>]*>')

#Creates lists using the compiled regexes and the target file
#lstSelectorGroups = re.findall(regSelectorGroups, targetFile)
lstProperties = removeValues((re.findall(regProperties, targetFile)),'')
lstTokens = re.findall(regTokens, tokenLibrary)
lstBrackets = re.findall(regBrackets, targetFile)
lstColons = re.findall(regColons, targetFile)
lstAngles = re.findall(regAngles, targetFile)

#sanitizes strings
cleanStrings(lstProperties)
cleanStrings(lstTokens)

printAll(lstProperties, 1)
printAll(lstBrackets, 0)
printAll(lstColons, 0)
printAll(lstAngles, 0)