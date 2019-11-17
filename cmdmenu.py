#!/usr/bin/env python
# -*- coding: utf-8 -*-
#title		:cmdmenu.py
#description	:This program displays an interactive menu for accessing command inputs
#author		:
#date		:
#version	:0.7.0
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

	print "What command would you like to use?"
	print "1. Navigate"
	print "2. See processes"
	print "3. Compile a file"
	print "4. See current directory"
	print "5. Make a directory"
	print "6. Remove a directory"
	print "7. Install an application"
	print "8. Check an application for updates"
	print "9. Upgrade an application"
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
	print "Would you like results in real time or a snapshot?"
	print "1. Real Time (Press Control and C keys to exit command)"
	print "2. Snapshot"
	print "0. Back to menu"

	choice = raw_input(" >> ")
	exec_deci(choice)

	return

# Execute Choice
def exec_deci(choice):
	os.system("clear")
	ch = choice.lower()
	if ch == '':
		choic_actions['decisions']()
	else:
		try:
			choic_actions[ch]()
		except KeyError:
			print "Invalid selection, please try again. \n"
			choic_actions['decisions']()
	return

# Real Time
def real():
	os.system("top")
	sys.exit()

# Snapshot
def snap():
	os.system("ps")
	sys.exit()

# Back
def back():
	menu_actions['main_menu']()

# Compile
def compile():
	print "Type the name of a file you would like to compile."
	print "The file name must end in .c."
	print "To execute the file, type ./a.out then press enter"
	choice = raw_input(" >> ")
	os.system("gcc " + choice)

# Show directory
def show():
	os.system("ls")
	sys.exit()

# Make directory
def make_direc():
	print "What would you like to name the directory?"
	choice = raw_input(" >> ")
	os.system("mkdir " + choice)

# Remove directory
def remove_direc():
	print "Give the name of the directory you want to remove"
	choice = raw_input(" >> ")
	os.system("rmdir " + choice)

# Install application
def ins_app():
	print "Give the name of the library you would like to install?"
	print "(You will need to provide your password to install it later)"
	choice = raw_input(" >> ")
	os.system("sudo apt install " + choice)

# Updates
def updater():
	print "Which library do you want to check for updates?"
	choice = raw_input(" >> ")
	os.system("sudo apt update " + choice)

# Upgrade
def upgrader():
	print "Which library do you want to update?"
	choice = raw_input(" >> ")
	os.system("sudo apt upgrade " + choice)

# Quit
def exit():
	sys.exit()

# Menu definition
menu_actions = {
	'main_menu': main_menu,
	'1': navigate,
	'2': processes,
	'3': compile,
	'4': show,
	'5': make_direc,
	'6': remove_direc,
	'7': ins_app,
	'8': updater,
	'9': upgrader,
	'0': exit,
}

#Choice defintion
choic_actions = {
	'decisions': processes,
	'1': real,
	'2': snap,
	'0': back,
}

# Main Program
if __name__ == "__main__":
	# Launch main menu
	main_menu()
