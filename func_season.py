#!/usr/bin/python3
import func_other_header
import os
import func_other_menu
import random
import time
import pdb
import func_game_engine
import func_other_teamreport
import func_clear_screen


global previous_results
previous_results=[]

def random_injury(squad):

    #age discremantion
    #loop through every player if random injury number =2
    #depending on age and char_det_luck we will remove 10% of their fitness
    #we pass back the new squad and any changes made 
    # example in changes (this inclues end of season training) 

#Mid Harold Lam               35    54    -7    46    0
#Mid Emile Randolph           33    58    1     62    2

#P   Name                 A   GS  DS  AS  F   Ab  C   D   L   E   VTT PA  Co  Wa  Sc
#Mid Harold     Lam       35  5   35  65  18  7   9   13  10  7   65  46  1   4
#Mid Harold     Lam       36  5   22  52  14  7   9   13  10  8   54  46  0   4

#Mid Emile      Randolph  33  7   58  61  7   14  11  11  9   8   62  60  1   3
#Mid Emile      Randolph  34  7   58  61  2   14  13  11  9   9   58  62  0   3

    changes=[]

    for player in squad:
        temppost=str(player[0])
        templname =str(player[2])
        tempage=int(player[3])
        tempfitness=player[7]
        tempfitness_90_percent=int((tempfitness/100)*90)
        char_det_luck=int(player[9])+int(player[10])+int(player[11])
        injury_random_number=random.randint(1,3)

        if injury_random_number ==2:
            if tempage >32:
                if tempfitness <13 and char_det_luck <55: 
                    player[7]=tempfitness_90_percent
                    n_in_nice_format=str(tempfitness_90_percent-tempfitness)
                    tchange=[temppost,templname,n_in_nice_format]
                    changes.append(temppost)
                    changes.append(templname)
                    changes.append(n_in_nice_format)
                elif tempfitness <16 and char_det_luck <50:
                    player[7]=tempfitness_90_percent
                    n_in_nice_format=str(tempfitness_90_percent-tempfitness)
                    tchange=[temppost,templname,n_in_nice_format]
                    changes.append(temppost)
                    changes.append(templname)
                    changes.append(n_in_nice_format)

                    #pdb.set_trace()
                elif tempfitness < 19 and char_det_luck <45:
                    player[7]=tempfitness_90_percent
                    n_in_nice_format=str(tempfitness_90_percent-tempfitness)
                    tchange=[temppost,templname,n_in_nice_format]
                    changes.append(temppost)
                    changes.append(templname)
                    changes.append(n_in_nice_format)
                    #pdb.set_trace()

    return (squad,changes)

 
        


