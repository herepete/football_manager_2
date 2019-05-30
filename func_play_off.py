#!/usr/bin/python3
import func_other_header
import func_other_menu
import os
import random


'''
<explain input>
<what happens>
<error checking>
'''

normal_exp=1
lose_in_wildcard_exp=1
lose_in_divisional_exp=1
lose_in_conference=2
lose_in_superblowl=3
win_superbowl=4
stage_po=0


def game_logic(opp_skill_ata,defscore,atascore,opp_skill_def):


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

    print ("us - %s , opp-%s" %(gf,ga),end="")

    if int(ga) > int(gf):
        print (" Game lost")
        return(0)
    #lost
    elif ga <gf:
    #won
        print (" Game Won")
        return(1)
    
    else:
    #draw
        drawresult_us=defscore+atascore
        drawresult_opp=opp_skill_ata+opp_skill_def
        difference_score=drawresult_us-drawresult_opp

        if drawresult_us >20:
            drawresult=random.randint(0,2)
        elif drawresult_us >10:
            drawresult=random.randint(0,2)
        else:
            drawresult=random.randint(0,1)
        if drawresult>0:
            print (" Game Won - in overtime")
            return(1)
        else:
            print (" Game lost - in overtime")
            return(0)


def playoff(season, game, defscore, atascore, squad,gameswon=9):

    global ngameswon
    ngameswon=int(gameswon)

    playoffwins=-1

    os.system('clear')
    func_other_header.header(status="p", season=season, game=game,defscore=defscore, atascore=atascore)

    if ngameswon < 9:
        input("You have not won enough games to enter the playoff's this year")
        #playoffwins=-1
        stage_po=0
        return (normal_exp,playoffwins,stage_po)

    if ngameswon < 11:
        playoffwins=0


        input("Entering Season play offs")

        input ("\nEntering Wild card weekend, hit enter to continue")
        wildcard_def=random.randint(70,80)
        wildcard_ata=random.randint(70,80)
        won_game=game_logic(opp_skill_ata=wildcard_ata,defscore=defscore,atascore=atascore,opp_skill_def=wildcard_def)
        print (wildcard_def,wildcard_ata)
        if won_game == 0:
            input ("Unlucky try again next season...")
            stage_po=1
            return (lose_in_wildcard_exp,playoffwins,stage_po)

        else:
            playoffwins+=1

    input ("\nEntering Diviosnal weekend, hit enter to continue")
    divisional_def=random.randint(75,83)
    divisional_ata=random.randint(75,83)
    won_game=game_logic(opp_skill_ata=divisional_ata,defscore=defscore,atascore=atascore,opp_skill_def=divisional_def)
    print (divisional_def,divisional_ata)
    if won_game == 0:
        input ("Unlucky try again next season...")
        stage_po=2
        return (lose_in_divisional_exp,playoffwins,stage_po)

    else:
        playoffwins+=1


    input ("\nEntering Conference game, hit enter to continue")
    conference_def=random.randint(83,90)
    conference_ata=random.randint(83,90)
    won_game=game_logic(opp_skill_ata=conference_ata,defscore=defscore,atascore=atascore,opp_skill_def=conference_def)
    print (conference_def,conference_ata)
    if won_game == 0:
        input ("Unlucky try again next season...")
        stage_po=3
        return (lose_in_conference,playoffwins,stage_po)
    else:
        playoffwins+=1


    input ("\nEntering Superbowl game, hit enter to continue")
    superbowl_def=random.randint(85,100)
    superbowl_ata=random.randint(85,100)
    won_game=game_logic(opp_skill_ata=superbowl_ata,defscore=defscore,atascore=atascore,opp_skill_def=superbowl_def)
    print (superbowl_def,superbowl_ata)
    if won_game == 0:
        input ("Unlucky try again next season...")
        stage_po=4
        return (lose_in_superblowl,playoffwins,stage_po)
    else:
        playoffwins+=1
        stage_po=5
        input ("Woop Superbowl won...")
        return (win_superbowl,playoffwins,stage_po)

        


    

    #while True:
    #    os.system('clear')
    #    func_other_header.header(status="p", season=season, game=game,defscore=defscore, atascore=atascore)
    #    userinput= input("Press enter to continue or m for menu\n")
    #    if userinput=="m":
    #        func_other_menu.menu(oursquad=squad, formation=1442, printoutput="y")
    #    else:
    #        break
    #playoff_wins=random.randint(1,5)
    #1 = lose in wildcard
    #2= lose in divisional
    #3 = lose in conference
    #4 = lose in superblowl
    #5 = win superbowl
    #return playoff_wins


if __name__ == "__main__":
    print ("***Script Called Directley****")

    qgameswon=input("how many g did we win?")
    exp_gained,rgameswon=playoff(season=1,game=2,defscore=99,atascore=99,squad=99,gameswon=qgameswon)
    print ()
    print ("We won...%s games" %(rgameswon))
    print ("We gained exp=" ,exp_gained)
