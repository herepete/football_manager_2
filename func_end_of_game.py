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
        userinput= input("You have reached the end of the game (if you want to conintnue edit func_other_game_settings.py and change the seasonstoplay variable , then rerun the game loading the previous saved file)\n")
        print ("Thank you and good bye")
        break

if __name__ == "__main__":
    print ("***Script Called Directley****")
    season=99
    game=99
    defscore=99
    atascore=99
    squad=99
    endofgame(season, game, defscore, atascore, squad)
