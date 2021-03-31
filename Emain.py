# This project allows you to print how man emails are there in the terminal
# in the Format of [There are (xyz) emails in the inbox]

# Import Modules
import POP3Config # Module that handles all the config!
import email
import poplib
from poplib import POP3
from getpass import getpass

# Inputs
print("Outlook or Gmail")
server = input("Enter Desired Service: ")

# --Connect to user's choice of POP Server-- #
# All of the work is done by the Module, we just import and execute it

#Outlook
if server == "Outlook":
    from POP3Config import outlook
    outlook()

elif server == "GMail":
    from POP3Config import gmail
    gmail()
# End Connection and give me Credit >:)
import poplib
from POP3Config import DevMark
poplib.POP3.quit
DevMark()
