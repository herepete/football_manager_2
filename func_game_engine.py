#!/usr/bin/python3.7
import random
import argparse
import os

verbosity=0

    #1 accept inputs
# caculate multipler and max scores
    #2 work on multipler as the different between our def / opp ata & our att / opp def 
    #2b if you have a difference of +10 on either def/ata you get a second role of the dice
    #3 multipler is added to input to create max score for us (if opposition is better max score will be a netagive number and reduced)
#roll the dice
    #4 choose random number between 
        # opp - input score -30 and input score for def and ata
        # us  - max score -30 and max score for def and ata
    #5 use the scores from  #4 (on the right hand side of the equation)
    #our_defense_score=opp_ata_score-our_def_score
    #our_attack_score=our_ata_score-opp_def_score
    #so basically a master def/ata score after random and multiples taken into account
    #6 get goals from master def/ata score above
    #opp_goals=random.randint(0,(our_defense_score//3))
    #our_goals=random.randint(0,(our_attack_score//3))
    #max goals hardcoded to 5
#check goals
    # if we score more than opp , win
    # if opp score more than us , loss
    # if same (i.e draw)
        #the teams are hard to split so
        #the mutpliers are reduant so we add the orginal input together, whoever has the highest has a chance has a 66.66% chance of winning in overtime
        # random.randint(0,2) 
        #us higher random number >= 1 we win  (66.66% chance of winning)
        #else ==2 we win (33.33% chance of winning)

    
    
        

def game_result(ourdef,ourata,oppdef,oppata):
    #ourdef=int(input("Our Def"))
    #ourdef=90
    #ourata=int(input("Our Att"))
    #ourata=90
    #oppdef=int(input("Opp Def"))
    #oppdef=80
    #oppata=int(input("Opp Ata"))
    #oppata=80
    if verbosity==1:
        print("inputs, ourdef=%s,ourata=%s,oppdef=%s,oppata=%s"%(ourdef,ourata,oppdef,oppata))

    #score difference
    # for every +1 add 1 to our max score

    goalsfor_multipler=ourata-oppdef
    if goalsfor_multipler>8:
        goalsfor_multipler=8
    goalsagainst_multiplier=ourdef-oppata
    if goalsagainst_multiplier>8:
        goalsagainst_multiplier=8

    if verbosity==1:
        print ("Multplier ,goalsfor_multipler=%s,goalsagainst_multiplier=%s"%(goalsfor_multipler,goalsagainst_multiplier))

    #only applying mutipler to us as if apply to opp as well it would double the effect
    #basically for every difference between our scores add 1 to our max score
    #if the oppistion had a high score  it would result in a minus number
    max_score_our_def=ourdef+goalsagainst_multiplier
    max_score_our_ata=ourata+goalsfor_multipler

    opp_def_dice=1
    opp_ata_dice=1
    our_def_dice=1
    our_ata_dice=1
    # if a differetial of 10 you get a second dice :)

    if (ourdef-oppata) > 15:
        # our defense is 10 better than opp ata
        our_def_dice=2
        if verbosity==1:
            print ("our_def_dice=2")
    if (oppata-ourdef) > 15:
        # our defense is 10 worse than opp ata
        opp_def_dice=2
        if verbosity==1:
            print ("opp_def_dice=2")
    if (ourata-oppdef) > 15:
        # our attack is 10 better than opp def
        our_ata_dice=2
        if verbosity==1:
            print ("our_ata_dice=2")
    if (oppdef-ourata) > 15:
        # our attack is 10 worse than opp def
        opp_def_dice=2
        if verbosity==1:
            print ("opp_def_dice=2")

    #roll dice

    our_def_score=0
    our_ata_score=0
    opp_def_score=0
    opp_ata_score=0


    for rolls in range(opp_def_dice):
        opp_def_score_temp=random.randint((oppdef-20),oppdef)
        if opp_def_score_temp>opp_def_score:
            opp_def_score=opp_def_score_temp

    for rolls in range(opp_ata_dice):
        opp_ata_score_temp=random.randint((oppata-20),oppata)
        if opp_ata_score_temp>opp_ata_score:
            opp_ata_score=opp_ata_score_temp

    for rolls in range(our_def_dice):
        our_def_score_temp=random.randint((max_score_our_def-20),max_score_our_def)
        if our_def_score_temp>our_def_score:
            our_def_score=our_def_score_temp

    for rolls in range(our_ata_dice):
        our_ata_score_temp=random.randint((max_score_our_ata-20),max_score_our_ata)
        if verbosity==1:
            print ("After multpliers - max_score_our_ata=%s max_score_our_ata-40=%s & Random number chosen=%s  "%(max_score_our_ata,max_score_our_ata-40,our_ata_score_temp))
        
        if our_ata_score_temp>our_ata_score:
            our_ata_score=our_ata_score_temp
    
    if verbosity==1:
        print ("After Dice roll ourdef score changed to %s from %s"%(our_def_score,ourdef))
        print ("After Dice roll ourata score changed to %s from %s"%(our_ata_score,ourata))
        print ("After Dice roll oppdef score changed to %s from %s"%(opp_def_score,oppdef))
        print ("After Dice roll oppata score changed to %s from %s"%(opp_ata_score,oppata))

    #caculate score basest on roll dice

    #so here we go for comparision
    our_defense_score=opp_ata_score-our_def_score
    our_attack_score=our_ata_score-opp_def_score

    #hardcode to stop decimals
    if our_defense_score < 3:
        our_defense_score=3
    if our_attack_score < 3:
        our_attack_score=3

    try:
        if our_defense_score > 15:
            defense_divider=2
        else:
            defense_divider=3
        opp_goals=random.randint(0,(our_defense_score//defense_divider))
        if opp_goals > 5:
            opp_goals=5
        
        if our_attack_score > 15:
            attack_divider=2
        else:
            attack_divider=3
        our_goals=random.randint(0,(our_attack_score//attack_divider))
        if  our_goals>5:
            our_goals=5
    except Exception as e:
        print (e)
        breakpoint()

    if verbosity==1:
        print ("our_Def_score=",our_defense_score)
        print ("our_Ata_score",our_attack_score)
        print ("our_goals=",our_goals)
        print ("opp_goals=",opp_goals)

    result=""

    if our_goals==opp_goals:
        result="Draw"
        ourtotalscore=ourdef+ourata
        opptotalscore=oppdef+oppata
        if ourtotalscore>opptotalscore:
            ourluck=1
        else:
            ourluck=2
        playoffluck=random.randint(0,2)
        if playoffluck>=ourluck:
            result="Overtime-Win"
        else:
            result="Overtime-Lose"
            
        
    elif opp_goals>our_goals:
        result="Lose"
    else:
        result="Win"

    return ("%s %s %s" %(result,our_goals,opp_goals))

if __name__ == "__main__":

    #os.system('clear')
    #verbosity=1

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

    output=game_result(ourdef=99,ourata=99,oppdef=random_defscore,oppata=random_atascore) 
    print (output)
