#!/usr/bin/python3
# intro to game
# team selection
# inital settings

# output draft picks
# number of seasons

from func_other_game_settings import minage,maxage,maxbudget,firstrounddraftpicks,secondrounddraftpicks ,thirdrounddraftpicks ,startseason ,maxskillofinitalteam ,minskillofinitalteam,defaultformation ,squad_size_gk,squad_size_def,squad_size_mid,squad_size_ata  

import func_other_header
import os
import func_other_create_players
import func_other_teamreport
import func_other_game_text
import func_other_format_input
import func_other_game_settings

global auto_save_game
auto_save_game=func_other_game_settings.auto_save_game
saved_game_filename="saved_game.txt"

'''

intro to game
team selection
inital settings

'''

def l_game():

    # read in file
    lseason=lseasonpost=lplayers=ldevelopmentsquad=filecontents = ""
    with open(saved_game_filename, 'r') as filehandle:
            filecontents = [filehandle.readlines()]
    #strip out \n from read in data
    #breakpoint()
    filecontents2=filecontents[0]
    lplayers=[]
    ldevelopmentsquad=[]
    lseason,lseasonpost,lplayers,ldevelopmentsquad,lprev_season_results=filecontents2

    #strip out crap we don't want i.e \n and "
    lplayers=eval(lplayers)
    ldevelopmentsquad=eval(ldevelopmentsquad)
    lseason=eval(lseason)
    lseasonpost=eval(lseasonpost)
    lprev_season_results=eval(lprev_season_results)

    global season
    season=lseason


    return ("99","99",lplayers,ldevelopmentsquad,lprev_season_results)


def intro(incoming_season, game, defscore, atascore):

    '''

    Getting the "Intro" section in place...
    
    input= season, game, defscore, atascore

    #this calls the welcome screen
    players2, newteam = func_other_game_text.intro()
    
    #create out scores
    masterdefscore, masteratascore = func_other_teamreport.report(
        players, formation, printoutput)

    output= masterdefscore, masteratascore, players
 
    '''
    global season
    season=incoming_season
    p_season_results=""

    a=os.system('cls||clear')

    players = func_other_create_players.createplayers(
        gk=squad_size_gk, defender=squad_size_def, mid=squad_size_mid, ata=squad_size_ata, qualityofplayer=func_other_game_settings.inital_top_range_player, maxageofplayer=maxage, minageofplayer=minage, ef="123")
    development_squad = func_other_create_players.createplayers(gk=2, defender=2, mid=2, ata=2, qualityofplayer=70, maxageofplayer=22, minageofplayer=18, ef="123",developmentsquad="y")
    
    # get team scores for header (this will get updated every off season)
    printoutput = "n"
    formation = defaultformation

    masterdefscore, masteratascore = func_other_teamreport.report(
        players, formation, printoutput)

    func_other_header.header(status="i", season=season, game=game,
                       defscore=masterdefscore, atascore=masteratascore)

    # newteam helps us work our if players should be used rather than the above default player creation
    newteam = 0

    exists = os.path.isfile(saved_game_filename)

    if exists:

        print ("Before we start")
        print("I have found a previously saved game,(saved_game.txt)shall i load that game?(y)")
        print ("\n***Note this previousley saved game will be overwritten at the end of the the next season***")
        load_game_qm=input()

        if load_game_qm=="y":
                defscore, atascore, players,development_squad,p_season_results = l_game()
                masterdefscore, masteratascore = func_other_teamreport.report(players, formation, printoutput)
                func_other_header.header(status="i", season=season, game=game,defscore=masterdefscore, atascore=masteratascore)
        else:
            a=os.system('cls||clear')
            func_other_header.header(status="i", season=season, game=game,defscore=masterdefscore, atascore=masteratascore)


        #this calls the welcome screen
        players2, newteam = func_other_game_text.intro()
    if newteam == 1:
        players = players2

    a=os.system('cls||clear')
    func_other_header.header(status="i", season=season, game=game,
                       defscore=masterdefscore, atascore=masteratascore)

    print("Here is your squad...\n")
    func_other_format_input.printplayers(players)

    print("\nAnd here is your Development squad...\n") 
    func_other_format_input.printplayers(development_squad)
    
    input("\nPress a button to continue")

    return(masterdefscore, masteratascore, players,development_squad,season,p_season_results)


if __name__ == "__main__":
    print ("Testing script...")
    intro(season=0, game=0, defscore=20, atascore=50)

