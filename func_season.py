#!/usr/bin/python3
import func_other_header
import os
import func_other_menu
import random
import time

global previous_results
previous_results=[]


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
        random_defscore=random.randint(70,85)
        random_atascore=random.randint(68,85)
        random_opps=[random_defscore,random_atascore]
        opposition_skill.append(random_opps)

    while True:
        a=os.system('cls||clear')
        func_other_header.header(status="s", season=season, game=game,defscore=defscore, atascore=atascore)
        input ("Press enter to start the season")
        a=os.system('cls||clear')
        func_other_header.header(status="s", season=season, game=game,defscore=defscore, atascore=atascore)
        print ("Season results...")

        while True:

            opp_skill_def, opp_skill_ata=opposition_skill.pop()
            #print ("Opposition skills ",opp_skill_def,opp_skill_ata)
            
            #goals against
            ga=round((opp_skill_ata-defscore)/5)
            if ga <1:
                ga=1
            ga=random.randint(0,ga)
            if ga >5:
                ga=random.randint(3,6)

            #goals for 
            gf=round((atascore-opp_skill_def)/5)
            if gf <1:
                gf=1
            gf=random.randint(0,gf)

            print ("us - %s , opp-%s oppd-%s oppa-%s" %(gf,ga,opp_skill_def,opp_skill_ata),end="")

            if int(ga) > int(gf):
                pass
                print (" Game lost")
                #lost
            elif ga <gf:
                #won
                ourwins+=1
                print (" Game Won")
            else:
                #draw
                opp_score=opp_skill_def+opp_skill_ata
                our_score=defscore+atascore
                difference_score=our_score-opp_score
                if difference_score >20:

                    drawresult=random.randint(0,3)
                elif difference_score >10:
                
                    drawresult=random.randint(0,2)
                else: 
                    drawresult=random.randint(0,1)
                    
                
                if drawresult>0:
                    ourwins+=1
                    print (" Game Won - in overtime")
                else:
                    print (" Game lost - in overtime")
            time.sleep(1)
            game+=1
            if game ==16:
                break

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
