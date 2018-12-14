#########################################################
# CIS 117 Python Programming: Lab 3                     #
#                                                       #
# User input, string, lists, conversion, for loops      #
#                                                       #
#########################################################

# list of the month string names
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
# constant to control for loop for test run
NUMBER_OF_TESTS = 5
for tests in range (NUMBER_OF_TESTS):
    # prompts user to enter date
    date = input("\nEnter a date (mm/dd/yyyy): ")
    # splits the date string into a list of 3 items 
    date = date.split('/')
    # converts, formats, and prints the date
    print("\nThe converted date is: {month} {day}, {year}\n"
    .format(month=months[int(date[0])-1], day=date[1],year=date[2]))

##########RUN TESTS
#
# Enter a date (mm/dd/yyyy): 07/29/1998
#
# The converted date is: July 29, 1998
#
##########
#
# Enter a date (mm/dd/yyyy): 12/25/1976
#
# The converted date is: December 25, 1976
#
##########
#
# Enter a date (mm/dd/yyyy): 10/31/2015
#
# The converted date is: October 31, 2015
#
##########
#
# Enter a date (mm/dd/yyyy): 7/11/2017
#
# The converted date is: July 11, 2017
#
##########
#
# Enter a date (mm/dd/yyyy): 09/01/1998
#
# The converted date is: September 01, 1998
#
##########