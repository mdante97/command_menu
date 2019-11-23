#!/usr/bin/env python
# -*- coding: utf-8 -*-
#title		:cmdmenu.py
#description	:This program displays an interactive menu for accessing command inputs
#author		:
#date		:
#version	:1.0.0
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

	print "What type of command would you like to use?"
	print "1. User management"
	print "2. File management"
	print "3. System Security"
	print "4. Program management"
	print "5. Process management"
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

#User management menu
def user_menu(choice):
	os.system('clear')
	ch = choice.lower()
	if ch == '':
		User_Menu['User_Menu']()
	else:
		try:
			User_Menu[ch]()
		except KeyError:
			print "Invalid selection, please try again. \n"
			User_Menu['User_Menu']()
	return

#User management menu
def file_menu(choice):
	os.system('clear')
	ch = choice.lower()
	if ch == '':
		File_Menu['File_Menu']()
	else:
		try:
			File_Menu[ch]()
		except KeyError:
			print "Invalid selection, please try again. \n"
			File_Menu['File_Menu']()
	return


#security menu
def security_menu(choice):
	os.system('clear')
	ch = choice.lower()
	if ch == '':
		Security_Menu['Security_Menu']()
	else:
		try:
			Security_Menu[ch]()
		except KeyError:
			print "Invalid selection, please try again. \n"
			Security_Menu['Security_Menu']()
	return

#program menu
def program_menu(choice):
	os.system('clear')
	print "we're here"
	ch = choice.lower()
	if ch == '':
		Program_Menu['Program_Menu']()
	else:
		try:
			Program_Menu[ch]()
		except KeyError:
			print "Invalid selection, please try again. \n"
			Program_Menu['Program_Menu']()
	return

#process menu
def process_menu(choice):
	os.system('clear')
	ch = choice.lower()
	if ch == '':
		Process_Menu['Process_Menu']()
	else:
		try:
			Process_Menu[ch]()
		except KeyError:
			print "Invalid selection, please try again. \n"
			Process_Menu['Process_Menu']()
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


# Show directory
def show():
	os.system("ls")
	sys.exit()
# User management menu
def User_Management():
	print "User Management"
	print "What action would you like to do?"
	print "1.  Add user"
	print "2.  Remove User"
	print "3.  Find info about user"
	print "4.  See which users are on the system"
	print "\n0.  Back"
	choice = raw_input (" >> ")
	user_menu(choice)

# File management
def File_Management():
	print "File Managment"
	print "What action would you like to do?"
	print "1.  Add Directory"
	print "2.  Remove Directory"
	print "3.  Mount Directory"
	print "4.  Unmount Directory"
	print "\n0.  Back"
	choice = raw_input (" >> ")
	file_menu(choice)

# System security
def Security_Management():
	print "Security menu"
	print "What action would you like to do?"
	print "1. Lock User's account"
	print "2. Unlock User's account"
	print "3. Find User Information"
	print "4. Change File Permissions"
	print "\n0. back"
	choice = raw_input (" >> ")
	security_menu(choice)

# program management
def Program_Management():
	print "Program Menu"
	print "What action would you like to do?"
	print "1. Install application"
	print "2. Update application"
	print "3. Upgrade application"
	print "4. Compile C Program"
	print "\n0. Back"
	choice = raw_input (" >> ")
	program_menu(choice)

# process management
def Process_Management():
	print "Process Menu"
	print "What action would you like to do?"
	print "1. Show Processes"
	print "2. Stop Process"
	print "3. Start Process"
	print "\n0. Back"
	choice = raw_input (" >> ")
	process_menu(choice)


# User Management Functions
# Add User
def Add_User():
	print "What is the name of the user that you would like to add?"
	choice = raw_input (" >> ")
	os.system("sudo useradd " + choice)

# Remove User
def Rem_User():
	print "What is the name of the user that you would like to remove?"
	choice = raw_input (" >> ")
	os.system("sudo userdel " + choice)

# Find information on user
def User_Info():
	print "What is the name of the user that you would like to know more about?"
	choice = raw_input (" >> ")
	os.system("finger " + choice)

