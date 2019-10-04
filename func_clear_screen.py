#!/usr/bin/python3.6
#this is called so much i am creating a function for it
# it also makes it easier to make tweaks to itvi 
import os

def clear_screen():
    a=os.name
    if a == "posix":
        os.system('clear')
    else:
        os.system('cls')
        

