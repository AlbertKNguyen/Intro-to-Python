#########################################################
# CIS 117 Python Programming: Lab 2                     #
#                                                       #
# Loops, Functions, Password Verification               #
#                                                       #
#########################################################
import re
min_size = 8
max_size = 16
def validChecker(pass1, pass2):#method checking for requirements of the password inputs
    error = False
    if len(pass1) < min_size or len(pass1) > max_size:
        print("The password must be between 8 to 16 characters long.")
        error = True
    if not re.search("[a-z]", pass1):
        print("The password must contain at least 1 lowercase letter.")
        error = True
    if not re.search("[0-9]", pass1):
        print("The password must contain at least 1 digit.")
        error = True
    if not re.search("[A-Z]", pass1):
        print("The password must contain at least 1 uppercase letter.")
        error = True
    if not pass1 == pass2:
        print("The passwords do not match.")
        error = True
    if error:#prints all of the error statements that apply along with the following "try again" statement
        print("This password will not work. Please try again.\n")
        return False
    else:#if no error, prints the "will work" statement and returns true, ending program
        print("This password will work.")
        return True


valid = False
while not valid:#loop referring to validchecker method
    password = input("Enter your password: ")
    passwordTwo = input("Re-enter your password: ")

    valid = validChecker(password, passwordTwo)

#Enter your password: passw
#Re-enter your password: passw
#The password must be between 8 to 16 characters long.
#The password must contain at least 1 digit.
#The password must contain at least 1 uppercase letter.
#This password will not work. Please try again.
#
#Enter your password: password
#Re-enter your password: password
#The password must contain at least 1 digit.
#The password must contain at least 1 uppercase letter.
#This password will not work. Please try again.
#
#Enter your password: Password
#Re-enter your password: Password
#The password must contain at least 1 digit.
#This password will not work. Please try again.
#
#Enter your password: Password1
#Re-enter your password: Password2
#The passwords do not match.
#This password will not work. Please try again.
#
#Enter your password: Password1
#Re-enter your password: Password1
#This password will work.
        
   