#find users on system	
def Who_is():
	print "Here are the users on the system"
	os.system("who")


# File Managment Functions
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

#mount directory
def mount_direc():
	print "Give the name of the directory you would like to mount to the filesystem"
	mount_choice = raw_input (" >> ")
	print "Give the name of where you would like to mount the directory to"
	print "Please note that this must be an existing directory"
	mount_location = raw_input (" >> ")
	os.system("mount " + mount_choice + " " + mount_location)

#unmount directory
def unmount_direc():
	print "Give the name of the directory you would like to unmount"
	choice = raw_input (" >> ")
	os.system("unmount " + choice)
# Security Management Functions
# Lock User Account
def user_lock():
	print "Give the name of the user account to lock"
	choice = raw_input (" >> ")
	os.system("Usermod -L " + choice)

# Unlock User Account
def user_unlock():
	print "Give the name of the user account to unlock"
	choice = raw_input (" >> ")
	os.system("Usermod -U " + choice)

# Change File Permissions
def file_permissions():
	print "Give the name of the file to change permissions"
	filename = raw_input (" >> ")
	print "Please answer the following questions with 1 or 0"
	print "Would you like the file owner to be able to read the file?"
	choice = int(input())*400
	print "Would you like the file owner to be able to write the file?"
	choice = choice+int(input())*200
	print "Would you like the file owner to be able to execute the file?"
	choice = choice+int(input())*100
	print "Would you like the owner's group to be able to read the file?"
	choice = choice+int(input())*40
	print "Would you like the owner's group to be able to write to the file?"
	choice = choice+int(input())*20
	print "Would you like the owner's group to be able to execute the file?"
	choice = choice+int(input())*10
	print "Would you like everyone to be able to read the file?"
	choice = choice+int(input())*4
	print "Would you like everyone to be able to write to the file?"
	choice = choice+int(input())*2
	print "Would you like everyone to be able to execute the file?"
	choice = choice+int(input())*1
	print ("The choice is |"+str(choice)+"|")
	print ("The filename is |"+filename+"|")
	os.system("chmod 0" + str(choice) + " " + filename)
	
# Program Management Functions
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

# Compile
def compile():
	print "Type the name of a file you would like to compile."
	print "The file name must end in .c."
	print "To execute the file, type ./a.out then press enter"
	choice = raw_input(" >> ")
	os.system("gcc " + choice)



# Process Management Functions
# Real Time
def real():
	os.system("top")
	sys.exit()

# Snapshot
def snap():
	os.system("ps")
	sys.exit()

# Stop Process
def Stop_Process():
	print "Name the process to be stopped"
	choice = raw_input (" >> ")
	os.system("sudo systemctl stop " + choice)
	
# Start Process
def Start_Process():
	print "Name the process to be started"
	choice = raw_input (" >> ")
	os.system("sudo systemctl start " + choice)

# Misc. Functions
# Quit
def exit():
	sys.exit()

# Back
def back():
	menu_actions['main_menu']()

# Menu definition
menu_actions = {
	'main_menu': main_menu,
	'1': User_Management,
	'2': File_Management,
	'3': Security_Management,
	'4': Program_Management,
	'5': Process_Management,
	'0': exit,
}

# User Menu definition
User_Menu = {
	'main_menu': main_menu,
	'1': Add_User,
	'2': Rem_User,
	'3': User_Info,
	'4': Who_is,
	'0': back,
}

# File menu definition
File_Menu = {
	'main_menu': main_menu,
	'1': make_direc,
	'2': remove_direc,
	'3': mount_direc,
	'4': unmount_direc,
	'0': back,
}

# Security_Menu
Security_Menu = {
	'main_menu': main_menu,
	'1': user_lock,
	'2': user_unlock,
	'3': User_Info,
	'4': file_permissions,
	'0': back,
}
# Program menu
Program_Menu = {
	'main_menu': main_menu,
	'1': ins_app,
	'2': updater,
	'3': upgrader,
	'4': compile,
	'0': back,
}
# Process menu
Process_Menu = {
	'main_menu': main_menu,
	'1': processes,
	'2': Stop_Process,
	'3': Start_Process,
	'0': back,
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
