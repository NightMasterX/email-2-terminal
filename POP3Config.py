"""Automatically add POP servers and no need to browse the web for the POP config, also allows you to connect 
and manage without needing to add more code! Made by NightMX in the search of clean code and easy management."""
import poplib
import getpass
from getpass import getpass
from poplib import POP3

# Servers
outlookpop = "outlook.office365.com"
outlookport = 995

# Outlook
def outlook():
    """Connects to the Outlook Server using POP3"""
    try:
        hostmail = input("Please enter desired email: ")
        hostpass = getpass("Please enter the Password: ") # Invisible Login
        Connect = poplib.POP3_SSL(outlookpop, outlookport)
        Connect.user(hostmail)
        Connect.pass_(hostpass)
        num_mess = len(Connect.list()[1])
        print("Total Emails in Inbox: %s" %num_mess)
    except poplib.error_proto:
        print("Bad Auth, wrong password or email.")

# GMail
def gmail():
    """Connects to Gmail Servers using POP3"""
    print("Coming Soon...")

# Developer Mark
def DevMark():
    """Makes NightMX Happy by giving Credits :)"""
    print("Made by NightMX!")
