#!/usr/bin/env python
# -*- coding: utf-8 -*-
#title		:cmdmenu.py
#description	:This program displays an interactive menu for accessing command inputs
#author		:
#date		:
#version	:0.1.0
#usage		:python cmdmenu.py
#notes		:
#python_version	:

# import modules
import sys, os

#Main definition
menu_actions = {}

#Main menu
def main_menu():
	os.system('clear')

	print "Welcome, \n"
	print "What command would you like to use?"
	print "1. Navigate"
	print "2. See processes"
	print "3. Compile a file"
	print "\n0. Quit"

	choice = raw_input(" >> ")
	exec_menu(choice)

	return

#Execute menu
def exec_menu(choice):
	os.system('clear')
	ch = choice.lower()
	if ch == '':
		menu_actions['main_menu']()
	else:
		try:
			menu_actions[ch]()
		except KeyError:
			print "Invalid selection, please try again. \n"
			menu_actions['main_menu']()
	return

# Navigate
def navigate():
	sys.exit()

# See processes
def processes():
	sys.exit()

# Compile
def compile():
	sys.exit()

# Quit
def exit():
	sys.exit()

# Menu definition
menu_actions = {
	'main_menu': main_menu,
	'1': navigate,
	'2': processes,
	'3': compile,
	'0': exit,
}

# Main Program
if __name__ == "__main__":
	# Launch main menu
	main_menu()
