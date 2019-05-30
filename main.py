#!/usr/bin/python3
# get variables from a lookup script, rather than hard coding in mulitple areas

#from func_other_game_settings import minage,maxage,maxbudget,firstrounddraftpicks,secondrounddraftpicks ,thirdrounddraftpicks ,startseason ,maxskillofinitalteam ,minskillofinitalteam,defaultformation ,squad_size_gk,squad_size_def,squad_size_mid,squad_size_ata


import os
import sys
import func_other_teamreport
import func_other_header
import func_intro_gameintro
import func_endofseason_training
import func_endofseason_draft
import func_end_of_game
import func_play_off
import func_season
import func_other_game_settings

# variables

global season
season = func_other_game_settings.startseason
seasonstoplay=func_other_game_settings.seasonstoplay

global game
game = 0

global auto_save_game
auto_save_game=func_other_game_settings.auto_save_game
saved_game_filename="saved_game.txt"

global previous_results,playoff_wins,defscore,atascore
previous_results=[]
defscore = 0  # these are declared as zero but worked out during game intro
atascore = 0


def print_previous_results():

    global previous_results,playoff_wins,defscore,atascore,season

    temp_results=[season,previous_results, defscore, atascore,playoff_wins]
    previous_results.append(temp_results)

    print ()
    print ("Previous season results 1")
    print ("\nS W D  A")
    for i in previous_results:
        temp_season=i[0]
        temp_wins=i[1]
        temp_def=i[2]
        temp_ata=i[3]
        temp_pow=i[3]
        print (temp_season,temp_wins,temp_def,temp_ata,temp_pow)



def s_game():
    
    save_details=[]
    #seasion number
    save_details.append(season)
    #last seasons poistion
    last_seasons_post=32
    save_details.append(last_seasons_post)
    save_details.append(players)
    save_details.append(developmentsquad)
    save_details.append(previousresults)

    with open(saved_game_filename, 'w') as filehandle:  
           filehandle.writelines('%s\n' % i for i in save_details)



thisyear_firstround=func_other_game_settings.firstrounddraftpicks
nextyear_firstround=func_other_game_settings.firstrounddraftpicks
thisyear_secondround=func_other_game_settings.secondrounddraftpicks
nextyear_secondround=func_other_game_settings.secondrounddraftpicks
thisyear_thirdround=func_other_game_settings.thirdrounddraftpicks
nextyear_thirdround=func_other_game_settings.thirdrounddraftpicks

defscore, atascore, players,developmentsquad,season,pseason = func_intro_gameintro.intro(incoming_season=season, game=game, defscore=defscore, atascore=atascore)


#Game logic
previousresults=[]

while season != seasonstoplay:

    normal_season_wins=0
    playoff_wins=0

    # normal season
    try:
        normal_season_wins,previousresults=func_season.season(season=season, game=game,defscore=defscore, atascore=atascore, squad=players,tpreviousseasonresults=pseason)
    except Exception as e:
        print (e)
        breakpoint()
    # play off 
    #stage_po=0 
    #stage_po=1
    #stage_po=2
    #stage_po=3
    #stage_po=4
    #stage_po=5

    exp_gained,playoff_wins,stage_po=func_play_off.playoff(season=season, game=game,defscore=defscore, atascore=atascore, squad=players,gameswon=normal_season_wins)
    #print_previous_results()

    # end of season training
    squad,devsquad=func_endofseason_training.training(season=season, game=game,defscore=defscore, atascore=atascore, squad=players,devsquad=developmentsquad,experience_gained=exp_gained)
    # end of season draft
    func_endofseason_draft.draft(game=game,idefscore=defscore, iatascore=atascore, squad=players,thisyear_firstround=thisyear_firstround,nextyear_firstround=nextyear_firstround,thisyear_secondround=thisyear_secondround,nextyear_secondround=nextyear_secondround,thisyear_thirdround=thisyear_thirdround,nextyear_thirdround=nextyear_thirdround,developmentsquad=developmentsquad,normal_season_wins=normal_season_wins,playoff_wins=playoff_wins,season_in=season)
    #add end of seasons playoff result to 
    len_previousresults=len(previousresults)-1
    if stage_po==0:
        poresults="Did not reach Play-offs"
    elif stage_po==1:
        poresults="Lost in Wildcard Weekend"
    elif stage_po==2:
        poresults="Lost in Divsional Game"
    elif stage_po==3:
        poresults="Lost in Conference Final"
    elif stage_po==4:
        poresults="Lost Superbowl"
    elif stage_po==5:
        poresults="Won Superbowl"
    else:
        breakpoint()
    try:
        previousresults[len_previousresults].append(poresults)
    except Exception as e1:
        print (e1)
        breakpoint()

    #updat team scores
    defscore, atascore=func_other_teamreport.report(oursquad=squad, formation=1442, printoutput="n")

    #clean up
    season=season+1
    #rotate draft picks, not currently used
    thisyear_firstround=nextyear_firstround
    nextyear_firstround=func_other_game_settings.firstrounddraftpicks
    thisyear_secondround=nextyear_secondround
    nextyear_secondround=func_other_game_settings.secondrounddraftpicks
    nextyear_thirdround=func_other_game_settings.thirdrounddraftpicks
    #save game
    if auto_save_game=="y":
        s_game()

func_end_of_game.endofgame(season=season, game=game,defscore=defscore, atascore=atascore, squad=players)


