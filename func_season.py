#!/usr/bin/python3
import func_other_header
import os
import func_other_menu
import random

global previous_results
previous_results=[]


def season(season, game, defscore, atascore, squad,previousseasonresults):
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
    opposition_skill=[]
    for i in range(0,16):
        random_defscore=random.randint(70,85)
        random_atascore=random.randint(68,85)
        random_opps=[random_defscore,random_atascore]
        opposition_skill.append(random_opps)

    while True:
        os.system('clear')
        func_other_header.header(status="s", season=season, game=game,defscore=defscore, atascore=atascore)
        input ("Press enter to start the season")
        os.system('clear')
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

            game+=1
            if game ==16:
                break

        print ("Games Won ",ourwins)

        global previous_results

    #check if we have previous season results (i.e from a loaded game and if so use them)
        if not previousseasonresults:
            #i.e empty
            #print("no results")
            pass
        else:
            previous_results=previousseasonresults


        temp_results=[season,ourwins, defscore, atascore]
        previous_results.append(temp_results)

        print ()
        print ("Previous season results")
        print ("\nSeason, Win, Def_Score,  Ata_Score")
        print ("==================================")

        for i in previous_results:
            #breakpoint()
            temp_season=i[0]
            temp_wins=i[1]
            temp_def=i[2]
            temp_ata=i[3]
            print ('{:<8}{:<5}{:<12}{:<6}'.format(temp_season,temp_wins,temp_def,temp_ata))
            #print (temp_season,temp_wins,temp_def,temp_ata)

            
        

        userinput= input("Press enter to continue or m for menu\n")
        if userinput=="m":
            func_other_menu.menu(oursquad=squad, formation=1442, printoutput="y")
        else:
            break
    #breakpoint()
    return (ourwins,previous_results)
        

if __name__=="__main__":
    print ("***Script Called Directley****")