def season(season, game, defscore, atascore, squad,tpreviousseasonresults):
    '''
    This is where the standard season starts
    input = season, game, defscore, atascore, squad)
    output = un-determined
    '''

    #check if we have previous season results (i.e from a loaded game and if so use them)
    #if not previousseasonresults:
        #i.e empty
        #print("no results")
     #   pass
    #else:
     #   previous_results=previousseasonresults

    #breakpoint()

    ourwins=0
   
    #build opp score
    global previousseasonresults 
    opposition_skill=[]
    for i in range(0,16):

        #after quite a lot of batch testing i came up with this:
        # our def ,our ata , %win rate (over 1,000 games) -including overtime
        # 70 v 70 = 13.3%
        # 80 v 80 = 42.9%
        # 85 v 85 = 63.8%
        # 90 v 90 = 79.6%
        # 95 v 95 = 88%
        # 99 v 99 = 90%
                   
        truely_random=random.randint(1,10)
        if truely_random <3:
            random_defscore=random.randint(70,80)
            random_atascore=random.randint(70,80)
        elif truely_random <7:
            random_defscore=random.randint(75,85)
            random_atascore=random.randint(75,85)
        elif truely_random <8:
            random_defscore=random.randint(78,87)
            random_atascore=random.randint(78,87)
        elif truely_random <9:
            random_defscore=random.randint(80,90)
            random_atascore=random.randint(80,90)
        else:
            random_defscore=random.randint(85,95)
            random_atascore=random.randint(85,95)

        random_opps=[random_defscore,random_atascore]
        opposition_skill.append(random_opps)

    while True:
        func_clear_screen.clear_screen()
        func_other_header.header(status="s", season=season, game=game,defscore=defscore, atascore=atascore)
        input ("Press enter to start the season")
        func_clear_screen.clear_screen()
        func_other_header.header(status="s", season=season, game=game,defscore=defscore, atascore=atascore)
        seasonresults=[]

        while True:
            #inspiraction taken from http://hjemmesider.diku.dk/~torbenm/Troll/RPGdice.pdf

            opp_skill_def, opp_skill_ata=opposition_skill.pop()
            #print ("Opposition skills ",opp_skill_def,opp_skill_ata)
            
            #goals against
            game=game+1
            gamenum= ("Game %s "%(game))
            tempresults=func_game_engine.game_result(ourdef=defscore,ourata=atascore,oppdef=opp_skill_def,oppata=opp_skill_ata)

            squad,changes=random_injury(squad)
            defscore, atascore = func_other_teamreport.report(oursquad=squad, formation=1442, printoutput="n")

            #game=game+1
            if "Win" in tempresults:
                ourwins+=1
            if not changes:
                tempresults=gamenum+tempresults
            else:
                #changes=str(changes)
                changes=' '.join(changes)
                s_and_result='{0: <28}'.format(gamenum+tempresults)
                tempresults=s_and_result+"  #"+changes
                
            seasonresults.append(tempresults)
            tempresults=""
            print ("Season results...(+ any changes in fitness of players)")
            for results in seasonresults:
                print (results)
            time.sleep(1)

            if game ==16:
                break
            else:
                func_clear_screen.clear_screen()
                func_other_header.header(status="s", season=season, game=game,defscore=defscore, atascore=atascore)

        print ("Games Won ",ourwins)

        #insert option here to call function
        #season_results(season=season,po_result="",win=ourwins,Def_score=defscore,Ata_score=atascore)
        #"""
        global previous_results

        #check if we have previous season results (i.e from a loaded game and if so use them)
        if not tpreviousseasonresults:
            #i.e empty
            #print("no results")
            pass
        else:
            previous_results=tpreviousseasonresults


        temp_results=[season,ourwins, defscore, atascore]

        previous_results.append(temp_results)

        print ()
        print ("Previous season results")
        print ("\nSeason, Win, Def_Score,  Ata_Score, PlayOffResult")
        print ("====================================================")

        for i in previous_results:
            #breakpoint()
            temp_season=i[0]
            temp_wins=i[1]
            temp_def=i[2]
            temp_ata=i[3]
            try:
                temp_prev_play_results=i[4]
            except:
                temp_prev_play_results=""
            print ('{:<8}{:<5}{:<12}{:<11}{:<12}'.format(temp_season,temp_wins,temp_def,temp_ata,temp_prev_play_results))
            #print (temp_season,temp_wins,temp_def,temp_ata)
        #"""
        
        userinput= input("Press enter to continue or m for menu\n")
        #season_results2(season=season,po_result="",win=ourwins,Def_score=defscore,Ata_score=atascore,presults=previous_results)
        if userinput=="m":
            func_other_menu.menu(oursquad=squad, formation=1442, printoutput="y")
        else:
            break
    #breakpoint()
    #season_results2(season=season,po_result="",win=ourwins,Def_score=defscore,Ata_score=atascore,presults=previous_results)
    #global previous_results
    return (ourwins,previous_results)

#def season_results2(season,win,po_result,Def_score,Ata_score,presults):
#
#    lprevious_results=presults
#    temp_results=[season,win, Def_score, Ata_score,presults]
#    lprevious_results.append(temp_results)
#
#    breakpoint()

def season_results(season,win,Def_score,Ata_score):

    global previous_results
    global previousseasonresults
    breakpoint()

    #check if we have previous season results (i.e from a loaded game and if so use them)
    if not previousseasonresults:
        #i.e empty
        #print("no results")
        pass
    else:
        previous_results=previousseasonresults


    temp_results=[season,win, Def_score, Ata_score]
    previous_results.append(temp_results)

    print ()
    print ("Previous season results")
    print ("\nSeason, Win, Def_Score,  Ata_Score")
    print ("==================================")

    for i in previous_results:
        temp_season=i[0]
        temp_wins=i[1]
        temp_def=i[2]
        temp_ata=i[3]
        print ('{:<8}{:<5}{:<12}{:<6}'.format(temp_season,temp_wins,temp_def,temp_ata))



    
        

if __name__=="__main__":
    print ("***Script Called Directley****")
