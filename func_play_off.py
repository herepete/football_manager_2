#!/usr/bin/python3.7
import func_other_header
import func_other_menu
import func_game_engine
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

    whats_the_result=func_game_engine.game_result(ourdef=defscore,ourata=atascore,oppdef=opp_skill_def,oppata=opp_skill_ata)
    list_whats_the_result=whats_the_result.split(" ")
    print(whats_the_result)
    if list_whats_the_result[0] =="Win" or list_whats_the_result[0]=="Overtime-Win":
        return(1)
    else:
        return(0)





    '''
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
    '''


def playoff(season, game, defscore, atascore, squad,gameswon=9):

    global ngameswon
    ngameswon=int(gameswon)

    playoffwins=-1

    a=os.system('cls||clear')
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
        #print (wildcard_def,wildcard_ata)
        if won_game == 0:
            input ("Unlucky try again next season...")
            stage_po=1
            return (lose_in_wildcard_exp,playoffwins,stage_po)

        else:
            playoffwins+=1

    input ("\nEntering Diviosnal weekend, hit enter to continue")
    divisional_def=random.randint(75,86)
    divisional_ata=random.randint(75,86)
    won_game=game_logic(opp_skill_ata=divisional_ata,defscore=defscore,atascore=atascore,opp_skill_def=divisional_def)
    #print (divisional_def,divisional_ata)
    if won_game == 0:
        input ("Unlucky try again next season...")
        stage_po=2
        return (lose_in_divisional_exp,playoffwins,stage_po)

    else:
        playoffwins+=1


    input ("\nEntering Conference game, hit enter to continue")
    conference_def=random.randint(83,93)
    conference_ata=random.randint(83,93)
    won_game=game_logic(opp_skill_ata=conference_ata,defscore=defscore,atascore=atascore,opp_skill_def=conference_def)
    #print (conference_def,conference_ata)
    if won_game == 0:
        input ("Unlucky try again next season...")
        stage_po=3
        return (lose_in_conference,playoffwins,stage_po)
    else:
        playoffwins+=1


    input ("\nEntering Superbowl game, hit enter to continue")
    superbowl_def=random.randint(87,100)
    superbowl_ata=random.randint(89,100)
    won_game=game_logic(opp_skill_ata=superbowl_ata,defscore=defscore,atascore=atascore,opp_skill_def=superbowl_def)
    #print (superbowl_def,superbowl_ata)
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
    #    a=os.system('cls||clear')
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
    '''
    print ("***Script Called Directley****")

    qgameswon=input("how many g did we win?")
    exp_gained,rgameswon=playoff(season=1,game=2,defscore=99,atascore=99,squad=99,gameswon=qgameswon)
    print ()
    print ("We won...%s games" %(rgameswon))
    print ("We gained exp=" ,exp_gained)
    '''

    squad1=[['Gk', 'Phoenix', 'Plato', 29, 86, 3, 10, 12, 18, 15, 16, 19, 14, 95, 84, 4, 10, 'GT'], ['Gk', 'Myles', 'Cunningham', 21, 42, 4, 9, 8, 6, 14, 18, 18, 2, 48, 61, 1, 1, ''], ['Gk', 'Jose', 'Ainsworth', 28, 91, 9, 3, 15, 17, 20, 20, 14, 16, 99, 91, 4, 10, 'ST'], ['Def', 'Ari', 'Hawkins', 30, 2, 77, 24, 16, 19, 19, 15, 16, 7, 86, 88, 4, 8, 'GT'], ['Def', 'Ian', 'Fells', 20, 6, 76, 27, 19, 19, 12, 18, 12, 2, 82, 82, 2, 3, 'D'], ['Def', 'Ari', 'Read', 33, 9, 71, 33, 19, 18, 20, 14, 17, 13, 89, 87, 4, 8, 'ST'], ['Def', 'Olly', 'Forrest', 29, 1, 87, 52, 20, 15, 16, 16, 20, 11, 99, 80, 4, 10, 'GT'], ['Def', 'Shay', 'Allen', 20, 9, 73, 13, 20, 19, 16, 10, 18, 1, 81, 80, 4, 4, 'D'], ['Def', 'Freddy', 'Tagg', 22, 7, 70, 23, 17, 20, 20, 14, 8, 2, 76, 86, 2, 3, 'D'], ['Def', 'Luke ', 'Beckam', 19, 1, 34, 11, 9, 19, 6, 17, 13, 2, 45, 73, 1, 1, ''], ['Def', 'Vicktor', 'Weaver', 21, 6, 80, 18, 7, 17, 20, 16, 16, 2, 74, 87, 2, 3, 'D'], ['Mid', 'Mychal', 'Isaacs', 27, 6, 75, 65, 13, 17, 18, 15, 18, 6, 78, 84, 1, 6, ''], ['Mid', 'Dai', 'Green ', 22, 1, 49, 45, 13, 18, 6, 5, 15, 1, 53, 57, 1, 1, ''], ['Mid', 'Elias', 'Ellis', 28, 7, 85, 89, 17, 19, 19, 17, 14, 14, 96, 90, 1, 14, 'ST'], ['Mid', 'Illya', 'Kett', 35, 7, 61, 62, 9, 20, 17, 20, 6, 7, 69, 89, 3, 4, 'GT'], ['Mid', 'Ari', 'Quigley', 28, 9, 83, 87, 16, 16, 12, 18, 17, 9, 92, 78, 4, 9, ''], ['Mid', 'Miguel', 'Whyte', 18, 7, 46, 38, 15, 14, 9, 6, 10, 2, 52, 52, 1, 1, ''], ['Mid', 'Lenny', 'Mayfield', 33, 6, 37, 45, 5, 18, 18, 8, 18, 7, 52, 78, 3, 1, 'GT'], ['Mid', 'Pat', 'Burns', 18, 1, 59, 44, 6, 19, 20, 9, 5, 1, 51, 77, 1, 1, 'U'], ['Ata', 'Joe', 'Mccoy', 20, 1, 6, 43, 17, 15, 5, 6, 19, 1, 55, 53, 1, 1, ''], ['Ata', 'Charlie', 'Whiteman', 19, 8, 5, 84, 13, 18, 19, 20, 11, 2, 82, 90, 3, 5, 'D'], ['Ata', 'Quain', 'Marsh', 19, 1, 6, 61, 16, 19, 20, 12, 12, 2, 70, 84, 2, 3, 'D'], ['Ata', 'Nasim', 'Weaver', 31, 3, 10, 77, 17, 20, 16, 13, 12, 15, 88, 82, 1, 10, 'ST'], ['Ata', 'Val', 'Diamond', 33, 6, 7, 72, 13, 19, 15, 13, 20, 12, 83, 83, 4, 7, 'GT']]
    playoff(season=3, game=16, defscore=80, atascore=90, squad=squad1,gameswon=9)

