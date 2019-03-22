#!/usr/bin/python3
import func_other_header
import func_other_menu
import os
'''
<explain input>
<what happens>
<error checking>
'''


def endofgame(season, game, defscore, atascore, squad):

    while True:
        os.system('clear')
        func_other_header.header(status="eg", season=season, game=game,
                       defscore=defscore, atascore=atascore)
        userinput= input("Press enter to continue or m for menu\n")
        if userinput=="m":
            func_other_menu.menu(oursquad=squad, formation=1442, printoutput="y")
        else:
            break

if __name__ == "__main__":
    print ("***Script Called Directley****")
