#########################################################
# CIS 117 Python Programming: Lab 4                     #
#                                                       #
# Classes, Constructor, Methods                         #
#                                                       #
#########################################################

class Message: 
    def __init__(self, sender, recipient): #constructor to initialize instance variables
        self.sender = sender
        self.recipient = recipient
        self.line = "\n"
    def append(self, line): # method that adds message to body of text adds new line character after each message line
        self.line += line + "\n"*2
    def toString(self): # returns entire message string
        return "From: {}\n\nTo: {}\n{}\n".format(self.sender, self.recipient, self.line)

#############
#From: Albert
#
#To: Santa
#
#For Christmas, I would like:
#
#A duck plushie
#
#Chicken Skewers
#
#The winning lottery ticket
#
#############