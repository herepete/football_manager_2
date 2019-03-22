#!/usr/bin/python3
# print header you see at the top of each page
# it uses termcolor to display which status we are at

# this is a ugly hack because pip3.7 is not happy at life
import sys
import os
sys.path.append('/usr/lib/python3.6/site-packages/')
from termcolor import colored


def header(status, season, game, defscore, atascore):

    """This function allows same basic info to be passed in & at the top of the screen you will see a status, its really to imrpove visiability,acceptable inputs of status are: 
        i=Intro
        s=Season
        p=Playoff's
        est=End of Season -Training
        esd=End of Season -Draft
        eg=End of game
    season,game,defscore,atascore are expected to be ints but can are dealt with as strings
"""

    if status == "i":
        os.system('clear')
        print(colored('Intro', 'red'), colored('>>>', 'white'), colored('Season', 'white'), colored('>>>', 'white'), colored("Play Off's", 'white'), colored('>>>', 'white'), colored('End of Season -Training', 'white'),colored('>>>', 'white'),colored('End of Season -Draft', 'white'),colored('>>>','white'),colored('End of game', 'white'))

    elif status == "s":
        print(colored('Intro', 'white'), colored('>>>', 'white'), colored('Season', 'red'), colored('>>>', 'white'), colored("Play Off's", 'white'), colored('>>>', 'white'), colored('End of Season -Training', 'white'),colored('>>>', 'white'),colored('End of Season -Draft', 'white'),colored('>>>','white'),colored('End of game', 'white'))

    elif status == "p":
        print(colored('Intro', 'white'), colored('>>>', 'white'), colored('Season', 'white'), colored('>>>', 'white'), colored("Play Off's", 'red'), colored('>>>', 'white'), colored('End of Season -Training', 'white'),colored('>>>', 'white'),colored('End of Season -Draft', 'white'),colored('>>>','white'),colored('End of game', 'white'))

    elif status == "est":
        print(colored('Intro', 'white'), colored('>>>', 'white'), colored('Season', 'white'), colored('>>>', 'white'), colored("Play Off's", 'white'), colored('>>>', 'white'), colored('End of Season -Training', 'red'),colored('>>>', 'white'),colored('End of Season -Draft', 'white'),colored('>>>','white'),colored('End of game', 'white'))

    elif status == "esd":
        print(colored('Intro', 'white'), colored('>>>', 'white'), colored('Season', 'white'), colored('>>>', 'white'), colored("Play Off's", 'white'), colored('>>>', 'white'), colored('End of Season -Training', 'white'),colored('>>>', 'white'),colored('End of Season -Draft', 'red'),colored('>>>','white'),colored('End of game', 'white'))

    elif status == "eg":
        print(colored('Intro', 'white'), colored('>>>', 'white'), colored('Season', 'white'), colored('>>>', 'white'), colored("Play Off's", 'white'), colored('>>>', 'white'), colored('End of Season -Training', 'white'),colored('>>>', 'white'),colored('End of Season -Draft', 'white'),colored('>>>','white'),colored('End of game', 'red'))
        
    else:
        print("Oh dear something went wrong you passed a status of=",status)
        return



    print("Season %s Game %s" % (season, game))
    print("First XI Defensive score ", defscore)
    print("First XI Attacking score ", atascore)
    print("##################################")

if __name__=="__main__":
    # to unit test output
    import os
    os.system('clear')
    header(status="i", season=1, game=1, defscore=20, atascore=30)
    header(status="s", season=1, game=1, defscore=20, atascore=30)
    header(status="p", season=1, game=1, defscore=20, atascore=30)
    header(status="est", season=1, game=1, defscore=20, atascore=30)
    header(status="esd", season=1, game=1, defscore=20, atascore=30)
    header(status="eg", season=1, game=1, defscore=20, atascore=30)
    header(status="x", season=1, game=1, defscore=20, atascore=30)
