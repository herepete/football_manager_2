#!/usr/bin/python3
import func_other_header
import func_other_menu
import os
import func_other_create_players
import func_other_format_input
import func_other_menu
import func_other_teamreport
import func_other_errorchecking
import random
import func_other_game_settings
import pdb
import func_clear_screen

#from itertools import permutations
from itertools import combinations 
#import logging
#
#logging.basicConfig(level=logging.DEBUG)
#logging.basicConfig(filename='logging_info.log' ,level=logging.DEBUG)
global max_draft_picks_allowed
max_draft_picks_allowed= func_other_game_settings.picksperyearmax 

global player_selected
player_selected=[]

global season
season=0

global game
game=0

global defscore
#defscore=98

global atascore
#atascore=97

global formation
formation=func_other_game_settings.defaultformation

global player_history
player_history=[]

# desperate pick section. made global to stop refreshing of offers when page is reloaded
global desp_picks_offered,gdpick1,gdpick2,gdpick3,third_pick_offer
desp_picks_offered=0
third_pick_offer=0
gdpick1=0
gdpick2=0
gdpick3=0





'''
<explain input>
<what happens>
<error checking>
'''

def create_draft():
    global createdraft

    #mixing up the number of draft picks to allow higher number of hopefully good players dropping down the rounds occosinally

    randomnum=random.randint(0,13)
    randomize_size_of_draft_gk=func_other_game_settings.size_of_draft_gk + randomnum
    randomnum=random.randint(0,20)
    randomize_size_of_draft_def=func_other_game_settings.size_of_draft_def + randomnum
    randomnum=random.randint(0,20)
    randomize_size_of_draft_mid=func_other_game_settings.size_of_draft_mid + randomnum
    randomnum=random.randint(0,13)
    randomize_size_of_draft_ata=func_other_game_settings.size_of_draft_ata + randomnum

    createdraft=func_other_create_players.createplayers(gk=randomize_size_of_draft_gk, defender=randomize_size_of_draft_def, mid=randomize_size_of_draft_mid, ata=randomize_size_of_draft_ata, qualityofplayer=func_other_game_settings.quality_of_draft, maxageofplayer=22, minageofplayer=18, ef="abc",draftlist="y")
    for i in createdraft:
        func_other_teamreport.vtt(i)
        func_other_teamreport.player_potential(i)

    
def view_draft_flawed_genius(fa="n"):
    #fa if free agency we want to use something other than create draft
    print ("Top 5 Players based on flawed_genius (poor char but otherwise a good player)...")
    flawedcreatedraft=[]
    #breakpoint()
    # i.e remove anyone with to much char
    #b=0
    if fa=="n":
        for i in createdraft:
            fname=i[1]
            sname=i[2]
            charn=int(i[9])
            if charn < 8:
                flawedcreatedraft.append(i)
        print ("Order by Potential Ability")
        flawedcreatedraft.sort(key=lambda flawedcreatedraft: flawedcreatedraft[14], reverse=True)
        func_other_format_input.printplayers(flawedcreatedraft,draft="y",outputlimit=5)
        print ()
        print ("Order by Value to Team")
        flawedcreatedraft.sort(key=lambda flawedcreatedraft: flawedcreatedraft[13], reverse=True)
        func_other_format_input.printplayers(flawedcreatedraft,draft="y",outputlimit=5)

    else:
        for i in master_undrafted_rookies:
            fname=i[1]
            sname=i[2]
            charn=int(i[9])
            if charn < 8:
                flawedcreatedraft.append(i)


        print ("Order by Potential Ability")
        flawedcreatedraft.sort(key=lambda flawedcreatedraft: flawedcreatedraft[14], reverse=True)
        #func_other_format_input.printplayers(flawedcreatedraft,draft="y",outputlimit=5)
        func_other_format_input.printplayers(flawedcreatedraft,vtt="n",draft="n",outputlimit=5,justpostion="",playerswap="n",extra_field_at_front="n")
        print ()
        print ("Order by Value to Team")
        flawedcreatedraft.sort(key=lambda flawedcreatedraft: flawedcreatedraft[13], reverse=True)
        #func_other_format_input.printplayers(flawedcreatedraft,draft="y",outputlimit=5)
        func_other_format_input.printplayers(flawedcreatedraft,vtt="n",draft="n",outputlimit=5,justpostion="",playerswap="n",extra_field_at_front="n")

    


def view_draft_potential(fa="n"):
    #fa if free agency we want to use something other than create draft
    if fa=="n":
        print ("Top 5 Players based on potential...")
        createdraft.sort(key=lambda createdraft: createdraft[14], reverse=True)
        func_other_format_input.printplayers(createdraft,draft="y",outputlimit=5)
        print ()
        func_other_format_input.printplayers(createdraft,draft="y",outputlimit=5,justpostion="Gk")
        print ()
        func_other_format_input.printplayers(createdraft,draft="y",outputlimit=5,justpostion="Def")
        print ()
        func_other_format_input.printplayers(createdraft,draft="y",outputlimit=5,justpostion="Mid")
        print ()
        func_other_format_input.printplayers(createdraft,draft="y",outputlimit=5,justpostion="Ata")
    else:
        print ("Top 5 Players based on potential...")
        master_undrafted_rookies.sort(key=lambda master_undrafted_rookies: master_undrafted_rookies[14], reverse=True)
        #func_other_format_input.printplayers(master_undrafted_rookies,draft="y",outputlimit=5)
        func_other_format_input.printplayers(master_undrafted_rookies,vtt="n",draft="n",outputlimit=5,justpostion="",playerswap="n",extra_field_at_front="n")
        print ()
        #func_other_format_input.printplayers(master_undrafted_rookies,draft="y",outputlimit=5,justpostion="Gk")
        func_other_format_input.printplayers(master_undrafted_rookies,vtt="n",draft="n",outputlimit=5,justpostion="Gk",playerswap="n",extra_field_at_front="n")
        print ()
        #func_other_format_input.printplayers(master_undrafted_rookies,draft="y",outputlimit=5,justpostion="Def")
        func_other_format_input.printplayers(master_undrafted_rookies,vtt="n",draft="n",outputlimit=5,justpostion="Def",playerswap="n",extra_field_at_front="n")
        print ()
        #func_other_format_input.printplayers(master_undrafted_rookies,draft="y",outputlimit=5,justpostion="Mid")
        func_other_format_input.printplayers(master_undrafted_rookies,vtt="n",draft="n",outputlimit=5,justpostion="Mid",playerswap="n",extra_field_at_front="n")
        print ()
        #func_other_format_input.printplayers(master_undrafted_rookies,draft="y",outputlimit=5,justpostion="Ata")
        func_other_format_input.printplayers(master_undrafted_rookies,vtt="n",draft="n",outputlimit=5,justpostion="Ata",playerswap="n",extra_field_at_front="n")




def view_draft_valuetoteam(fa="n"):
    #fa if free agency we want to use something other than create draft
    print ("Top 5 Players based on Value to team...")
    if fa=="n":
        createdraft.sort(key=lambda createdraft: createdraft[13], reverse=True)
        func_other_format_input.printplayers(createdraft,draft="y",outputlimit=5)
        print ()
        func_other_format_input.printplayers(createdraft,draft="y",outputlimit=5,justpostion="Gk")
        print ()
        func_other_format_input.printplayers(createdraft,draft="y",outputlimit=5,justpostion="Def")
        print ()
        func_other_format_input.printplayers(createdraft,draft="y",outputlimit=5,justpostion="Mid")
        print ()
        func_other_format_input.printplayers(createdraft,draft="y",outputlimit=5,justpostion="Ata")
    else:
        master_undrafted_rookies.sort(key=lambda master_undrafted_rookies: master_undrafted_rookies[13], reverse=True)
        func_other_format_input.printplayers(master_undrafted_rookies,vtt="n",draft="n",outputlimit=5,justpostion="",playerswap="n",extra_field_at_front="n")
        print ()
        func_other_format_input.printplayers(master_undrafted_rookies,vtt="n",draft="n",outputlimit=5,justpostion="",playerswap="n",extra_field_at_front="n")
        print ()
        func_other_format_input.printplayers(master_undrafted_rookies,vtt="n",draft="n",outputlimit=5,justpostion="",playerswap="n",extra_field_at_front="n")
        print ()
        func_other_format_input.printplayers(master_undrafted_rookies,vtt="n",draft="n",outputlimit=5,justpostion="",playerswap="n",extra_field_at_front="n")
        print ()
        func_other_format_input.printplayers(master_undrafted_rookies,vtt="n",draft="n",outputlimit=5,justpostion="",playerswap="n",extra_field_at_front="n")


def value_players(vtt,age):

    # a spin on http://walterfootball.com/draftchart.php
    # based on VTT a player_value is given
    # the player_value then determines in which round you pick falls

    player_value=0

    if vtt < 80:
        player_value=0
    elif vtt==80:
        player_value=117
    elif vtt==81:
        player_value=135
    elif vtt==82:
        player_value=175
    elif vtt==83:
        player_value=225
    elif vtt==84:
        player_value=262
    elif vtt==85:
        player_value=292
    elif vtt==86:
        player_value=400
    elif vtt==87:
        player_value=480
    elif vtt==88:
        player_value=520
    elif vtt==89:
        player_value=570
    elif vtt==90:
        player_value=700
    elif vtt==91:
        player_value=850
    elif vtt==92:
        player_value=900
    elif vtt==93:
        player_value=1488
    elif vtt==94:
        player_value=1555
    elif vtt==95:
        player_value=1675
    elif vtt==96:
        player_value=2112
    elif vtt==97:
        player_value=2150
    elif vtt==98:
        player_value=2450
    elif vtt==99:
        player_value=2673
    elif vtt==100:
        player_value=2900
    # trying to get that bit more randomness and reduce duplicate offers
    if player_value-age < 22:
        player_value=player_value+100
    elif player_value-age < 24:
        player_value=player_value+50
    elif age == 28 and player_value >850:
        player_value=850
    elif age == 29 and player_value >720:
        player_value=720
    elif age == 30 and player_value >590:
        player_value=590
    elif age == 31 and player_value >530:
        player_value=530
    elif age == 32 and player_value >500:
        player_value=500
    elif age == 33 and player_value >440:
        player_value=440
    elif age == 34 and player_value >400:
        player_value=440
    elif age == 35 and player_value >300:
        player_value=300
    elif age == 36 and player_value >220:
        player_value=220
    elif age == 37 and player_value >150:
        player_value=150
    elif age >37 and player_value >120:
        player_value=120

        
    else:
        player_value=player_value-age



    return player_value

def draft_offer(player_value):

    value_into_pick_loopup={'1':'3000','2':'2600','3':'2200','4':'1800','5':'1700','6':'1600','7':'1500','8':'1400','9':'1350','10':'1300','11':'1250','12':'1200','13':'1150','14':'1100','15':'1050','16':'1000','17':'950','18':'900','19':'875','20':'850','21':'800','22':'780','23':'760','24':'740','25':'720','26':'700','27':'680','28':'660','29':'640','30':'620','31':'600','32':'590',
            '33':'580','34':'560','35':'550','36':'540','37':'530','38':'520','39':'510','40':'500','41':'490','42':'480','43':'470','44':'460','45':'450','46':'440','47':'430','48':'420','49':'410','50':'400','51':'390','52':'380','53':'370','54':'360','55':'350','56':'340','57':'330','58':'320','59':'310','60':'292','61':'284','62':'276','63':'270',
            '64':'265','65':'260','66':'255','67':'250','68':'245','69':'240','70':'235','71':'230','72':'225','73':'220','74':'215','75':'210','76':'205','77':'200','78':'195','79':'190','80':'185','81':'180','82':'175','83':'170','84':'165','85':'160','86':'155','87':'150','88':'145','89':'140','90':'140','91':'136','92':'132','93':'128','94':'124','95':'120','96':'116'}
    previous_value=4000# first value needs a value above 3000 for comparrision
    for pick,value in value_into_pick_loopup.items():
        if int(value) <=int(player_value) <=int(previous_value):
            return (pick)
        previous_value=value
    pick=(0)
    return (pick)

           
           
    
def swap_players(squad,all_round_pn,report="y",):
    '''
    report= do you want a report of to trigger the actual swap process
    '''

    global defscore
    global atascore

    if report=="y":
        print ("\nHere are the players whom you can sell...\n")
        playerstosell_d={}
        playerstosell_l=[]

      #first loop to get draft value of players put into a dictiorary with index possition in squad and offer
      #second loop if values found index index position to find player add to list and print offer
    offered_picks=[]
    for index,x in enumerate(squad):
        try:
            player_vtt=float(x[13])
        except Exception as e:
            print (index)
            print (e)
        player_contract=float(x[15])
        player_age=float(x[3])
        player_value=value_players(player_vtt,player_age)
        #player value in format - 192.0

        pick=draft_offer(player_value)
        #pick in format - 76
        if int(pick) in all_round_pn:
            # err we already have that offer lets try a bit of hacking to stop us having dupplicate picks
            while True:
                pick=int(pick)+1
                if int(pick) not in offered_picks:
                    #ahh found a value not in our pre-existing picks
                    break
                elif int(pick) >90:
                    # logic to deal with end of draft i.e we don't want a 93 pick popping up
                    pick ==0
                    break

        #ignore players at end of contract contracts or other edge cases (probable legacy issue know)
        if int(pick) == 0 or pick is None or player_contract==0 :
            pass
        else:
            playerstosell_d[index]=pick
    if len(playerstosell_d) > 0:
        for index,offer in playerstosell_d.items():
            #(Pdb) print ( playerstosell_d)
            #{0: '50', 5: '96', 12: '42', 19: '42', 22: '96'}

            player=squad[index].copy()
            player.append(offer)

            if  1 <= int(offer) <=3:
                player.append("First round")
            elif 4 <= int(offer) <=16:
                player.append ("First round middle pick")
            elif 16 <= int(offer) <=32:
                player.append("Later First round pick")
            elif 32 <= int(offer) < 64:
                player.append("Second round pick")
            elif 64 <= int(offer) < 97:
                player.append("Third round pick")


            playerstosell_l.append(player)
            #  playerstosell_l in format ['Ata', 'Gabriel', 'Plato', 34, 9, 9, 93, 12, 16, 5, 14, 13, 8, 82, 62, 2, 7, '89', 'Third round pick']


        func_other_format_input.printplayers(playerstosell_l,draft="",outputlimit=25,justpostion="",playerswap="y")
        print ("PN = Pick Number in the draft")
        defscore, atascore = func_other_teamreport.report(squad, formation, printoutput="n")
        return playerstosell_l  

def outofcontract_players(squad):

    print ("\nHere are the Out of contract players...(you can renew/release players after the draft,output limited to 7 players)\n")
    outofcontract=[]
    temp_squad=squad.copy()
    for index,i in enumerate(temp_squad):
        if (i[15]==0):
            outofcontract.append(i)
    #220319
    outofcontract.sort(key=lambda flawedcreatedraft: flawedcreatedraft[13], reverse=True)

    func_other_format_input.printplayers(outofcontract,draft="n",outputlimit=7,justpostion="")

def money(squad):

    print ("\nMoney Summary...\n")
    func_other_menu.finance_report(squad)


def draftnumbers(thisyear_firstround,nextyear_firstround,thisyear_secondround,nextyear_secondround,thisyear_thirdround,nextyear_thirdround,first_round_pn,second_round_pn,third_round_pn,all_round_pn):

    print ("\nBased on the seasons results & any picks you have acqured here are your draft picks...\n")

    thisyear_firstround=0
    thisyear_secondround=0
    thisyear_thirdround=0
    first_round_pn=[]
    second_round_pn=[]
    third_round_pn=[]
    first_round_text=""
    second_round_text=""
    third_round_text=""

    for i in all_round_pn:
        j=int(i)
        if j !="":
            if  j <33:
                thisyear_firstround=thisyear_firstround+1
                first_round_pn.append(j)
            elif  j <65:
                thisyear_secondround=thisyear_secondround+1
                second_round_pn.append(j)
            else:
                thisyear_thirdround=thisyear_thirdround+1
                third_round_pn.append(j)
            
    if len (first_round_pn) > 0:
        first_round_text=",".join([str(x) for x in first_round_pn])
    if len (second_round_pn) > 0:
        second_round_text=",".join([str(x) for x in second_round_pn])
    if len (third_round_pn) > 0:
        third_round_text=",".join([str(x) for x in third_round_pn])





    print ('{:<8}{:<8}{:<8}'.format("Round","Picks","Pick Number"))
    print()
    print ('{:<8}{:<8}{:<8}'.format("1",thisyear_firstround,first_round_text))
    print ('{:<8}{:<8}{:<8}'.format("2",thisyear_secondround,second_round_text))
    print ('{:<8}{:<8}{:<8}'.format("3",thisyear_thirdround,third_round_text))

def retiring_players(squad):

    pass
    #version2 will hopefully be added
def sell_player(squad,players_to_sell,developmentsquad):

    global defscore
    global atascore

    if players_to_sell:
        print ("\nHere are the players you can sell...\n")
        sellbuild=[]
        numberofplayers=[]
        templine=[]
        for index,i in enumerate(players_to_sell):
            templine=i.copy()
            #remove special skill field as not needed
            #breakpoint()
            del i[17]
            #breakpoint()
            templine.insert(0,index)
            numberofplayers.append(index)
            sellbuild.append(templine)
        func_other_format_input.printplayers(sellbuild,draft="",outputlimit=25,justpostion="",playerswap="y",extra_field_at_front="y",sellplayer="y")
    
        while True:
            playertochange=(input("Which numbered player do you want to sell {}? or press e to exit ".format(numberofplayers)))
            if playertochange=="e":
                players_pic_num=""
                break
                return(squad,developmentsquad,players_pic_num)
            else:
                #error check userinput
                valid_answer=func_other_errorchecking.checkinput(number="y",char="n",min=0,max=0,userinput=playertochange,listinput=numberofplayers)
            if valid_answer=="False":
                #bad answer
                print ("That is not a valid input please re-enter a correct value")
            else:
                playertochange=int(playertochange)
                playertosell=players_to_sell[playertochange]
                players_pic_num=playertosell[17]
                #need to convert player to sell into squad number
                # no unique id for each player so we are going to do a complicated compare (very small risk of similar name players,position and skills getting confused)
                playertosell_position=playertosell[0]
                playertosell_fname=playertosell[1]
                playertosell_sname=playertosell[2]
                playertosell_age=playertosell[3]
                playertosell_gkskill=playertosell[4]
                playertosell_defskill=playertosell[5]
                playertosell_ataskill=playertosell[6]
                playertosell_potential=playertosell[14]

                for index,i in enumerate(squad):
                    squad_pos=i[0]
                    squad_fname=i[1]
                    squad_sname=i[2]
                    squad_age=i[3]
                    squad_gkskill=i[4]
                    squad_defskill=i[5]
                    squad_ataskill=i[6]
                    squad_potential=i[14]
                    if (squad_pos==playertosell_position) and (squad_fname==playertosell_fname) and (squad_sname==playertosell_sname) and (squad_age==playertosell_age) and (squad_gkskill==playertosell_gkskill) and (squad_defskill==playertosell_defskill) and (squad_ataskill==playertosell_ataskill) and (squad_potential==playertosell_potential):
                        playertoremove=index


                squad,developmentsquad=switch_main_squad_and_dev_squad(squad=squad,devsquad=developmentsquad,playertoremove=playertoremove)
                #add new player to dev squad
                ttgk=0
                ttdef=0
                ttmid=0
                ttata=0
                if playertoremove <3:
                    ttgk=1
                elif playertoremove <11:
                    ttdef=1
                elif playertoremove <19:
                    ttmid=1
                else:
                    ttata=1

                newplayer_for_dev_squad1=func_other_create_players.createplayers(gk=ttgk, defender=ttdef, mid=ttmid, ata=ttata, qualityofplayer=60, maxageofplayer=21, minageofplayer=18, ef="abc",draftlist="n",developmentsquad="y")
                newplayer_for_dev_squad1=newplayer_for_dev_squad1[0]
                developmentsquad[dev_playertochange]=newplayer_for_dev_squad1
                break

             # add sold players pick to our picks
             # replace player with draft pick

        defscore, atascore = func_other_teamreport.report(squad, formation, printoutput="n")
        return (squad,developmentsquad,players_pic_num)
    else:
        input("There are currently no players to sell")
        players_pic_num=""
        return (squad,developmentsquad,players_pic_num)


def renewplayercontract(squad,developmentsquad):

    #logic for contract renew and player release

    global defscore
    global atascore

    print ("\nHere are the Out of contract players...\n")
    outofcontract=[]
    numberofplayers=[]
    temp_copy_of_squad=squad.copy()
    for index,i in enumerate(temp_copy_of_squad):
        if i[15]==0:
            templine=i.copy()
            templine.insert(0,index)
            numberofplayers.append(index)
            outofcontract.append(templine)
    func_other_format_input.printplayers(outofcontract,draft="",outputlimit=100,justpostion="",playerswap="",extra_field_at_front="y")
    #func_other_format_input.printplayers(outofcontract,draft="n",outputlimit=100,justpostion="")

    print()

    while True:
        print ("Note if you release a single player you can replace them with someone from the Development squad if you release all the replacment will be an undrafted rookie")
        playertochange=(input("\nWhich numbered player do you want to renew/release {}? or press e to exit or r to release all ".format(numberofplayers)))
        if playertochange=="r":
            playertochange2=(input("\nAre you really,really sure?(y) "))
            if playertochange2 !="y":
                print ("Confirmation not recevied, returning you to main menu")
                break

            for i in numberofplayers:
                try:
                    position_of_player=squad[i][0]
                except:
                    print ("Erroring if player to release is number 23")
                del squad[i]
                #developmentsquad="y" is the quickest way to force 1 year contracts
                if position_of_player=="Gk":
                    random_player_from_dev_squad=int(random.randint(0,1))
                    if int(developmentsquad[0][14]) > int(developmentsquad[1][14]):
                        random_player_from_dev_squad=0
                    else:
                        random_player_from_dev_squad=1
                    #double list needed as further down newplayer[0] is referenced without a double list newplayer[0]=Position rather than whole player 
                    newplayer=developmentsquad[random_player_from_dev_squad]
                    #using [0] as i am getting back list of a list which is screwing up the replace
                    newplayer_for_dev_squad=func_other_create_players.createplayers(gk=1, defender=0, mid=0, ata=0, qualityofplayer=50, maxageofplayer=21, minageofplayer=18, ef="abc",draftlist="n",developmentsquad="y")
                    newplayer_for_dev_squad=newplayer_for_dev_squad[0]
                    developmentsquad[random_player_from_dev_squad]=newplayer_for_dev_squad

                elif position_of_player=="Def":
                    if int(developmentsquad[2][14]) > int(developmentsquad[3][14]):
                        random_player_from_dev_squad=2
                    else:
                        random_player_from_dev_squad=3
                    newplayer=developmentsquad[random_player_from_dev_squad]
                    newplayer_for_dev_squad=func_other_create_players.createplayers(gk=0, defender=1, mid=0, ata=0, qualityofplayer=50, maxageofplayer=21, minageofplayer=18, ef="abc",draftlist="n",developmentsquad="y")
                    newplayer_for_dev_squad=newplayer_for_dev_squad[0]
                    developmentsquad[random_player_from_dev_squad]=newplayer_for_dev_squad
                    
                elif position_of_player=="Mid":
                    if int(developmentsquad[4][14]) > int(developmentsquad[5][14]):
                        random_player_from_dev_squad=4
                    else:
                        random_player_from_dev_squad=5
                    newplayer=developmentsquad[random_player_from_dev_squad]
                    newplayer_for_dev_squad=func_other_create_players.createplayers(gk=0, defender=0, mid=1, ata=0, qualityofplayer=50, maxageofplayer=21, minageofplayer=18, ef="abc",draftlist="n",developmentsquad="y")
                    newplayer_for_dev_squad=newplayer_for_dev_squad[0]
                    developmentsquad[random_player_from_dev_squad]=newplayer_for_dev_squad
                
                elif position_of_player=="Ata":
                    if int(developmentsquad[6][14]) > int(developmentsquad[7][14]):
                        random_player_from_dev_squad=6
                    else:
                        random_player_from_dev_squad=7

                    newplayer=developmentsquad[random_player_from_dev_squad]
                    newplayer_for_dev_squad=func_other_create_players.createplayers(gk=0, defender=0, mid=0, ata=1, qualityofplayer=50, maxageofplayer=21, minageofplayer=18, ef="abc",draftlist="n",developmentsquad="y")
                    newplayer_for_dev_squad=newplayer_for_dev_squad[0]
                    developmentsquad[random_player_from_dev_squad]=newplayer_for_dev_squad
                else:
                    print ("Woops")
                    breakpoint()
                #squad.insert(i,newplayer[0])   
                squad.insert(i,newplayer)   
            input ("\nAll out of contract players have been released and they have been replaced by a the player from the development Squad with the highest PA...press a button to continue ")
            break
        if playertochange=="e":
            break
        #error check userinput
        valid_answer=func_other_errorchecking.checkinput(number="y",char="n",min=0,max=0,userinput=playertochange,listinput=numberofplayers)
        if valid_answer=="False":
            #bad answer
            print ("That is not a valid input please re-enter a correct value")
        else:
            playeroption=input("Do you want to (r)release or (c)offer new contract ") 
            if (playeroption =="r") or (playeroption =="c"):
                #release player
                if playeroption =="r":
                    checkanswer=input("Are you sure you want to release the player? (y) ")
                    if checkanswer != "y":
                        print ("No Changes made returning to the menu")
                    else:
                        print ()
                        playertochange=int(playertochange)
                        squad,developmentsquad=switch_main_squad_and_dev_squad(squad=squad,devsquad=developmentsquad,playertoremove=playertochange)
                        defscore, atascore = func_other_teamreport.report(squad, formation, printoutput="n")

                        #add new player to dev squad
                        tgk=0
                        tdef=0
                        tmid=0
                        tata=0
                        if playertochange <3:
                            tgk=1
                        elif playertochange <11:
                            tdef=1
                        elif playertochange <19:
                            tmid=1
                        else:
                            tata=1

                        #newplayer=developmentsquad[random_player_from_dev_squad]
                        newplayer_for_dev_squad=func_other_create_players.createplayers(gk=tgk, defender=tdef, mid=tmid, ata=tata, qualityofplayer=60, maxageofplayer=21, minageofplayer=18, ef="abc",draftlist="n",developmentsquad="y")
                        newplayer_for_dev_squad=newplayer_for_dev_squad[0]
                        developmentsquad[dev_playertochange]=newplayer_for_dev_squad


                        input ("\nThe chosen player has been released...")
                        break
            if playeroption =="c":
                   #renew contract
                   #1/2/3 year options alongside costs
                   # prompt user for choice (or e to exit)
                   # update player accordingle

                   playertochange=int(playertochange)
                   playertorenew=squad[playertochange]
                   playertorenew_age=playertorenew[3]
                   playertorenew_sc=playertorenew[17]
                    
                   vttvalue=playertorenew[13]

                   #renew players contract

                   if vttvalue  <55:
                    wage=1
                   elif vttvalue  <60:
                    wage=2
                   elif vttvalue  <65:
                    wage=2
                   elif vttvalue  <70:
                    wage=3
                   elif vttvalue  <73:
                    wage=4
                   elif vttvalue  <76:
                    wage=5
                   elif vttvalue  <80:
                    wage=6
                   elif vttvalue  <85:
                    wage=7
                   elif vttvalue  <90:
                    wage=8
                   elif vttvalue  <95:
                    wage=9
                   else:
                    wage=10
                   if wage > 5:
                       if playertorenew_sc=="D":
                           print ("\nThe player feels a loyalty to the team as we was drafted by you so he is willing to take a smaller contract than otherwise expected...")
                           wage_p1=wage+0
                           wage_p2=wage+0
                           wage_p3=wage+0
                           wage_p4=wage+1
                       elif playertorenew_sc=="U":
                           print ("\nThe player feels a semi-loyalty to the team as we was drafted by you so he is willing to take a slightly smaller contract than otherwise expected...")
                           wage_p1=wage+1
                           wage_p2=wage+1
                           wage_p3=wage+1
                           wage_p4=wage+2
                       elif playertorenew_age>30:
                           wage_p1=wage+2
                           wage_p2=wage+1
                           wage_p3=wage+0
                           wage_p4=wage-1
                       else:
                           wage_p1=wage+0
                           wage_p2=wage+1
                           wage_p3=wage+2
                           wage_p4=wage+3
                   else:
                       if playertorenew_sc=="U":
                           print ("\nThe player feels a semi-loyalty to the team as we was drafted by you so he is willing to take a slightly smaller contract than otherwise expected...")
                           wage_p1=wage+0
                           wage_p2=wage+0
                           wage_p3=wage+1
                           wage_p4=wage+1
                       elif playertorenew_age<24:
                           wage_p1=wage+0
                           wage_p2=wage+0
                           wage_p3=wage+1
                           wage_p4=wage+1
                       else:
                           wage_p1=wage+0
                           wage_p2=wage+1
                           wage_p3=wage+1
                           wage_p4=wage+2
                   if wage >1:
                       wage_m1=wage-1
                   if int(playertorenew_age)>32:
                       print ("**Your Assistant is advising as the player is towards the end of this carrear he should not be given a long contract ")
                   print ("You can renwew:\n")
                   print ("1 year contract with Wage=", wage_p1)
                   print ("2 year contract with Wage=", wage_p2)
                   print ("3 year contract with Wage=", wage_p3)
                   print ("4 year contract with Wage=", wage_p4)
                   user_input=input("Enter 1/2/3/4 or e to exit? ")
                   breakhit=0
                   while True:
                       if (user_input =="1") or (user_input =="2") or (user_input =="3") or (user_input =="4") or (user_input =="e"):
                           if user_input =="1":
                            for index,i in enumerate(squad):
                                if index==playertochange:
                                    i[16]=wage_p1
                                    i[15]=1
                            print ("Change Made")
                            breakhit=1
                            break
                           if user_input =="2":
                            for index,i in enumerate(squad):
                                if index==playertochange:
                                    i[16]=wage_p2
                                    i[15]=2
                            print ("Change Made")
                            breakhit=1
                            break
                           if user_input =="3":
                            for index,i in enumerate(squad):
                                if index==playertochange:
                                    i[16]=wage_p3
                                    i[15]=3
                            print ("Change Made")
                            breakhit=1
                            break

                           if user_input =="4":
                            for index,i in enumerate(squad):
                                if index==playertochange:
                                    i[16]=wage
                                    i[15]=4
                            print ("Change Made")
                            breakhit=1
                            break
                           if user_input=="e":
                            print ("No Changes Made")
                            breakhit=1
                            break
                       else:
                           input ("Please enter a valid option... ")
                           break
                   if breakhit==1:
                        break






        
            
            else:
                print ("That is not a valid value please re-enter a correct value")
    #breakpoint()                
    return (squad,developmentsquad)
    
def switch_main_squad_and_dev_squad(squad,devsquad,playertoremove): 

    #prompt for replacement
    #replace
        #squad[playertochange]=player_from_practise_squad[0]
    #add dev player to squad
        #playerposition=(tempsquad[playertochange][1])
    #add new player to dev squad
    # some kind of confirmation
    # return s & ds

    global defscore
    global atascore
    
    toreplace_playerposition=(squad[playertoremove][0])
    templist_ps=[]
    dev_numberofplayers=[]
    for index,i in enumerate(devsquad):
        dev_playerposition=i[0]

        if toreplace_playerposition == dev_playerposition:
            templine=i.copy()
            templine.insert(0,index)
            templist_ps.append(templine)
            dev_numberofplayers.append(index)


    func_other_format_input.printplayers(templist_ps,draft="",outputlimit=100,justpostion="",playerswap="",extra_field_at_front="y")
    print ()
    while True:
        global dev_playertochange
        dev_playertochange=(input("Which numbered player do you want to promote from the Development Squad {}? or press e to exit ".format(dev_numberofplayers)))
        if dev_playertochange=="e":
            breakhit=1
            break
        dev_valid_answer=func_other_errorchecking.checkinput(number="y",char="n",min=0,max=0,userinput=dev_playertochange,listinput=dev_numberofplayers)
        if dev_valid_answer=="False":
            #bad answer
            print ("That is not a valid input please re-enter a correct value")
            breakhit=0
        else:
            dev_playertochange=int(dev_playertochange)
            squad[playertoremove]=devsquad[dev_playertochange]
            if toreplace_playerposition =="Gk":
                if int(devsquad[0][14]) > int(devsquad[1][14]):
                     random_player_from_dev_squad=0
                else:
                    random_player_from_dev_squad=1
                newplayer=devsquad[random_player_from_dev_squad]
                newplayer_for_dev_squad=func_other_create_players.createplayers(gk=1, defender=0, mid=0, ata=0, qualityofplayer=50, maxageofplayer=21, minageofplayer=18, ef="abc",draftlist="n",developmentsquad="y")
                newplayer_for_dev_squad=newplayer_for_dev_squad[0]


            if toreplace_playerposition =="Def":
                if int(devsquad[2][14]) > int(devsquad[3][14]):
                     random_player_from_dev_squad=2
                else:
                    random_player_from_dev_squad=3
                newplayer=devsquad[random_player_from_dev_squad]
                newplayer_for_dev_squad=func_other_create_players.createplayers(gk=0, defender=1, mid=0, ata=0, qualityofplayer=50, maxageofplayer=21, minageofplayer=18, ef="abc",draftlist="n",developmentsquad="y")
                newplayer_for_dev_squad=newplayer_for_dev_squad[0]

            if toreplace_playerposition =="Mid":
                if int(devsquad[4][14]) > int(devsquad[5][14]):
                     random_player_from_dev_squad=4
                else:
                    random_player_from_dev_squad=5
                newplayer=devsquad[random_player_from_dev_squad]
                newplayer_for_dev_squad=func_other_create_players.createplayers(gk=0, defender=0, mid=1, ata=0, qualityofplayer=50, maxageofplayer=21, minageofplayer=18, ef="abc",draftlist="n",developmentsquad="y")
                newplayer_for_dev_squad=newplayer_for_dev_squad[0]




            if toreplace_playerposition =="Ata":


                if int(devsquad[6][14]) > int(devsquad[7][14]):
                     random_player_from_dev_squad=6
                else:
                    random_player_from_dev_squad=7
                newplayer=devsquad[random_player_from_dev_squad]
                newplayer_for_dev_squad=func_other_create_players.createplayers(gk=0, defender=0, mid=0, ata=1, qualityofplayer=50, maxageofplayer=21, minageofplayer=18, ef="abc",draftlist="n",developmentsquad="y")
                newplayer_for_dev_squad=newplayer_for_dev_squad[0]







            #devsquad[dev_playertochange]=new_player_into_practise_squad[0]
            print ("Swap made")
            #input("Press a button to continue")
            breakhit=1
            break
        if breakhit==1:
            break

    defscore, atascore = func_other_teamreport.report(squad, formation, printoutput="n")

    return (squad,devsquad)

def rebuild_newpoints(allvalues,valueofplayer):
        #rebuild is done to stop the same pick being offered twice (to give the user more choice)
        #it also strips out any picks higher than our pick
    newpoints=[]

    for key,value in allvalues.items():
        value_n=int(value)
        if value_n < valueofplayer:
            newpoints.append(value)

    return(newpoints)

#def offer_picks


def move_up_down_draft (picks):

        #logic for 0 picks
        # 1 pick but 1 is 1st
        # 2 picks and 1 of them is 1st
        # 8 picks combo offer
        # accept new pick our and lose the others in exchange
        # pass back picks

        value_into_pick_loopup={'1':'3000','2':'2600','3':'2200','4':'1800','5':'1700','6':'1600','7':'1500','8':'1400','9':'1350','10':'1300','11':'1250','12':'1200','13':'1150','14':'1100','15':'1050','16':'1000','17':'950','18':'900','19':'875','20':'850','21':'800','22':'780','23':'760','24':'740','25':'720','26':'700','27':'680','28':'660','29':'640','30':'620','31':'600','32':'590',
                            '33':'580','34':'560','35':'550','36':'540','37':'530','38':'520','39':'510','40':'500','41':'490','42':'480','43':'470','44':'460','45':'450','46':'440','47':'430','48':'420','49':'410','50':'400','51':'390','52':'380','53':'370','54':'360','55':'350','56':'340','57':'330','58':'320','59':'310','60':'292','61':'284','62':'276','63':'270',
                                        '64':'265','65':'260','66':'255','67':'250','68':'245','69':'240','70':'235','71':'230','72':'225','73':'220','74':'215','75':'210','76':'205','77':'200','78':'195','79':'190','80':'185','81':'180','82':'175','83':'170','84':'165','85':'160','86':'155','87':'150','88':'145','89':'140','90':'140','91':'136','92':'132','93':'128','94':'124','95':'120','96':'116'}
        total_value_of_picks=0
        picks.sort()
        picks_string=",".join([str(x) for x in picks])
        print ("Summary")
        print ("=======")
        print ("You have picks ",picks_string)
        print ("\nMove up the Draft")
        print ("=================")
        if 1 in picks:
            print ("\nYou already have the first pick, so it will not be used in the following qualications")
        for i in picks:
            for j,k in value_into_pick_loopup.items():
                if int(j)==int(i) and int(i) !=1:
                    total_value_of_picks=total_value_of_picks+int(k)
        #i need an upper limit to (lastitem) to have as a first compare
        lastitem=8000
        for j,k in  value_into_pick_loopup.items():
            
            if int(lastitem) > total_value_of_picks >= int(k):
                move_up_to=j

            lastitem=k
        number_picks=len(picks)
        try:
            if number_picks==1:
                    print("\nYou only have 1 pick so you cannot move up in the draft...")
            elif move_up_to in picks:
                    print ("\nYou cannot move up any higher than the pick you already possess ...")
            else:
                try:
                    print("\nSelling all your picks you could move up to a highest position of ...",move_up_to)
                except:
                    print ("Something went wrong dropping into debug mode")
                    breakpoint()
        except Exception as e:
            print (e)
            input("oops")
            breakpoint()
        print ()

        print ("Move Down the Draft")
        print ("===================\n")
        len_picks=len(picks)+1

        first_round_pick=picks[0]
        allvalues={'1':'3000','2':'2600','3':'2200','4':'1800','5':'1700','6':'1600','7':'1500','8':'1400','9':'1350','10':'1300','11':'1250','12':'1200','13':'1150','14':'1100','15':'1050','16':'1000','17':'950','18':'900','19':'875','20':'850','21':'800','22':'780','23':'760','24':'740','25':'720','26':'700','27':'680','28':'660','29':'640','30':'620','31':'600','32':'590',
                                        '33':'580','34':'560','35':'550','36':'540','37':'530','38':'520','39':'510','40':'500','41':'490','42':'480','43':'470','44':'460','45':'450','46':'440','47':'430','48':'420','49':'410','50':'400','51':'390','52':'380','53':'370','54':'360','55':'350','56':'340','57':'330','58':'320','59':'310','60':'292','61':'284','62':'276','63':'270',
                                                                            '64':'265','65':'260','66':'255','67':'250','68':'245','69':'240','70':'235','71':'230','72':'225','73':'220','74':'215','75':'210','76':'205','77':'200','78':'195','79':'190','80':'185','81':'180','82':'175','83':'170','84':'165','85':'160','86':'155','87':'150','88':'145','89':'140','90':'140','91':'136','92':'132','93':'128','94':'124','95':'120','96':'116'}
        if int(picks[0])>32:
            print ("No first round picks are avaiable to trade down for")
        else:
            # simple explanation - We don't want trade offers for picks we already possess so we remove our picks as eligable items from allvalues lookup, we also remove any picks higher than our first round pick.
            # example we have pick 4,34,78 . from our lookup 1,2,3,4 get stripped as they are not permitted numbers
            # explanation - get value of our first pick (at index 0 of picks) and delete it
            for index,i in enumerate(picks):
                tempstr=str(i)
                # firstitem
                if index==0:
                    valueofplayer= int(allvalues.get(tempstr))
                if index==1:
                    #used to help caculate if we can offer a pick for our second first round pick
                    valueof2player=int(allvalues.get(tempstr))
                del allvalues[tempstr]

            newpoints=[]
            newpoints=rebuild_newpoints(allvalues,valueofplayer)
            offers={}
            #will look like offers={'23': '57', '48': '28'}
            picks_for_offers=[]
            #will look like picks_for_offers=[1,32]
            #output will look like...
            # for Your 1 you are offered pick 23 and 57
            # for Your 32 you are offered pick 48 and 28



            count_p=0
            while True:
                # this will create 3 offers
                # each offer to you is made up of 2 picks(parts)
                # 1 pick(part) a random number lower than your pick
                # 2 pick(part)a numerical is caculated by value of your pick - 1st part of the offer
                # each offer & your current pick & anything higher than your pick will get removed from the lookup
                # so if you win the SB and have pick 32 the first 32 picks are removed from the lookup followed by 6(3*2)offers & any other picks you already have
 
                # first part of offer 
                # explanation pick a random number from newpoints (depending on picks number the lookup will show all values less than your highest pick)

                firstofferrn=random.choice(newpoints)
                #explanation firstofferrn (example 600 i.e 32)is turned into a positional pick number
                for key,value in allvalues.items():
                    if value==firstofferrn:
                        firstoffer_text=key
                #explanation don't want that random pick to be offered again so its removed from the lookup 
                del allvalues[firstoffer_text]
                newpoints=rebuild_newpoints(allvalues,valueofplayer)

                #explanation so we know have 1 pick in exchange for ours to get the second pick we work our the differnce between the pick we have and the pick we have already been offered
                # example we have pick number 1 in the draft, random selected first offer is pick 4 , the second offer is worked out as the points left where pick 1 (3000 points)  -pick 4 (1800points)
                # = 1200 points left to find. Going back to the lookup 1200 points = Pick 12 so the offer sheet will look something like
                # For pick number 1 in the draft you are offered pick 4 & pick 12

                value_left=int(valueofplayer)-int(firstofferrn)
                seondoffer=0

                #second part of offer
                for i in newpoints:
                    if int(value_left) > int(i):
                        seondoffer=i
                        break

                    seondoffer_text=""
                for key2,value2 in allvalues.items():
                    if value2==seondoffer:
                        seondoffer_text=key2
                if seondoffer_text=="":
                    if value_left < 200:
                        # set to 200 as a large catch all
                        #oops not enough value left to create that second pick i.e
                        #(Pdb) print (all_of_our_picks)
                        #[17] # 950 points
    
                        #(Pdb) print (firstofferrn)
                        #875
                        #(Pdb) print (firstoffer_text)
                        # get last item
                        seondoffer_text=sorted(allvalues.keys())[-1]

                del allvalues[seondoffer_text]
                newpoints=rebuild_newpoints(allvalues,valueofplayer)

                #add offer to offical list
                offers[firstoffer_text]=seondoffer_text
                count_p=count_p+1
                picks_for_offers.append(first_round_pick)
                #breakpoint()
                # the 3 here means we only want 3 different offers(the count starts at 0) for our picks (each offer is made up of 2 picks)
                if count_p==3:
                    break


            #let check if we have a second first round pick and see if we can create an offer of that (it might be the lookup is to small or the maths is not possible)
            picks.sort()
            countfrp=0
            second_first_round_hit=0
            for i in picks:
                tempi=int(i)
                if i < 33:
                    countfrp+=1
                if countfrp < 2:
                    pass
                if i > 32:
                    pass
                    #less than 2 first round picks
                    #pick number is greater than 32
                else:
                    #breakpoint()
                    # more than 1 first round pick
                    # follow logic from above section
                    count_ps=0
                    second_first_round_hit=1
                    while True:

                        newpoints=rebuild_newpoints(allvalues,valueof2player)
                        # first part of offer
                        firstofferrn_second=random.choice(newpoints)
                        for key,value in allvalues.items():
                            if value==firstofferrn_second:
                                firstoffer_text_second=key
                        del allvalues[firstoffer_text_second]
                        newpoints=rebuild_newpoints(allvalues,valueof2player)

                        value_left=int(valueofplayer)-int(firstofferrn_second)
                        seondoffer=0
                        #second part of offer

                        for i in newpoints:
                            if int(value_left) > int(i):
                                seondoffer=i
                                break

                            seondoffer_text=""
                        for key2,value2 in allvalues.items():
                            if value2==seondoffer:
                                seondoffer_text=key2
                        if seondoffer_text=="":
                            if value_left < 200:
                                seondoffer_text=sorted(allvalues.keys())[-1]
                        count_ps+=1
                        if count_ps > 0:
                            break
                    offers[firstoffer_text_second]= seondoffer_text
                    picks_for_offers.append(tempi)
                    #breakpoint()

            offer_counter=0
            if second_first_round_hit==0:
                print ("Here are some offers for your picks...")
                # used for error checking
                maxoffers=2
            else:
                second_first_round_pick=picks[1]
                print ("Here are some offers for your picks...")
                maxoffers=3

            print ()
            print ("{:<8}{:<16}{:<16}{:<16}".format("Offer","Pick Number 1","Pick Number 2","For your Pick"))
            for index,(key,value) in enumerate(offers.items()):
                    tempoffer=picks_for_offers[index]
                    print ("{:<8}{:<16}{:<16}{:<16}".format(offer_counter,key,value,tempoffer))
                    if offer_counter==0:
                        offer_0=[key,value]
                    elif offer_counter==1:
                        offer_1=[key,value]
                    elif offer_counter==2:
                        offer_2=[key,value]
                    elif offer_counter==3:
                        offer_3=[key,value]
                    elif offer_counter==4:
                        offer_4=[key,value]
                    elif offer_counter==5:
                        offer_5=[key,value]
                    elif offer_counter==6:
                        offer_6=[key,value]

                    offer_counter=offer_counter+1

        breakhit_trace=0
        while True:
            user_input=input("\nEnter: \n(e)exit\n(u)Move up Draft\n(d)Move Down Draft ")
            if breakhit_trace==1:
                break
            if user_input=="e":
                breakhit_trace=1
                break
            elif user_input=="u" and number_picks==1:
                input("Only 1 pick avaliable, so you cannot move up the draft...")
                break

            elif user_input=="d":
                if len(picks)>=max_draft_picks_allowed:
                    print ("By moving down the draft you will breach the max %s picks rule,you could move up the draft to free up a trade"%(max_draft_picks_allowed))
                    input()
                    break
                if int(picks[0])> 32:
                    print ("Sorry you can only trade down first round picks & you don't have any :(")
                    input()
                    break 

                user_replace=input("Which offer do you want to choose?(or (e) to exit)")
                if user_replace=="e":
                    print ("e hit so exiting")
                    input()
                    break
                maxoffers=len(picks_for_offers)

                
                replace_result=func_other_errorchecking.checkinput(number="y",char="n",min=0,max=maxoffers,userinput=int(user_replace),listinput="")
                if replace_result=="True":
                    replace_sure=input("Are you sure (y)")
                    if replace_sure =="y":
                        #breakpoint()
                        if int(user_replace)==0:
                            temp_add= int(offer_0[0])
                            temp_add1= int(offer_0[1])
                        if int(user_replace)==1:
                            temp_add= int(offer_1[0])
                            temp_add1= int(offer_1[1])
                        if int(user_replace)==2:
                            temp_add= int(offer_2[0])
                            temp_add1= int(offer_2[1])
                        if int(user_replace)==3:
                            temp_add= int(offer_3[0])
                            temp_add1= int(offer_3[1])
                        if int(user_replace)==4:
                            temp_add= int(offer_4[0])
                            temp_add1= int(offer_4[1])
                        if int(user_replace)==5:
                            temp_add= int(offer_5[0])
                            temp_add1= int(offer_5[1])
                        if int(user_replace)==6:
                            temp_add= int(offer_6[0])
                            temp_add1= int(offer_6[1])

                        #if int(user_replace)==3:
                        #    picks.remove(second_first_round_pick)
                        #else:
                        #    picks.remove(first_round_pick)
                        remove_pick=picks_for_offers[int(user_replace)]
                        picks.remove(remove_pick)
                        picks.append(temp_add)
                        picks.append(temp_add1)
                        input ("Ok swapped (press enter to continue)")
                        break
                    else:
                        print ("Y not selected so not Swapped")
                        input()
                        #break
                else:
                    print ("That is not a valid option please re-try")
                    input("")

            elif user_input=="u":

                picks_m1=len(picks)+1
                all_offers=[]
                first_round_picks=0
                second_round_picks=0
                third_round_picks=0
                #picks_m1=len(picks)
                while True:
                    picks_m1=picks_m1-1
                    if picks_m1==1:
                        breakhit_trace=1
                        break
                      
                    perm = combinations(picks,picks_m1)
                    temp_total_value_of_picks=0
                    temp_picks=[]
                    #goes through itertools perm and 
                    for idd in list(perm):
                        #breakpoint()
                        optionsd=idd
                        # example 
                        #optionsd
                        #(15, 47, 79)

                        #print ("optionsd=",idd)
                        temp_total_value_of_picks=0
                        temp_picks=[]
                        #loop through each pick
                        for jd in optionsd:
                            #print ("jd=",jd)
                            temp_picks.append(jd)
                            for ld,kd in value_into_pick_loopup.items():
                                #print ("ld and kd=",ld,kd)
                                if int(jd)==int(ld): 
                                    temp_total_value_of_picks=temp_total_value_of_picks+int(kd)
                            temp_lastitem=8000
                            for pd,nd in  value_into_pick_loopup.items():
                                if int(temp_lastitem) > temp_total_value_of_picks >= int(nd):
                                    move_up_to=pd
                                temp_lastitem=nd
                        temp_picks_text=",".join(map(str,temp_picks))
                        if move_up_to not in picks:
                            #print ("You can swap picks... %s in exchange for %s " %(temp_picks_text,move_up_to))
                            temp_offer=("You can swap picks... %s in exchange for pick %s " %(temp_picks_text,move_up_to))
                            all_offers.append(temp_offer)
                            if int(move_up_to)<33:
                                first_round_picks=first_round_picks+1
                            elif int(move_up_to)<65:
                                second_round_picks=second_round_picks+1
                            else:
                                third_round_picks=third_round_picks+1
                        #    if move_up_to=="":
                        #        print ("That looks odd, lets head into bebuger as move_up_to should not be blank")
                        #        breakpoint()

                        temp_picks_text=""
                        move_up_to=""
                print ("\nSummary of Options of moving up the draft")
                print ("===========================================")
                print ("\nFirst round offers=",first_round_picks)
                print ("Second round offers=",second_round_picks)
                print ("Third round offers=",third_round_picks)
                print ("\nOffers")
                print ("=====")
                #breakpoint()
               
                for index,i in enumerate(all_offers):
                    print (index, i)
                # index offers
                # offer choice
                # offer > new list 
                # new list extract numbers
                offer_range=len(all_offers)-1
                print("press (e) to exit or a number between 0 and ",offer_range)
                user_choice=input()
                if user_choice=="e":
                    break
                else:
                   # userchoice_text=int(userchoice_text)
                    valid_answer_uc=func_other_errorchecking.checkinput(number="y",char="n",min=0,max=offer_range,userinput=user_choice)
                    if valid_answer_uc =="True":
                        # we need to do a bit of hacking to get
                        # You can swap picks... 47,79 in exchange for pick 31
                        # into a offer we will replace the comma with a space, strip out the numbers and then in a list pop the last item i.e 31
                        # and loop through whats left i.e 47 & 79
                        user_choice=int(user_choice)
                        listitem_extracted=all_offers[user_choice]
                        listitem_extracted=listitem_extracted.replace("," , " ")
                        num_from_listitem_extracted=[int(s) for s in listitem_extracted.split() if s.isdigit()]
                        #last item in list i.e the pick we will get
                        newpick=num_from_listitem_extracted.pop()
                        # loop through the rest i.e the picks we will lose 
                        picks.append(newpick)
                        for i in num_from_listitem_extracted:
                            picks.remove(i)


                        input("All done")
                    else:
                        print ("Please enter a valid option")
                        input()
                        continue




            else:
                input("\nPlease enter a valid option")
                continuehit=1
                continue

        picks.sort()
        return picks

def draft_choice_logic(pick_num=3):

    type_of_player=random.randint(1,100)

    if pick_num < 4:
        best_player=70
        best_gk=80
        best_def=85
        best_mid=90
        best_ata=100
        best_pot=0
        best_flawed=0
    elif pick_num < 11:
        best_player=40
        best_gk=55
        best_def=70
        best_mid=85
        best_ata=100
        best_pot=0
        best_flawed=0
    elif pick_num < 33:
        best_player=30
        best_gk=47
        best_def=64
        best_mid=81
        best_ata=100
        best_pot=0
        best_flawed=0
    elif pick_num < 64:
        best_player=30
        best_gk=40
        best_def=50
        best_mid=60
        best_ata=70
        best_pot=100
        best_flawed=0
    else:
        best_player=10
        best_gk=22
        best_def=34
        best_mid=46
        best_ata=70
        best_pot=100
        best_flawed=0 # needs some work to include
       # i.e 3rd round
    #print ()

    #safety check number of players left and if in doubt default to best player
    totalgkleft=0
    totaldefleft=0
    totalmidleft=0
    totalataleft=0
    for type_player in createdraft:
        if type_player[0]=="Gk":
            totalgkleft+=1
        if type_player[0]=="Def":
            totaldefleft+=1
        if type_player[0]=="Mid":
            totalmidleft+=1
        if type_player[0]=="Ata":
            totalataleft+=1
        

    #lets go down this logic if not many positionaly players left
    if (totalgkleft < 5) or (totaldefleft < 5) or (totalmidleft < 5) or (totalataleft < 5): 
        pick_player_in_draft(picklogic="bp",picknumber=pick_num)
    elif type_of_player > 0 and type_of_player < best_player:
        #print ("Deleting Best Player")
        pick_player_in_draft(picklogic="bp",picknumber=pick_num)
    elif type_of_player > 0 and type_of_player < best_gk:
        #print ("Deleting Best Gk")
        pick_player_in_draft(picklogic="gk",picknumber=pick_num)
    elif type_of_player > 0 and type_of_player < best_def:
        #print ("Deleting Best Defender")
        pick_player_in_draft(picklogic="def",picknumber=pick_num)
    elif type_of_player > 0 and type_of_player < best_mid:
        #print ("Deleting Best Midfielder")
        pick_player_in_draft(picklogic="mid",picknumber=pick_num)
    elif type_of_player > 0 and type_of_player <= best_ata:
        #print ("Deleting Best Atacker")
        pick_player_in_draft(picklogic="ata",picknumber=pick_num)
    elif type_of_player > 0 and type_of_player <= best_pot:
        #print ("Deleting Best potential")
        pick_player_in_draft(picklogic="pot",picknumber=pick_num)
        pass
    else: 
        print ("I shouldn't hit this logic")
        breakpoint()
        pass
        #type_of_player > 0 and type_of_player < best_flawed:




def enter_draft(picks,squad,developmentsquad):

    #createdraft is a global variable
    # only 96 picks , but 98 as i want the extra number to add a suitable breakout of loop point
    draft_picks=list(range(1,98))
    pick_num=0
    breakhit=0
    breakhit1=0

    global defscore
    global atascore
    picks.sort()

    while breakhit==0:
        for pick_num in draft_picks:
            lastitem=draft_picks[-1]

            if int(pick_num) > 96:
                breakhit=1
                break

            if pick_num in picks:
                playerleft=len(createdraft)

                if pick_num < 33:
                    print ("First Round")
                    print ("Your picks ",picks)

                elif int(pick_num)>=33 and int(pick_num)<=64:
                    func_clear_screen.clear_screen()
                    func_other_header.header(status="esd", season=season, game=game,defscore=defscore, atascore=atascore)
                    print ("Second Round")
                    global player_selected
                    if int(pick_num)==33:
                        player_selected=[]
                    print ("Your picks ",picks)
                    
                elif int(pick_num)>=65:
                    func_clear_screen.clear_screen()
                    func_other_header.header(status="esd", season=season, game=game,defscore=defscore, atascore=atascore)
                    print ("Third Round")
                    if int(pick_num)==65:
                        player_selected=[]
                    print ("Your picks ",picks)
                else:
                    print ("Your picks ",picks)
                    print ("Players selected so far in the round")
                    print ()
                func_other_format_input.printplayers(input=player_selected,vtt="n",draft="n",outputlimit=1000,justpostion="",playerswap="n",extra_field_at_front="n",sellplayer="n")

                while True:
                    if int(pick_num) > 96:
                        breakhit=1
                        break
                    input ("\nYour turn to pick...(%s)" %(pick_num))
                    func_clear_screen.clear_screen()
                    func_other_header.header(status="esd", season=season, game=game,defscore=defscore, atascore=atascore)
        
                    picksleft=[]
                    for pl in picks:
                        if pl >= pick_num:
                            picksleft.append(pl)

                    print("Press: \nh Help Menu\no View your Squad\nx First XI Team report\np for top players by potential\nv value to team(default view) \nf Flawed\ns for (manual) sort\ny draft your player (i.e continue)\nd move down draft (if you have a desperate team willing to move up the draft)")
                    print ("You have picks the following picks left...",picksleft)

                    desperate_pick_offer=0
                    # so only offer if in first 2 round and we have less that 6 picks already (less than 7 was getting a bit silly)
                    if int(pick_num) < 65 and (len(picks)<8):
                        desperate_pick_offer=1
                        print ("\n***A desparate team want to jump up in the draft and will offer you***")
                        global desp_picks_offered,dpick1,dpick2
                        #desp_picks_offered=0
                        #gdpick1=0
                        #gdpick2=0

                        # trying to prevent "new offer" being given on screen re-fresh
                        if desp_picks_offered==0:

                            if pick_num < 3:
                                desperation_ranking=random.randint(1,3)
                                desperation_ranking2=random.randint(5,10)
                                desperation_ranking3=random.randint(80,96)
                                third_pick_offer=1
                            elif pick_num < 8:
                                desperation_ranking=random.randint(1,6)
                                desperation_ranking2=random.randint(4,10)
                                desperation_ranking3=random.randint(90,96)
                                third_pick_offer=1
                            elif pick_num < 20:
                                desperation_ranking=random.randint(3,10)
                                desperation_ranking2=random.randint(7,18)
                                third_pick_offer=0
                            elif pick_num < 32:
                                desperation_ranking=random.randint(3,24)
                                desperation_ranking2=random.randint(5,18)
                                third_pick_offer=0
                            else:
                                desperation_ranking=random.randint(1,24)
                                desperation_ranking2=random.randint(10,25)
                                third_pick_offer=0
        
                            tally=0
                            dpick1=pick_num+desperation_ranking
                            while dpick1 in picks:
                                dpick1+=1                  
                                tally+=1
                                if tally >6:
                                    print ("Infinite loop please help...")
                                    breakpoint()
                            dpick2=dpick1+desperation_ranking2
                            while dpick2 in picks:
                                dpick2+=1                  
                                tally+=1
                                if tally >12:
                                    print ("Infinite loop please help...")
                                    breakpoint()
                            tally=0
                            #try:
                            if third_pick_offer==1:
                                dpick3=desperation_ranking3
                                while dpick3 in picks:
                                    dpick3-=1                  
                                    tally+=1
                                    if tally >6:
                                        print ("Infinite loop please help...")
                                        breakpoint()
                            else:
                                pass
                            #except Exception as e:
                                #print("Woops11")
                                #print (e)
                                #breakpoint()
    


                            if third_pick_offer==1:
                                print ("Pick %s and %s and %s for this pick (%s)"%(dpick1,dpick2,dpick3,pick_num))
                                desperate_pick_offer=1
                                desp_picks_offered=1

                                gdpick1=dpick1
                                gdpick2=dpick2
                                gdpick3=dpick3
                            else:
                                print ("Pick %s and %s for this pick (%s)"%(dpick1,dpick2,pick_num))
                                desperate_pick_offer=1

                                desp_picks_offered=1
                                gdpick1=dpick1
                                gdpick2=dpick2
                        else:
                            if third_pick_offer==1:
                                dpick1=gdpick1
                                dpick2=gdpick2
                                dpick3=gdpick3
                                print ("Pick %s and %s and %s for this pick (%s)"%(dpick1,dpick2,dpick3,pick_num))
                                desperate_pick_offer=1

                            else:
                                dpick1=gdpick1
                                dpick2=gdpick2
                                print ("Pick %s and %s for this pick (%s)"%(dpick1,dpick2,pick_num))
                                
                                desperate_pick_offer=1
        
                              



                    #view_draft_valuetoteam()
                    userinput1=input("")
                    if userinput1=="d" and desperate_pick_offer==1:
                        #breakpoint()
                        #add and remove items to our picks list
                        picks.append(dpick1)
                        picks.append(dpick2)
                        picks.remove(pick_num)
                        if third_pick_offer==1:
                            picks.append(dpick3)
                        picks.sort()
                        print ("Draft picks swapped")
                        # and let the opposition take a draft pick
                        draft_choice_logic(pick_num=pick_num)
                        input("Press a button to continue")
                        desp_picks_offered=0
                        break
                        
                    if userinput1=="h":
                        func_clear_screen.clear_screen()
                        func_other_header.header(status="esd", season=season, game=game,defscore=defscore, atascore=atascore)
                        func_other_menu.menu(oursquad=squad, formation=1442, printoutput="y")
                        continue
                    if userinput1=="x":
                        func_clear_screen.clear_screen()
                        func_other_header.header(status="esd", season=season, game=game,defscore=defscore, atascore=atascore)
                        func_other_teamreport.report(oursquad=squad, formation=1442, printoutput="y")
                        input ("\nPress enter to continue")
                        continue

                    if userinput1=="y":
                        userinput1a=input("How do you want to Order avaliable players? VTT(default) or (p)potenital or (a)all players sorted by position ")
                        #
                        if userinput1a == "p":
                            createdraft.sort(key=lambda createdraft: createdraft[14],reverse=True)
                            func_other_format_input.printplayers(createdraft,draft="yd",outputlimit=30,justpostion="")
                        elif userinput1a == "a":
                            createdraft.sort(key=lambda createdraft: createdraft[0],reverse=True)
                            func_other_format_input.printplayers(createdraft,draft="yd",outputlimit=999,justpostion="")
                        else:
                            createdraft.sort(key=lambda createdraft: createdraft[13],reverse=True)
                            func_other_format_input.printplayers(createdraft,draft="yd",outputlimit=30,justpostion="")
                        print ()
                        #createdraft.sort(key=lambda createdraft: createdraft[14],reverse=True)
                        #func_other_format_input.printplayers(createdraft,draft="yd",outputlimit=10,justpostion="")
                        whom_to_draft=input("enter the number of the player you want to draft or r to choose a differnt sort option ")
                        if whom_to_draft=="r":
                            continue
                        else:
                            try:
                                 whom_to_draft=int(whom_to_draft)
                                 defscore, atascore = func_other_teamreport.report(squad, formation, printoutput="n")
                            except:
                                #breakhit1=1
                                input("Invalid input, please try again")
                                continue

                        validdraftnumbers=playerleft-1
                        valid_answer1=func_other_errorchecking.checkinput(number="y",char="n",min=0,max=validdraftnumbers,userinput=whom_to_draft,listinput="")
                        if valid_answer1=="True":                  
                            posttion_new_draft_pick=createdraft[whom_to_draft]
                            posttion_new_draft_pick=posttion_new_draft_pick[0]
                            posttion_name=createdraft[whom_to_draft][1] + " " + createdraft[whom_to_draft][2] 
                            record_signing_player(ppostion=posttion_new_draft_pick,pname=posttion_name,playerdraftinfo=pick_num,playersoldinfo="")
                            #who_to_replace_list=squad.copy()
                            #who_to_replace_list=enumerate(who_to_replace_list)

                            func_other_format_input.printplayers(squad,vtt="y",draft="yd",outputlimit=100,justpostion=posttion_new_draft_pick)


                            if posttion_new_draft_pick=="Gk":
                                min_post_num=0
                                max_post_num=2
                                add_values=0
                            elif posttion_new_draft_pick=="Def":
                                min_post_num=1
                                max_post_num=8
                                add_values=2
                            elif posttion_new_draft_pick=="Mid":
                                min_post_num=1
                                max_post_num=8
                                add_values=10
                            elif posttion_new_draft_pick=="Ata":
                                min_post_num=1
                                max_post_num=5
                                add_values=18
                            else:
                                print ("Oops")
                                breakpoint()



                            userinput4=input("Who do you wish to replace? between %s - %s, or if you want to return and draft a different enter an invalid number " %(min_post_num,max_post_num))
                            valid_answer4=func_other_errorchecking.checkinput(number="y",char="n",min=min_post_num,max=max_post_num,userinput=userinput4,listinput="")
                            if valid_answer4=="True":
                                userinput4=int(userinput4)
                                #func_other_format_input.printplayers(squad,draft="n",outputlimit=100,justpostion="")
                                player_to_delete1=int(userinput4)+add_values
                                del squad[player_to_delete1]
                                playerselected=createdraft[whom_to_draft]
                                #playerdrafted
                                playerselected[17]="D"
                                #edit players contract length and wage to reflect draft position
                                if pick_num <4:
                                    #15 =contract lenght , 16 =wage
                                    playerselected[15]=4
                                    playerselected[16]=5
                                elif pick_num <33:
                                    playerselected[15]=4
                                    playerselected[16]=4
                                elif pick_num <65:
                                    playerselected[15]=3
                                    playerselected[16]=3
                                else:
                                    # i.e 3rd rounder
                                    playerselected[15]=2
                                    playerselected[16]=2
                                squad.insert(player_to_delete1,playerselected)
                                del createdraft[whom_to_draft]
                                defscore, atascore = func_other_teamreport.report(squad, formation, printoutput="n")

                                #func_other_format_input.printplayers(squad,draft="n",outputlimit=100,justpostion="")
                                pname1=playerselected[1]
                                sname1=playerselected[2]
                                input ("%s %s has been signed on %s year contract on wages of %s, press enter to continue" %(pname1,sname1,playerselected[15],playerselected[16]))
                                # we have rejected the inital desperate team offer so reset the offer for the next pick
                                desp_picks_offered=0
                                break
                            else:
                                input ("That is invalid number please try again...(i a going to return you to the player draft menu)")
                                breakhit1=1


                            #replace player logic
                   
                        else:
                            if breakhit1==1:
                                pass
                            else:
                                input ("That is invalid input please try again...")
                                continue
                            #invalid option
                        #input()


                    # on out pick clear page (make page slicker)
                    # menu top 10 players (enumrated), top 10 potetnial(e),all - maybe overcompicated
                    # just enuermate the whole draft and allow filtering?
                    # choose player - confirm y/n
                    # get exit of for loop correct maybe it needs to be udner a while loop?
                    # swap player
                    # cap hit?
                    # all our picks then exit draft to next page opn menu?

                    if userinput1=="o":
                        func_clear_screen.clear_screen()
                        func_other_header.header(status="esd", season=season, game=game,defscore=defscore, atascore=atascore)
                        func_other_format_input.printplayers(squad,draft="n",outputlimit=100,justpostion="")
                        print ("\nHere Is your Development squad\n")
                        func_other_format_input.printplayers(developmentsquad,draft="n",outputlimit=100,justpostion="")
                        input("Press a button to conitnue")
                        
                    if userinput1=="p":
                        func_clear_screen.clear_screen()
                        func_other_header.header(status="esd", season=season, game=game,defscore=defscore, atascore=atascore)
                        view_draft_potential()
                        input("Press a button to conitnue")
                        #continue
                    elif userinput1=="v":
                        func_clear_screen.clear_screen()
                        func_other_header.header(status="esd", season=season, game=game,defscore=defscore, atascore=atascore)
                        view_draft_valuetoteam()
                        input("Press a button to conitnue")
                        #continue
                    elif userinput1=="f":
                        func_clear_screen.clear_screen()
                        func_other_header.header(status="esd", season=season, game=game,defscore=defscore, atascore=atascore)
                        view_draft_flawed_genius()
                        input("Press a button to conitnue")
                        #continue
                    elif userinput1=="s":
                        func_clear_screen.clear_screen()
                        func_other_header.header(status="esd", season=season, game=game,defscore=defscore, atascore=atascore)
                        userinput2=input ("Enter an option to sort by : \n\nA -age\nGS -Goalkeeper skill\nDS -Defense Skill\nAS -Attack Skill\nF -Fitness\nAb -Ability\nC -Char\nD -Determination\nL -Luck\nE -experience\nVTT -Value to team\nPA -Potential Ability\ne To exit\n")
                        if userinput2=="e":
                            #continue
                            pass
                        else:
                            userinput3=input ("Enter a position i.e Gk/Def/Mid/Ata to filter by leave blank for all\n")

                            if userinput3 in ("Gk","Def","Mid","Ata"):
                                jp=userinput3
                            else:
                               jp="" 
                               if userinput2=="A":
                                    createdraft.sort(key=lambda createdraft: createdraft[3], reverse=True)
                               if userinput2=="GS":
                                    createdraft.sort(key=lambda createdraft: createdraft[4], reverse=True)
                               if userinput2=="DS":
                                    createdraft.sort(key=lambda createdraft: createdraft[5], reverse=True)
                               if userinput2=="AS":
                                    createdraft.sort(key=lambda createdraft: createdraft[6], reverse=True)
                               if userinput2=="F":
                                    createdraft.sort(key=lambda createdraft: createdraft[7], reverse=True)
                               if userinput2=="Ab":
                                    createdraft.sort(key=lambda createdraft: createdraft[8], reverse=True)
                               if userinput2=="C":
                                    createdraft.sort(key=lambda createdraft: createdraft[9], reverse=True)
                               if userinput2=="D":
                                    createdraft.sort(key=lambda createdraft: createdraft[10], reverse=True)
                               if userinput2=="L":
                                    createdraft.sort(key=lambda createdraft: createdraft[11], reverse=True)
                               if userinput2=="E":
                                    createdraft.sort(key=lambda createdraft: createdraft[12], reverse=True)
                               if userinput2=="VTT":
                                    createdraft.sort(key=lambda createdraft: createdraft[13], reverse=True)
                               if userinput2=="PA":
                                    createdraft.sort(key=lambda createdraft: createdraft[14], reverse=True)

                               func_other_format_input.printplayers(createdraft,draft="y",outputlimit=200,justpostion=jp)


    
                        input("Press a button to conitnue")
                        #continue
                    else:
                        if breakhit1==1:
                            pass
                        else:
                            input("Enter a valid button ")


            else:
                draft_choice_logic(pick_num=pick_num)
                if int(pick_num)==33:
                    func_clear_screen.clear_screen()
                    func_other_header.header(status="esd", season=season, game=game,defscore=defscore, atascore=atascore)
                    print ("Second Round")
                if int(pick_num)==65:
                    func_clear_screen.clear_screen()
                    func_other_header.header(status="esd", season=season, game=game,defscore=defscore, atascore=atascore)
                    print ("Third Round")
        global undrafted_rookies
        undrafted_rookies=createdraft

    return (squad)


def pick_player_in_draft(picklogic,picknumber):

    #picklogic:
    # bp =best player
    # pot = potential
    # fla = flawed chars

    if picknumber==33 or picknumber==65:
        # clear up list after previous round
        global player_selected
        player_selected=[]

    playerleft=len(createdraft)
    #print ("Picknumber=%s , Player left=%s " %(picknumber,playerleft))

    if picklogic=="bp":
        createdraft.sort(key=lambda createdraft: createdraft[13], reverse=True)
        # trying to add a bit more value the lower down the draft you go
        if picknumber < 33:
            whom_shall_we_remove=random.randint(0,2)
        elif picknumber < 65:
            whom_shall_we_remove=random.randint(0,5)
        else:
            whom_shall_we_remove=random.randint(0,8)
        #print ("player ",createdraft[whom_shall_we_remove])
        temp_player=list(createdraft[whom_shall_we_remove])
        # hacky but getting it into a list of a list so print players can work
        player_selected.append(temp_player)
        #func_other_format_input.printplayers(input=player_selected,vtt="n",draft="n",outputlimit=1000,justpostion="",playerswap="n",extra_field_at_front="n",sellplayer="n")
        #print ("deleting ",createdraft[whom_shall_we_remove])
        del createdraft[whom_shall_we_remove]

    elif picklogic=="gk":
        index_to_delete=0
        position=""
        counter=0
        createdraft.sort(key=lambda createdraft: createdraft[13], reverse=True)
        for i in createdraft:
            position=i[0]
            if position == "Gk":
                break
            counter=counter+1
        try:
            temp_player=list(createdraft[counter])
        except Exception as e:
            print (e)
            breakpoint()
        player_selected.append(temp_player)
        #func_other_format_input.printplayers(input=player_selected,vtt="n",draft="n",outputlimit=1000,justpostion="",playerswap="n",extra_field_at_front="n",sellplayer="n")
        #print ("player ",createdraft[counter])
        del createdraft[counter]
    elif picklogic=="def":
        index_to_delete=0
        position=""
        counter=0
        createdraft.sort(key=lambda createdraft: createdraft[13], reverse=True)
        for i in createdraft:
            position=i[0]
            if position == "Def":
                break
            counter=counter+1
        temp_player=list(createdraft[counter])
        player_selected.append(temp_player)
        #func_other_format_input.printplayers(input=player_selected,vtt="n",draft="n",outputlimit=1000,justpostion="",playerswap="n",extra_field_at_front="n",sellplayer="n")
        #print ("player ",createdraft[counter])
        del createdraft[counter]


    elif picklogic=="mid":
        index_to_delete=0
        position=""
        counter=0
        createdraft.sort(key=lambda createdraft: createdraft[13], reverse=True)
        for i in createdraft:
            position=i[0]
            if position == "Mid":
                break
            counter=counter+1
        temp_player=list(createdraft[counter])
        player_selected.append(temp_player)
        #func_other_format_input.printplayers(input=player_selected,vtt="n",draft="n",outputlimit=1000,justpostion="",playerswap="n",extra_field_at_front="n",sellplayer="n")
        #print ("player ",createdraft[counter])
        del createdraft[counter]

    elif picklogic=="ata":
        index_to_delete=0
        position=""
        counter=0
        createdraft.sort(key=lambda createdraft: createdraft[13], reverse=True)
        for i in createdraft:
            position=i[0]
            if position == "Ata":
                break
            counter=counter+1
        temp_player=list(createdraft[counter])
        player_selected.append(temp_player)
        #print ("player ",createdraft[counter])
        del createdraft[counter]
        #func_other_format_input.printplayers(input=player_selected,vtt="n",draft="n",outputlimit=1000,justpostion="",playerswap="n",extra_field_at_front="n",sellplayer="n")


    elif picklogic=="pot":
        createdraft.sort(key=lambda createdraft: createdraft[14], reverse=True)
        #func_other_format_input.printplayers(input=createdraft[0],vtt="y",draft="n",outputlimit=1000,justpostion="",playerswap="n",extra_field_at_front="n",sellplayer="n")
        whom_shall_we_remove=random.randint(0,3)
        temp_player=list(createdraft[whom_shall_we_remove])
        player_selected.append(temp_player)
        #func_other_format_input.printplayers(input=player_selected,vtt="n",draft="n",outputlimit=1000,justpostion="",playerswap="n",extra_field_at_front="n",sellplayer="n")
        del createdraft[whom_shall_we_remove]

    elif picklogic=="fla":
        pass

    else:
         input ("Woops")

def count_outofcontactplayers(squad):

        numberofplayers=0
        temp_copy_of_squad=squad.copy()
        for index,i in enumerate(temp_copy_of_squad):
            if i[15]==0:
                numberofplayers+=1
        return numberofplayers




def draft_clearup (developmentsquad):

    # we don't want the list of undrafted rookies getting to big year after year
    # so lets do some tidying up...

    # we will remove :
    #anyone over 34 
    #anyone age over 23 and vtt and potential under 60
    #delete any one over 300(in lookup) , randomize the list and keep popinng the last one until we have 300

    #anyone over 24 in dev squad get releasted
    ########################## 22032019
    newplayer_for_dev_squad=""
    for index,player in enumerate(developmentsquad):
        try:
            p_age=player[3]
        except Exception as e:
            print ("Oops")
            print (e)
            breakpoint
        p_position=player[0]
        if p_age >23:
            if p_position =="Gk":
                newplayer_for_dev_squad=func_other_create_players.createplayers(gk=1, defender=0, mid=0, ata=0, qualityofplayer=50, maxageofplayer=21, minageofplayer=18, ef="abc",draftlist="n",developmentsquad="y")
            if p_position  =="Def":
                newplayer_for_dev_squad=func_other_create_players.createplayers(gk=0, defender=1, mid=0, ata=0, qualityofplayer=50, maxageofplayer=21, minageofplayer=18, ef="abc",draftlist="n",developmentsquad="y")

            if p_position  =="Mid":
                newplayer_for_dev_squad=func_other_create_players.createplayers(gk=0, defender=0, mid=1, ata=0, qualityofplayer=50, maxageofplayer=21, minageofplayer=18, ef="abc",draftlist="n",developmentsquad="y")

            if p_position  =="Ata":
                newplayer_for_dev_squad=func_other_create_players.createplayers(gk=0, defender=0, mid=0, ata=1, qualityofplayer=50, maxageofplayer=21, minageofplayer=18, ef="abc",draftlist="n",developmentsquad="y")
            #breakpoint() 
            newplayer_for_dev_squad=newplayer_for_dev_squad[0]
            developmentsquad[index]=newplayer_for_dev_squad



    # lets stop this getting over messey and create a new list
    global defscore
    global atascore
    global master_undrafted_rookies
    master_undrafted_rookies=undrafted_rookies.copy()
    #this is top stop the index getting misalligned
    number_of_player_removed=0

    #lets age player

    for index,i in enumerate(undrafted_rookies):
        tempage=i[3]
        tempvtt=i[13]
        temppot=i[14]
        if tempage >= 34:
            del master_undrafted_rookies[index-number_of_player_removed]
            number_of_player_removed+=1
            #print ("deleting...",i)
        elif tempage > 23 and (tempvtt < 60 and temppot <60):
            del master_undrafted_rookies[index-number_of_player_removed]
            number_of_player_removed+=1
            #print ("deleting...",i)
        else:
            pass # player is ok to stay

    if len(master_undrafted_rookies) > func_other_game_settings.size_of_undrafted_class:
        random.shuffle(master_undrafted_rookies)
        while len(master_undrafted_rookies) > func_other_game_settings.size_of_undrafted_class:
            master_undrafted_rookies.pop()

    freeagents= func_other_create_players.createplayers(gk=func_other_game_settings.freeagency_gk, defender=func_other_game_settings.freeagency_def, mid=func_other_game_settings.freeagency_mid, ata=func_other_game_settings.freeagency_ata, qualityofplayer=func_other_game_settings.inital_top_range_player_freeagency, maxageofplayer=34, minageofplayer=27, ef="abc",draftlist="y",freeagent="y")
    #func_other_format_input.printplayers(freeagents,draft="n",outputlimit=100,justpostion="")
    for player in master_undrafted_rookies:
        # tidying up contracts as now undrafted rookies so contact length should be 1
        # under 25's i.e undrafted rookies rather than free agents contract length = 1
        if player[16]==0:
            player[16]=1
        if player[3]<25:
            player[15]=1
            
    master_undrafted_rookies=master_undrafted_rookies+freeagents
    #print (len(master_undrafted_rookies))
    #print ()
    #print (master_undrafted_rookies)
    #input("W2")


    return developmentsquad
        
    
def sign_uncontractedplayers(squad,developmentsquad):
    #print(master_undrafted_rookies)

    global defscore
    global atascore

    
    input("\nYou have no more draft picks, moving onto the final steps of the draft process")


    while True:
        func_clear_screen.clear_screen()
        func_other_header.header(status="esd", season=season, game=game,defscore=defscore, atascore=atascore)
        print("You know have the final chance to make changes to your squad before the new season\n\nPress\nh Help Menu\no View your Squad\nx First XI Team report\ns to sign undrafted/free agents \nr Renew/release (out of contract players)\nq quit draft page and start the new season (i.e continue) ")
        numberofplayers_outofcontract=count_outofcontactplayers(squad)
        if int(numberofplayers_outofcontract)!=0:
            print ("\n***You cannot continue unless you relase/renew the out of contract players***")
            print ("**Press r to release/renew those players**")
        print ("\nOut of contract players...(%s)"%(numberofplayers_outofcontract))
            

        print ("\nMoney Summary...\n")
        func_other_menu.finance_report(squad)
        breakhit11=0

        userinput7=input()
        if userinput7=="h":
            func_clear_screen.clear_screen()
            func_other_header.header(status="esd", season=season, game=game,defscore=defscore, atascore=atascore)
            func_other_menu.menu(oursquad=squad, formation=1442, printoutput="y")
            continue

        if userinput7=="s":
                    breakhit11=0
                    printoutput="n"
                    defscore, atascore = func_other_teamreport.report(squad, formation, printoutput)
                    func_clear_screen.clear_screen()
                    func_other_header.header(status="esd", season=season, game=game,defscore=defscore, atascore=atascore)

                    print("This is your last chance to improve your squad before the new season, you cannot exceed your budget though doing it...")

                    print("Press: \nh Help menu\no View our Squad\nx First XI Team Report\np for top players by potential\nv by value to team(default view) \nf by Flawed players\nu See Undrafted Players\ny Sign a player")
                    print ("\nMoney Summary...\n")
                    func_other_menu.finance_report(squad)

                    #view_draft_valuetoteam()
                    userinput1=input("")
                    if userinput1=="h":
                        func_clear_screen.clear_screen()
                        func_other_header.header(status="esd", season=season, game=game,defscore=defscore, atascore=atascore)
                        func_other_menu.menu(oursquad=squad, formation=1442, printoutput="y")
                        continue
                    if userinput1=="u":
                        func_clear_screen.clear_screen()
                        func_other_header.header(status="esd", season=season, game=game,defscore=defscore, atascore=atascore)
                        players_under_24=[]
                        for uplayer in master_undrafted_rookies:
                            playersage=uplayer[3]
                            if playersage < 25:
                                players_under_24.append(uplayer)
                        players_under_24.sort(key=lambda players_under_24: players_under_24[13],reverse=True)
                        print ("Top 15 players under 25 sorted by VTT")
                        func_other_format_input.printplayers(players_under_24,draft="n",outputlimit=15,justpostion="",playerswap="n",extra_field_at_front="n")
                        print ()
                        print ("Top 15 players under 25 sorted by Potential")
                        players_under_24.sort(key=lambda players_under_24: players_under_24[14],reverse=True)
                        func_other_format_input.printplayers(players_under_24,draft="n",outputlimit=15,justpostion="",playerswap="n",extra_field_at_front="n")




                    if userinput1=="x":
                        func_clear_screen.clear_screen()
                        func_other_header.header(status="esd", season=season, game=game,defscore=defscore, atascore=atascore)
                        func_other_teamreport.report(oursquad=squad, formation=1442, printoutput="y")
                        input ("\nPress enter to continue")
                        breakhit11=1
                        continue
                    if userinput1=="o":
                        func_clear_screen.clear_screen()
                        func_other_header.header(status="esd", season=season, game=game,defscore=defscore, atascore=atascore)
                        func_other_format_input.printplayers(squad,draft="n",outputlimit=100,justpostion="")
                        print ("\nHere Is your Development squad\n")
                        func_other_format_input.printplayers(developmentsquad,draft="n",outputlimit=100,justpostion="")
                        input("Press a button to conitnue")
                        breakhit11=1
                    if userinput1=="p":
                        func_clear_screen.clear_screen()
                        func_other_header.header(status="esd", season=season, game=game,defscore=defscore, atascore=atascore)
                        view_draft_potential(fa="y")
                        input("Press a button to conitnue")
                        breakhit11=1
                        #continue
                    elif userinput1=="v":
                        func_clear_screen.clear_screen()
                        func_other_header.header(status="esd", season=season, game=game,defscore=defscore, atascore=atascore)
                        view_draft_valuetoteam(fa="y")
                        input("Press a button to conitnue")
                        breakhit11=1
                        #continue
                    elif userinput1=="f":
                        func_clear_screen.clear_screen()
                        func_other_header.header(status="esd", season=season, game=game,defscore=defscore, atascore=atascore)
                        view_draft_flawed_genius(fa="y")
                        input("Press a button to conitnue")
                        breakhit11=1
                        #continue
                    elif userinput1=="y":
                        maxbudget,players_wages,maxbudget_minus_players_wages=func_other_menu.finance_report(squad,returnv="y")
                        # inital safety check
                        under24_triggered=0
                        if maxbudget_minus_players_wages < 0:
                            print ("You do not have enough money to sign any players")
                            input()
                            breakhit11=1
                            userinput1a=""
                            input("Returning you to main menu, press enter to continue")
                            continue
                        else:
                            userinput1a=input("Order by VTT(default) or (p)potenital or (u) Age under 24 -undrafted players via PA,(g) Age under 24 -undrafted players via VTT (a)all players sorted by position,(s)Special skill,(v) Players between 6-8 cost  ")
                            func_clear_screen.clear_screen()
                            func_other_header.header(status="esd", season=season, game=game,defscore=defscore, atascore=atascore)
                        if userinput1a == "v":
                            print("These are the players you can sign ...(between 6-8 cost)")
                            global count_pb46
                            count_pb46=0

                            #messey but creating my own sort so higher values for anything between 5 and 8
                            def sort_list_temp(x):
                                global count_pb46
                                tx=x[16]
                                if tx  < 5:
                                    return tx + 150
                                elif tx > 8:
                                    return tx + 100
                                else:
                                    count_pb46+=1
                                    return tx

                            #outputlimit=int(count_pb46)
                            outputlimit=45
                            master_undrafted_rookies.sort(key=sort_list_temp)
                            func_other_format_input.printplayers(master_undrafted_rookies,draft="ydc",outputlimit=int(count_pb46),justpostion="")



                        elif userinput1a == "g":
                            print("These are the top 45 players you can sign ...(Ordered by vtt)")
                            under24_triggered=1
                            under_24_temp_list=[]
                            for i in master_undrafted_rookies:
                                if int(i[3]) < 24:
                                    under_24_temp_list.append(i)
                            if len(under_24_temp_list)<45:
                                outputlimit=int(len(under_24_temp_list))
                            else:
                                outputlimit=45
                            under_24_temp_list.sort(key=lambda under_24_temp_list: under_24_temp_list[13],reverse=True)
                            func_other_format_input.printplayers(under_24_temp_list,draft="ydc",outputlimit=outputlimit,justpostion="")
                        elif userinput1a == "u":
                            print("These are the top 45 players you can sign ...(Ordered by potential)")
                            under24_triggered=1
                            under_24_temp_list=[]
                            for i in master_undrafted_rookies:
                                if int(i[3]) < 24:
                                    under_24_temp_list.append(i)
                            if len(under_24_temp_list)<45:
                                outputlimit=int(len(under_24_temp_list))
                            else:
                                outputlimit=45
                            under_24_temp_list.sort(key=lambda under_24_temp_list: under_24_temp_list[14],reverse=True)
                            func_other_format_input.printplayers(under_24_temp_list,draft="ydc",outputlimit=outputlimit,justpostion="")
                            
                        elif userinput1a == "p":
                            print("These are the players you can sign ...(Ordered by potential)")
                            outputlimit=30
                            master_undrafted_rookies.sort(key=lambda master_undrafted_rookies: master_undrafted_rookies[14],reverse=True)
                            func_other_format_input.printplayers(master_undrafted_rookies,draft="ydc",outputlimit=outputlimit,justpostion="")
                        elif userinput1a == "s":
                            print("These are the players you can sign ...(Ordered by Special skill)")
                            outputlimit=45
                            master_undrafted_rookies.sort(key=lambda master_undrafted_rookies: master_undrafted_rookies[17],reverse=True)
                            func_other_format_input.printplayers(master_undrafted_rookies,draft="ydc",outputlimit=outputlimit,justpostion="")

                        elif userinput1a == "a":
                            print("These are the players you can sign ...(Ordered by position)")
                            master_undrafted_rookies.sort(key=lambda master_undrafted_rookies: master_undrafted_rookies[0],reverse=True)
                            outputlimit=999
                            func_other_format_input.printplayers(master_undrafted_rookies,draft="ydc",outputlimit=outputlimit,justpostion="")
                        else:
                            print("These are the players you can sign ...(Ordered by VTT)")
                            outputlimit=45
                            master_undrafted_rookies.sort(key=lambda master_undrafted_rookies: master_undrafted_rookies[13],reverse=True)
                            func_other_format_input.printplayers(master_undrafted_rookies,draft="ydc",outputlimit=outputlimit,justpostion="")
                        print ()
                        whom_to_sign_fa=input("enter the number of the player you want to sign or r to choose a differnt sort option ")

                        if (whom_to_sign_fa=="r") or not whom_to_sign_fa.isdigit():

                            input ("Unexpected input returning you to previous menu")
                            continue
                        else:
                            try:
                                whom_to_sign_1=int(whom_to_sign_fa)
                                whom_to_sign_fa=int(whom_to_sign_fa)
                            except ValueError:
                                pass
                                input ("Bad input returning you to previous menu")

                        #max output not matching greater than
                        #so increment again and force error
                        if whom_to_sign_fa == outputlimit:
                            whom_to_sign_fa+=1

                        valid_answer1=func_other_errorchecking.checkinput(number="y",char="n",min=0,max=outputlimit,userinput=whom_to_sign_fa,listinput="")
                        if valid_answer1=="True":
                            if under24_triggered==1:
                                try:
                                    posttion_new_draft_pick=under_24_temp_list[whom_to_sign_fa]
                                except:
                                    print ("Erroed")
                                    breakpoint()
                            else:
                                posttion_new_draft_pick=master_undrafted_rookies[whom_to_sign_fa]
                            age_new_pick=posttion_new_draft_pick[3]
                            
                            posttion_new_draft_pick=posttion_new_draft_pick[0]

                            # if over 24 straight into main squad, if under either into dev squad or main squad
                            if age_new_pick < 24:
                                wheretoplaceplayer=input("As the player is under 24 , do you want to place the player in the development squad (default) or the main squad (d/m)?")
                                if wheretoplaceplayer=="m":
                                    pass
                                    # break out of this loop & follow normal logic for squad
                                else:
                                    func_other_format_input.printplayers(developmentsquad,vtt="y",draft="ydc",outputlimit=100,justpostion=posttion_new_draft_pick)
                                    if posttion_new_draft_pick=="Gk":
                                        min_post_num=0
                                        max_post_num=1
                                        add_values=0
                                    elif posttion_new_draft_pick=="Def":
                                        min_post_num=1
                                        max_post_num=2
                                        add_values=1
                                    elif posttion_new_draft_pick=="Mid":
                                        min_post_num=1
                                        max_post_num=2
                                        add_values=3
                                    elif posttion_new_draft_pick=="Ata":
                                        min_post_num=1
                                        max_post_num=2
                                        add_values=5
                                    else:
                                        print ("Oops")
                                        breakpoint()
                                    userinput6=input("Who do you wish to replace? between %s - %s, or if you want to return and draft a different enter an invalid number " %(min_post_num,max_post_num))
                                    try:
                                        userinput6=int(userinput6)
                                        valid_answer6=func_other_errorchecking.checkinput(number="y",char="n",min=min_post_num,max=max_post_num,userinput=userinput6,listinput="")
                                    except:
                                        valid_answer6="False" 
                                            
                                    if valid_answer6=="True":
                                        #because we had a modified draft the delete will be a bit more compllicated
                                        player_to_delete6=int(userinput6)+add_values
                                        player_to_select_wages6=master_undrafted_rookies[whom_to_sign_fa][16]
                                        #logic on player to delete check wages and contract
                                        player_to_delete_wages6=developmentsquad[player_to_delete6][16]
                                        player_to_delete_contract6=developmentsquad[player_to_delete6][15]
                                        increase_wages6=round((player_to_delete_wages6*player_to_delete_contract6)/2)

                                        # exttra logic based on sort option 
                                        # normal sort
                                        if under24_triggered==0:
                                            del developmentsquad[player_to_delete6]
                                            playerselected6=master_undrafted_rookies[whom_to_sign_fa]
                                            del master_undrafted_rookies[whom_to_sign_fa]
                                            #edit players contract length and wage to reflect draft position
                                            developmentsquad.insert(player_to_delete6,playerselected6)
                                            breakhit11=1
                                            continue
                                        #just under 24 sort (u)
                                        # no unique ref for a player so i need to do a detailed comparrision
                                        else:
                                            found=0
                                            #########################2103019
                                            #userinput6=userinput6-1
                                            #player_i_want=under_24_temp_list[userinput6]
                                            player_i_want=under_24_temp_list[whom_to_sign_1]
                                            #player_i_want=master_undrafted_rookies[userinput6]
                                            player_i_want_post=player_i_want[0]
                                            player_i_want_fname=player_i_want[1]
                                            player_i_want_sname=player_i_want[2]
                                            player_i_want_age=player_i_want[3]
                                            player_i_want_gkskill=player_i_want[4]
                                            player_i_want_defskill=player_i_want[5]
                                            player_i_want_ataskill=player_i_want[6]
                                            player_i_want_vtt=player_i_want[13]
                                            player_i_want_pot=player_i_want[14]

                                            num_found=0

                                            for index,playeriwant in enumerate(master_undrafted_rookies):
                                                #breakpoint()
                                                if (str(playeriwant[0])==str(player_i_want_post)) and (str(playeriwant[1])==str(player_i_want_fname)) and (str(playeriwant[2])==str(player_i_want_sname)) and (playeriwant[3]==player_i_want_age) and (playeriwant[4]==player_i_want_gkskill) and (playeriwant[5]==player_i_want_defskill) and (playeriwant[6]==player_i_want_ataskill) and (playeriwant[13]==player_i_want_vtt) and (playeriwant[14]==player_i_want_pot):
                                                    whom_to_sign_fa=index
                                                    found=1
                                                    num_found+=1
                                                    #print (" i am adding", player_i_want)
                                                    #check=input("Happy?(n)")
                                                    #if check=="n":
                                                    #    breakpoint()
                                            if found==1:
                                                del developmentsquad[player_to_delete6]
                                                playerselected6=master_undrafted_rookies[whom_to_sign_fa]
                                                del master_undrafted_rookies[whom_to_sign_fa]
                                                #edit players contract length and wage to reflect draft position
                                                #input("Woomba")
                                                #breakpoint()
                                                developmentsquad.insert(player_to_delete6,playerselected6)
                                                breakhit11=1
                                                input("\nChange to Development Squad done, press enter to continue")
                                                continue

                                            else:
                                                print ("No match found err...?!")
                                                breakpoint()
                                            



                                    else:
                                        input ("That is invalid number please try again...(i a going to return you to the player draft menu)")
                                        breakhit1=1
                                        continue

                                    
                           
                            #pass continues here
                            #func_other_format_input.printplayers(squad,vtt="y",draft="ydc",outputlimit=100,justpostion=posttion_new_draft_pick)
                            if under24_triggered==1:
                                    posttion_new_draft_pick=under_24_temp_list[whom_to_sign_fa]
                            else:
                                posttion_new_draft_pick=master_undrafted_rookies[whom_to_sign_fa]
                            age_new_pick=posttion_new_draft_pick[3]
                            posttion_new_draft_pick=posttion_new_draft_pick[0]


                            func_other_format_input.printplayers(squad,vtt="y",draft="ydc",outputlimit=100,justpostion=posttion_new_draft_pick)

                            if posttion_new_draft_pick=="Gk":
                                min_post_num=0
                                max_post_num=2
                                add_values=0
                            elif posttion_new_draft_pick=="Def":
                                min_post_num=1
                                max_post_num=8
                                add_values=2
                            elif posttion_new_draft_pick=="Mid":
                                min_post_num=1
                                max_post_num=8
                                add_values=10
                            elif posttion_new_draft_pick=="Ata":
                                min_post_num=1
                                max_post_num=5
                                add_values=18
                            else:
                                print ("Oops")
                                breakpoint()
                            userinput5=input("Who do you wish to replace? between %s - %s, or if you want to return and draft a different enter an invalid number " %(min_post_num,max_post_num))

                            try:
                                userinput5=int(userinput5)
                                valid_answer5=func_other_errorchecking.checkinput(number="y",char="n",min=min_post_num,max=max_post_num,userinput=userinput5,listinput="")
                            except:
                                valid_answer5="False"
                            #breakpoint() 

                            if valid_answer5=="True":
                                player_to_delete2=int(userinput5)+add_values
                                if under24_triggered==1:
                                    player_to_select_wages=under_24_temp_list[whom_to_sign_fa][16]
                                    #playerselected6[17]="U"
                                else:    
                                    player_to_select_wages=master_undrafted_rookies[whom_to_sign_fa][16]
                                #logic on player to delete check wages and contract
                                player_to_delete_wages=squad[player_to_delete2][16]
                                player_to_delete_contract=squad[player_to_delete2][15]
                                increase_wages=round((player_to_delete_wages*player_to_delete_contract)/2)

                                if player_to_delete_contract ==0 or player_to_delete_wages==1:
                                    pass
                                    # out of contract or 1£ million wage budget
                                else:
                                    player_to_select_wages=player_to_select_wages+increase_wages
                                    print ("\nbecause this player has a %s year contract on %s per year left" %(player_to_delete_contract,player_to_delete_wages))
                                    print ("Our players wages will have to be increased by ",increase_wages)
                                    print ("So in total the new players wages will be ", player_to_select_wages)
                                    proceed_iw=input("Do you wish to carry on proceed?(y/(n)")
                                    if proceed_iw =="y":
                                        master_undrafted_rookies[whom_to_sign_fa][16]=player_to_select_wages
                                        if under24_triggered==1:
                                            under_24_temp_list[whom_to_sign_fa][16]=player_to_select_wages
                                    else:
                                        continue

                                if under24_triggered==0:
                                    del squad[player_to_delete2]
                                    playerselected=master_undrafted_rookies[whom_to_sign_fa]
                                    del master_undrafted_rookies[whom_to_sign_fa]
                                    #edit players contract length and wage to reflect draft position
                                    squad.insert(player_to_delete2,playerselected)
                                    breakhit11=1
                                    defscore, atascore = func_other_teamreport.report(squad, formation, printoutput)
                                    input("\nChange to Squad done,press enter to continue")
                                    continue
                                else:
                                    found=0
                                    try:
                                        ############userinput5 is wrong 05032019 player_to_delete2
                                        #player_i_want=under_24_temp_list[userinput5]
                                        #player_to_delete2=player_to_delete2+add_values
                                        player_i_want=under_24_temp_list[whom_to_sign_fa]
                                    except:
                                        print ("Error Error")
                                        breakpoint()
                                    player_i_want_post=player_i_want[0]
                                    player_i_want_fname=player_i_want[1]
                                    player_i_want_sname=player_i_want[2]
                                    player_i_want_age=player_i_want[3]
                                    player_i_want_gkskill=player_i_want[4]
                                    player_i_want_defskill=player_i_want[5]
                                    player_i_want_ataskill=player_i_want[6]
                                    player_i_want_vtt=player_i_want[13]
                                    player_i_want_pot=player_i_want[14]
                                    for index1,playeriwant1 in enumerate(master_undrafted_rookies):
                                        if (str(playeriwant1[0])==str(player_i_want_post)) and (str(playeriwant1[1])==str(player_i_want_fname)) and (str(playeriwant1[2])==str(player_i_want_sname)) and (playeriwant1[3]==player_i_want_age) and (playeriwant1[4]==player_i_want_gkskill) and (playeriwant1[5]==player_i_want_defskill) and (playeriwant1[6]==player_i_want_ataskill) and (playeriwant1[13]==player_i_want_vtt) and (playeriwant1[14]==player_i_want_pot):
                                            whom_to_sign_ur=index1
                                            found=1
                                    if found==1:
                                        #player_to_delete2=player_to_delete2+add_values
                                        del squad[player_to_delete2]
                                        playerselected=under_24_temp_list[whom_to_sign_fa]
                                        playerselected[17]="U"
                                        del master_undrafted_rookies[whom_to_sign_ur]
                                        #edit players contract length and wage to reflect draft position
                                        squad.insert(player_to_delete2,playerselected)
                                        breakhit11=1
                                        defscore, atascore = func_other_teamreport.report(squad, formation, printoutput)
                                        input("\nChange to Squad done,press enter to continue")
                                        continue

                                    else:
                                        print ("No match found err...?!")
                                        breakpoint()


                            else:
                                input ("That is invalid number please try again...(i a going to return you to the player draft menu)")
                                breakhit1=1


                        



                    else:
                        if breakhit11==1:
                            continue
                        else:
                            input("Enter a valid button ")
                            continue



        if userinput7=="q":
            if int(numberofplayers_outofcontract)!=0:
                input("You need to release/renew all your players contacts before you continue (press o to renew/release your players)")
                continue
            else:
                global player_selected
                player_selected=[]
                return(squad,developmentsquad)
                #break
        if userinput7=="r":
            func_clear_screen.clear_screen()
            func_other_header.header(status="esd", season=season, game=game,defscore=defscore, atascore=atascore)
            #breakpoint()
            squad,developmentsquad=renewplayercontract(squad,developmentsquad)
            #breakpoint()
            input("Press a button to conitnue")
            continue
        if userinput7=="o":
            func_clear_screen.clear_screen()
            func_other_header.header(status="esd", season=season, game=game,defscore=defscore, atascore=atascore)
            print ("\nHere Is your first team squad\n")
            func_other_format_input.printplayers(squad,draft="n",outputlimit=100,justpostion="")
            print ("\nHere Is your Development squad\n")
            func_other_format_input.printplayers(developmentsquad,draft="n",outputlimit=100,justpostion="")
            input("Press a button to conitnue")
            continue
        if userinput7=="x":
            func_clear_screen.clear_screen()
            func_other_header.header(status="esd", season=season, game=game,defscore=defscore, atascore=atascore)
            func_other_teamreport.report(oursquad=squad, formation=1442, printoutput="y")
            input ("\nPress enter to continue")

        else:
            if breakhit11==1:
                pass
            else:
                input("Bad input please try again...Press a button to continue")
                #breakpoint()

def record_signing_player(ppostion,pname,playerdraftinfo,playersoldinfo=""):

    global player_history

    linebuild=season,ppostion,pname,playerdraftinfo,playersoldinfo
    player_history.append(linebuild)
    #print(player_history)




def draft(game, idefscore, iatascore, squad,thisyear_firstround,nextyear_firstround,thisyear_secondround,nextyear_secondround,thisyear_thirdround,nextyear_thirdround,developmentsquad,normal_season_wins,playoff_wins,season_in,stage_po):

    first_round_pn=0
    second_round_pn=0
    third_round_pn=0
    all_round_pn=[]
    #normal_season_wins=games won
    #1 = lose in wildcard
    #2= lose in divisional
    #3 = lose in conference
    #4 = lose in superblowl
    #5 = win superbowl

    global defscore
    global atascore
    global season
    season=season_in
    
    printoutput="n"
    defscore, atascore = func_other_teamreport.report(squad, formation, printoutput)


    if stage_po==5: #superbowl win
        first_round_pn=32
    elif stage_po==4:#superbowl loss
        first_round_pn=31
    elif stage_po==3:# conference game loss
        first_round_pn=random.randint(29,30)
    elif stage_po==2: #division game loss
        first_round_pn=random.randint(24,28)
    elif stage_po==1: # wildcardloss
        first_round_pn=random.randint(16,24)
    else: # stage_po==0 # no playoffs
        if int(normal_season_wins) ==0:
            first_round_pn=1
        elif int(normal_season_wins) < 2:
            first_round_pn=random.randint(1,3)
        elif int(normal_season_wins) < 3:
            first_round_pn=random.randint(2,4)
        elif int(normal_season_wins) < 4:
            first_round_pn=random.randint(4,5)
        elif int(normal_season_wins) < 6:
            first_round_pn=random.randint(5,7)
        elif int(normal_season_wins) < 7:
            first_round_pn=random.randint(7,12)
        elif int(normal_season_wins) < 8:
            first_round_pn=random.randint(8,13)
        elif int(normal_season_wins) < 10:
            first_round_pn=random.randint(14,15)
        else:
            input("hmm that's odd")
    
    '''
    if int(normal_season_wins) ==0:
        first_round_pn=1
    elif int(normal_season_wins) < 2:
        first_round_pn=random.randint(1,3)
    elif int(normal_season_wins) < 3:
        first_round_pn=random.randint(2,4)
    elif int(normal_season_wins) < 4:
        first_round_pn=random.randint(4,5)
    elif int(normal_season_wins) < 6:
        first_round_pn=random.randint(5,7)
    elif int(normal_season_wins) < 7:
        first_round_pn=random.randint(7,12)
    elif int(normal_season_wins) < 8:
        first_round_pn=random.randint(8,13)
    elif int(normal_season_wins) < 10:
        first_round_pn=random.randint(14,15)
    elif int(playoff_wins==-1) or int(playoff_wins==0):
        first_round_pn=random.randint(16,24)
    elif int(playoff_wins==1):
        first_round_pn=random.randint(24,28)
    elif int(playoff_wins==2):
        first_round_pn=random.randint(29,30)
    elif int(playoff_wins==3):
        first_round_pn=31
    elif int(playoff_wins>3):
        first_round_pn=32
    else:
        input ("Err, not sure on whcih pick number to give you")
        breakpoint()
    '''
    
    
    all_round_pn.append(first_round_pn)
    second_round_pn=32+first_round_pn
    all_round_pn.append(second_round_pn)
    third_round_pn=64+first_round_pn
    all_round_pn.append(third_round_pn)
    
    breakhit=0
    draft_already_created=0

    #salary cap breached, bad user
    bb1=""
    bb2=""
    bb1,bb2,bad_ness=func_other_menu.finance_report(squad,returnv="y")
    if bad_ness < -14:
        print ("Because you have massivley breached salary cap rules you have had all your draft picks removed")
        input()
        all_round_pn.clear()
    elif bad_ness < -10:
        #delete first round pick
        print ("Because you have massivley breached salary cap rules you have had your first round pick removed")
        input()
        del all_round_pn[0]
    elif bad_ness < -5:
        print ("Because you have breached salary cap rules you have had your second round pick removed")
        input()
        #delete second round pick
        del all_round_pn[1]
    elif bad_ness < -1:
        print ("Because you have breached salary cap rules you have had your third round pick removed")
        input()
        #delete third round pick
        all_round_pn.pop()
    else:
        pass





    while True:
        func_clear_screen.clear_screen()
        func_other_header.header(status="esd", season=season, game=game,defscore=defscore, atascore=atascore)
        #print("Press enter to continue or m for menu,p see draft potential,v for value to team \n,f for flawed genius y View your squad, d see Full Draft , r Renew players contracts ") #userinput is accecpted further below as i wanted menu options at the top of the page and info below it
        print("Press: \nh Help menu\td Scout Draft\tv View your Squad\tx First XI Team Report\tr Change (out of contract players)\te Enter draft(i.e Continue)\ts Sell a player\tm move up/down draft board\nhd History of draft ") #userinput is accecpted further below as i wanted menu options at the top of the page and info below it


        if draft_already_created==0:
            create_draft()
            draft_already_created=1
        print ("\nThis is where you can improve your squad & Development squad through signing players in the draft/free agency as well as undrafted players & dealing with your of contract players")
        print ("There are 3 stages pre draft (sell players/trade picks) > draft (use you draft picks to get good young players) > post draft (you can sign undrafted players/free agents)")
        print ("After you enter the draft you cannot trade or sell players")
        print ("You can deal with out of contract players either before or after the draft\n")
        players_to_sell=swap_players(squad=squad,all_round_pn=all_round_pn,report="y")
        outofcontract_players(squad)
        #breakpoint()
        #developmentsquad=draft_clearup (developmentsquad)
        #breakpoint()
        money(squad)
        try:
            draftnumbers(thisyear_firstround,nextyear_firstround,thisyear_secondround,nextyear_secondround,thisyear_thirdround,nextyear_thirdround,first_round_pn, second_round_pn,third_round_pn,all_round_pn)
        except:
            print("woops something odd happened- dropping into debug")
            breakpoint()

        userinput=input("")
        if userinput=="hd":
            func_clear_screen.clear_screen()
            func_other_header.header(status="esd", season=season, game=game,defscore=defscore, atascore=atascore)
            global player_history
            print ("Previous draft picks")
            #breakpoint()
            print ("\nSeason  P   Name            Pick Num")
            for i in player_history:
                tseason=i[0]
                tp=i[1]
                tname=i[2]
                tpicknumber=i[3]
                print ('{:<7}{:<6}{:<16}{:<12}'.format(tseason,tp,tname,tpicknumber))

            input()
            continue
        if userinput=="h":
            func_clear_screen.clear_screen()
            func_other_header.header(status="esd", season=season, game=game,defscore=defscore, atascore=atascore)
            func_other_menu.menu(oursquad=squad, formation=1442, printoutput="y")
            continue
        if userinput=="m":
            func_clear_screen.clear_screen()
            func_other_header.header(status="esd", season=season, game=game,defscore=defscore, atascore=atascore)
            picks=move_up_down_draft(all_round_pn)
            continue
            
        if userinput=="e":
            func_clear_screen.clear_screen()
            func_other_header.header(status="esd", season=season, game=game,defscore=defscore, atascore=atascore)
            squad=enter_draft(all_round_pn,squad,developmentsquad)
            #breakpoint()
            developmentsquad=draft_clearup (developmentsquad)
            #breakpoint()
            try:
                squad,developmentsquad=sign_uncontractedplayers(squad,developmentsquad)
            except Exception as e:
                print ("Something went wrong, dropping to debug mode")
                print (e)
                breakpoint()
            #breakpoint()

            break


        if userinput=="s":
            count_all_round_pn=len(all_round_pn)
            if count_all_round_pn >= max_draft_picks_allowed:
                print ("\nYou have to many picks already please move up the draft to create a spot (you can have %s at max)" %(max_draft_picks_allowed))
            else:
                func_clear_screen.clear_screen()
                func_other_header.header(status="esd", season=season, game=game,defscore=defscore, atascore=atascore)
                newpicks_received=""
                squad,developmentsquad,newpicks_received=sell_player(squad,players_to_sell,developmentsquad)
                try:
                    if newpicks_received != "":
                        all_round_pn.append(int(newpicks_received))
                except ValueError as e:
                    print (e)
                    breakpoint()
                    pass

            input("Press a button to continue")
            continue

        if userinput=="d":
            func_clear_screen.clear_screen()
            func_other_header.header(status="esd", season=season, game=game,defscore=defscore, atascore=atascore)
            print("Press enter to continue or: \np for top players by potential\nv value to team(default view) \nf Flawed\ns for (manual) sort\n ") #userinput is accecpted further below as i wanted menu options at the top of the page and info below it
            
            view_draft_valuetoteam()
            userinput1=input("")
            if userinput1=="p":
                func_clear_screen.clear_screen()
                func_other_header.header(status="esd", season=season, game=game,defscore=defscore, atascore=atascore)
                view_draft_potential()
                input("Press a button to conitnue")
                continue
            elif userinput1=="v":
                func_clear_screen.clear_screen()
                func_other_header.header(status="esd", season=season, game=game,defscore=defscore, atascore=atascore)
                view_draft_valuetoteam()
                input("Press a button to conitnue")
                continue
            elif userinput1=="f":
                func_clear_screen.clear_screen()
                func_other_header.header(status="esd", season=season, game=game,defscore=defscore, atascore=atascore)
                view_draft_flawed_genius()
                input("Press a button to conitnue")
                continue
            elif userinput1=="s":
                func_clear_screen.clear_screen()
                func_other_header.header(status="esd", season=season, game=game,defscore=defscore, atascore=atascore)
                userinput2=input ("Enter an option to sort by : \n\nA -age\nGS -Goalkeeper skill\nDS -Defense Skill\nAS -Attack Skill\nF -Fitness\nAb -Ability\nC -Char\nD -Determination\nL -Luck\nE -experience\nVTT -Value to team\nPA -Potential Ability\ne To exit\n")
                if userinput2=="e":
                    continue
                else:
                    userinput3=input ("Enter a position i.e Gk/Def/Mid/Ata to filter by leave blank for all\n")

                    if userinput3 in ("Gk","Def","Mid","Ata"):
                        jp=userinput3
                    else:
                        jp=""

                
                    if userinput2=="A":
                        createdraft.sort(key=lambda createdraft: createdraft[3], reverse=True)
                    if userinput2=="GS":
                        createdraft.sort(key=lambda createdraft: createdraft[4], reverse=True)
                    if userinput2=="DS":
                        createdraft.sort(key=lambda createdraft: createdraft[5], reverse=True)
                    if userinput2=="AS":
                        createdraft.sort(key=lambda createdraft: createdraft[6], reverse=True)
                    if userinput2=="F":
                        createdraft.sort(key=lambda createdraft: createdraft[7], reverse=True)
                    if userinput2=="Ab":
                        createdraft.sort(key=lambda createdraft: createdraft[8], reverse=True)
                    if userinput2=="C":
                        createdraft.sort(key=lambda createdraft: createdraft[9], reverse=True)
                    if userinput2=="D":
                        createdraft.sort(key=lambda createdraft: createdraft[10], reverse=True)
                    if userinput2=="L":
                        createdraft.sort(key=lambda createdraft: createdraft[11], reverse=True)
                    if userinput2=="E":
                        createdraft.sort(key=lambda createdraft: createdraft[12], reverse=True)
                    if userinput2=="VTT":
                        createdraft.sort(key=lambda createdraft: createdraft[13], reverse=True)
                    if userinput2=="PA":
                        createdraft.sort(key=lambda createdraft: createdraft[14], reverse=True)



                    func_other_format_input.printplayers(createdraft,draft="y",outputlimit=200,justpostion=jp)
                    

                    
                input("Press a button to conitnue")
                continue
            else:
                input("Enter a valid button ")
        if breakhit==1:
            break

            #continue

        if userinput=="v":
            func_clear_screen.clear_screen()
            func_other_header.header(status="esd", season=season, game=game,defscore=defscore, atascore=atascore)
            print ("\nHere Is your first team squad\n")
            func_other_format_input.printplayers(squad,draft="n",outputlimit=100,justpostion="")
            print ("\nHere Is your Development squad\n")
            func_other_format_input.printplayers(developmentsquad,draft="n",outputlimit=100,justpostion="")
            input("Press a button to conitnue")
            continue

        if userinput=="r":
            func_clear_screen.clear_screen()
            func_other_header.header(status="esd", season=season, game=game,defscore=defscore, atascore=atascore)
            #27032019
            #squad,developmentsquad=renewplayercontract(squad,developmentsquad)
            input("Press a button to conitnue")
            continue

        if userinput=="x":
            func_clear_screen.clear_screen()
            func_other_header.header(status="esd", season=season, game=game,defscore=defscore, atascore=atascore)
            func_other_teamreport.report(oursquad=squad, formation=1442, printoutput="y")
            input ("\nPress enter to continue")
            continue


        else:
            #pass
            input("Enter a valid button ")
        
if __name__=="__main__":
    print ("***Script Called Directley****\n")

    defscore=99
    atascore=99

    print("Enter A to test draft function (check draft pick based on regular season wins and play off wins")
    ui=input("")
    if ui =="A":
        game= 0
        idefscore= 90,
        iatascore = 95 
        squad= [['Gk', 'Jonathon', 'Graves', 32, 86, 10, 7, 15, 17, 20, 15, 14, 23, 94, 85, 1, 10, 'ST'], ['Gk', 'Kendall', 'Cisneros', 21, 49, 2, 2, 11, 9, 16, 18, 17, 7, 61, 69, 0, 1, ''], ['Gk', 'Elvis', 'Singleton', 23, 88, 1, 8, 17, 16, 17, 20, 20, 12, 99, 88, 3, 10, 'D'], ['Def', 'Ollie', 'Matthews', 23, 3, 80, 52, 17, 13, 20, 20, 19, 12, 93, 86, 3, 9, 'D'], ['Def', 'Connie', 'Payne', 21, 10, 44, 21, 17, 11, 14, 11, 9, 7, 62, 58, 0, 1, ''], ['Def', 'Harold', 'Davila', 25, 5, 49, 25, 15, 20, 20, 20, 13, 15, 73, 96, 0, 2, ''], ['Def', 'Warner', 'Wallace', 22, 9, 89, 48, 10, 19, 20, 20, 20, 8, 91, 98, 1, 4, 'D'], ['Def', 'Williams', 'Sanchez', 21, 6, 66, 23, 12, 18, 16, 12, 18, 4, 72, 80, 0, 1, ''], ['Def', 'Mac', 'Moon', 30, 9, 92, 42, 14, 20, 18, 14, 17, 16, 96, 88, 1, 11, 'ST'], ['Def', 'Brandon', 'Sutton', 33, 8, 80, 37, 12, 17, 17, 13, 17, 21, 86, 80, 2, 7, 'ST'], ['Def', 'Garry', 'Luna', 27, 7, 63, 28, 6, 20, 20, 20, 15, 16, 73, 98, 3, 4, 'ST'], ['Mid', 'Nathan', 'Lyons', 24, 6, 68, 55, 15, 19, 10, 20, 13, 4, 71, 82, 0, 1, ''], ['Mid', 'Christoper', 'Stevens', 24, 10, 68, 97, 17, 20, 7, 20, 20, 12, 93, 84, 1, 7, 'D'], ['Mid', 'Shawn', 'Benjamin', 23, 4, 38, 41, 20, 15, 13, 6, 7, 4, 58, 57, 0, 1, ''], ['Mid', 'Daren', 'Hartman', 24, 6, 84, 68, 19, 19, 16, 19, 20, 8, 91, 92, 1, 4, 'D'], ['Mid', 'Francisco', 'Gallagher', 38, 6, 32, 33, 11, 20, 16, 17, 18, 25, 58, 90, 0, 3, 'ST'], ['Mid', 'Damien', 'Nolan', 24, 7, 71, 71, 16, 14, 19, 20, 17, 10, 86, 85, 3, 7, 'U'], ['Mid', 'Deon', 'Rodriguez', 20, 2, 44, 40, 12, 17, 13, 13, 20, 7, 60, 76, 0, 1, ''], ['Mid', 'Jamaal', 'Travis', 21, 3, 88, 83, 20, 20, 20, 12, 20, 6, 95, 90, 2, 4, 'D'], ['Ata', 'Ezekiel', 'Jenkins', 20, 10, 1, 89, 9, 20, 18, 20, 14, 6, 86, 94, 2, 4, 'D'], ['Ata', 'Lazaro', 'Lam', 23, 10, 1, 88, 20, 20, 14, 20, 14, 12, 100, 90, 3, 10, 'D'], ['Ata', 'Guillermo', 'Henry', 21, 3, 7, 71, 20, 19, 9, 20, 20, 4, 84, 84, 3, 4, 'D'], ['Ata', 'Mose', 'Villanueva', 23, 10, 7, 87, 18, 20, 16, 20, 16, 10, 98, 93, 0, 4, 'D'], ['Ata', 'Edmond', 'Norris', 33, 9, 10, 98, 20, 19, 20, 19, 20, 26, 100, 97, 3, 10, 'ST']]
        thisyear_firstround = 1 
        nextyear_firstround= 1 
        thisyear_secondround= 1 
        nextyear_secondround= 1 
        thisyear_thirdround= 1 
        nextyear_thirdround= 1 
        developmentsquad= [['Gk', 'Granville', 'Peterson', 24, 42, 5, 6, 18, 12, 8, 10, 6, 4, 52, 56, 1, 1, ''], ['Gk', 'Issac', 'Lin', 21, 46, 10, 8, 15, 16, 16, 19, 13, 4, 58, 79, 1, 1, ''], ['Def', 'Eduardo', 'Walters', 24, 3, 43, 20, 13, 7, 13, 5, 6, 4, 51, 48, 1, 1, ''], ['Def', 'Guadalupe', 'Avila', 20, 5, 44, 23, 7, 7, 19, 5, 13, 3, 47, 55, 1, 1, ''], ['Mid', 'Ruben', 'Wilkinson', 19, 6, 38, 28, 17, 7, 19, 7, 5, 1, 47, 62, 1, 1, ''], ['Mid', 'Sergio', 'Jacobs', 22, 2, 47, 37, 5, 20, 14, 7, 20, 3, 48, 70, 1, 1, ''], ['Ata', 'Jefferson', 'Rosas', 20, 2, 2, 42, 7, 14, 13, 10, 12, 2, 46, 58, 1, 1, ''], ['Ata', 'Harris', 'Morton', 24, 4, 5, 40, 20, 10, 7, 12, 9, 2, 56, 56, 1, 1, '']]
        normal_season_wins= 14
        playoff_wins= 1
        season_in= 6
    
        draft(game, idefscore, iatascore, squad,thisyear_firstround,nextyear_firstround,thisyear_secondround,nextyear_secondround,thisyear_thirdround,nextyear_thirdround,developmentsquad,normal_season_wins,playoff_wins,season_in)
        


    else:
        print ("No valid input entered")



    squad= [['Gk', 'Leon', 'Thomon', 27, 54, 1, 1, 8, 14, 13, 19, 9, 5, 61, 62, 1, 3, ''], ['Gk', 'Milan', 'Gill', 29, 69, 8, 10, 18, 7, 11, 15, 16, 6, 77, 60, 1, 6, ''], ['Gk', 'Phil', 'French', 22, 66, 1, 1, 5, 6, 13, 18, 19, 4, 67, 52, 1, 4, ''], ['Def', 'Davit', 'Newbury', 27, 3, 51, 29, 14, 9, 8, 15, 6, 5, 59, 50, 1, 2, ''], ['Def', 'Brogan', 'Whitehouse', 30, 2, 59, 26, 6, 16, 9, 8, 20, 7, 62, 58, 1, 3, ''], ['Def', 'Louis', 'Stewart', 26, 8, 70, 14, 7, 6, 8, 10, 9, 5, 62, 38, 3, 3, ''], ['Def', 'Mychal', 'Scott', 35, 6, 54, 26, 5, 17, 15, 20, 6, 8, 60, 66, 1, 3, ''], ['Def', 'Ada', 'Green ', 27, 3, 60, 32, 6, 17, 18, 14, 11, 7, 64, 71, 2, 3, ''], ['Def', 'Ace', 'Njoku', 18, 2, 63, 23, 16, 5, 11, 6, 6, 1, 62, 46, 2, 3, ''], ['Def', 'Luke ', 'Edge', 27, 10, 66, 13, 11, 9, 14, 14, 14, 6, 69, 60, 2, 4, ''], ['Def', 'Travis', 'Major', 18, 10, 62, 35, 13, 11, 10, 5, 10, 2, 61, 52, 1, 3, ''], ['Mid', 'Ace', 'Norcross', 29, 3, 63, 35, 6, 5, 20, 12, 11, 5, 52, 55, 1, 1, ''], ['Mid', 'Paisley', 'Watson', 35, 9, 51, 37, 9, 6, 7, 16, 16, 8, 55, 44, 1, 2, ''], ['Mid', 'Louis', 'Parry', 19, 6, 53, 69, 6, 6, 13, 19, 11, 1, 56, 50, 1, 2, ''], ['Mid', 'Antoni', 'Atterbury', 22, 9, 63, 69, 16, 7, 11, 20, 12, 4, 72, 59, 3, 5, ''], ['Mid', 'Dana', 'Njoku', 23, 5, 37, 45, 9, 18, 18, 11, 16, 3, 52, 76, 3, 1, ''], ['Mid', 'Shay', 'Ealy', 32, 7, 44, 60, 20, 20, 14, 19, 16, 6, 74, 88, 3, 5, ''], ['Mid', 'Josh', 'Nickel', 33, 9, 41, 38, 8, 9, 18, 16, 19, 5, 52, 66, 1, 1, ''], ['Mid', 'Ethan', 'Archer', 30, 7, 54, 63, 13, 15, 13, 20, 13, 5, 68, 72, 1, 4, ''], ['Ata', 'Alfa  ', 'Ali', 23, 5, 8, 70, 6, 6, 11, 14, 14, 6, 65, 46, 1, 4, ''], ['Ata', 'Corvert', 'Asher', 31, 7, 7, 63, 15, 7, 9, 20, 16, 6, 72, 57, 3, 5, ''], ['Ata', 'Genard', 'Read', 25, 10, 8, 67, 16, 14, 7, 20, 17, 4, 75, 66, 3, 6, ''], ['Ata', 'Donald', 'Parry', 30, 1, 3, 50, 15, 8, 17, 6, 16, 5, 62, 64, 3, 3, ''], ['Ata', 'Goran', 'Meyer', 33, 6, 6, 60, 11, 13, 9, 12, 15, 7, 66, 58, 1, 4, '']]

    #developmentsquad = [['Gk', 'Randy', 'Adey', 20, 50, 5, 10, 17, 9, 18, 7, 11, 4, 57, 66, 1, 1, ''], ['Gk', 'Omar', 'Bolton', 20, 69, 8, 6, 8, 7, 17, 8, 13, 2, 65, 54, 1, 1, ''], ['Def', 'Tank', 'Ireland', 19, 9, 67, 12, 12, 7, 10, 14, 5, 2, 63, 47, 1, 1, ''], ['Def', 'Miguel', 'Thomon', 20, 3, 55, 18, 8, 15, 15, 12, 18, 3, 59, 68, 1, 1, ''], ['Mid', 'Jan', 'Laing', 18, 6, 48, 45, 16, 9, 11, 17, 11, 1, 57, 60, 1, 1, ''], ['Mid', 'Hans', 'Swenney', 22, 7, 66, 48, 10, 19, 9, 15, 13, 4, 62, 66, 1, 1, ''], ['Ata', 'Minik', 'Watson', 18, 1, 4, 68, 11, 5, 11, 12, 20, 1, 65, 51, 1, 1, ''], ['Ata', 'Hugo', 'Bello', 22, 6, 1, 64, 17, 5, 5, 11, 18, 6, 71, 46, 1, 1, '']]


    #undrafted_rookies=[['Gk', 'Mychal', 'Hawkins', 22, 80, 1, 2, 10, 18, 5, 17, 11, 1, 68, 69, 1, 0,''], ['Ata', 'Ari', 'Cox', 35, 7, 6, 80, 10, 8, 16, 16, 17, 1, 68, 64, 2, 0,''], ['Ata', 'Wayne', 'Bauer', 20, 1, 9, 75, 16, 9, 12, 16, 20, 1, 68, 63, 2, 0,''],['Gk', 'Mychal1', 'Hawkins1', 22, 80, 1, 2, 10, 18, 5, 17, 11, 1, 68, 69, 1, 0,''], ['Ata', 'Ari1', 'Cox1', 24, 7, 6, 80, 10, 8, 16, 16, 17, 1, 68, 30, 2, 0,''], ['Ata', 'Wayne1', 'Bauer1', 24, 1, 9, 75, 16, 9, 12, 16, 20, 1, 40, 40, 2, 0,'']]
    undrafted_rookies=[['Gk', 'Mychalg', 'Hawkins', 22, 81, 1, 2, 10, 18, 5, 17, 11, 1, 67, 69, 1, 0,''], ['Def', 'Arid', 'Coxd', 18, 7, 6, 82, 10, 8, 16, 16, 17, 1, 70, 64, 2, 0,''], ['Mid', 'Waynem', 'Bauer', 20, 1, 9, 75, 16, 9, 12, 16, 20, 1, 68, 63, 2, 0,''],['Ata', 'Mychala', 'Hawkins1', 22, 83, 1, 2, 10, 18, 5, 17, 11, 1, 74, 69, 1, 0,''], ['Ata', 'Ari1', 'Cox1', 24, 7, 6, 85, 10, 8, 16, 16, 17, 1, 77, 30, 2, 0,''], ['Ata', 'Wayne1', 'Bauer1', 24, 1, 9, 75, 16, 9, 12, 16, 20, 1, 40, 40, 2, 0,'']]


    #draft_clearup ()
    #squad,developmentsquad=sign_uncontractedplayers(squad,developmentsquad)

    
    developmentsquad=[['Gk', 'Ahmed', 'Banks', 24, 61, 9, 1, 18, 11, 5, 17, 11, 1, 66, 56, 1, 1, ''], ['Gk', 'Brogan', 'Rice', 19, 70, 10, 6, 11, 6, 16, 20, 19, 2, 72, 64, 1, 1, ''], ['Def', 'Alexis', 'Ford', 19, 10, 52, 33, 14, 16, 13, 7, 14, 2, 60, 68, 1, 1, ''], ['Def', 'Ada', 'Smith', 21, 3, 65, 25, 9, 11, 6, 18, 5, 2, 60, 46, 1, 1, ''], ['Mid', 'Martin', 'Abacus', 19, 2, 63, 55, 18, 18, 11, 19, 5, 1, 68, 74, 1, 1, ''], ['Mid', 'Ada', 'Ireland', 23, 6, 44, 48, 20, 14, 6, 17, 10, 3, 62, 64, 1, 1, ''], ['Ata', 'Alfa  ', 'Amor', 19, 8, 3, 63, 10, 14, 20, 20, 5, 1, 64, 80, 1, 1, ''], ['Ata', 'Carlos', 'Harper', 22, 8, 4, 54, 9, 14, 9, 14, 11, 3, 56, 56, 1, 1, '']]
    print (developmentsquad) 

    draft_clearup (developmentsquad)
    
    print (developmentsquad) 



    #import func_other_create_players
    #squad=func_other_create_players.createplayers(gk=3, defender=8, mid=8, ata=4, qualityofplayer=99, maxageofplayer=35, minageofplayer=18, ef="abc",draftlist="y")
    #draft(season=1, game=2, defscore=3, atascore=4, squad=squad)

    #print ("Test draft logic")
    #enter_draft(picks=1)

    """
    print ("Value of player test")
    vtt=99
    player_value=value_players(vtt)
    print (player_value)

    print ("\nLarge bulk test\n")
    print ("VTT, Player_Points,pick offer, nicer terms \n")
    for i in range(70,101):
        print (i,end=' ')
        player_value=value_players(i)
        print (player_value,end=' ')
        pick=draft_offer(player_value)
        print (pick,end=' ')
        if pick == 0 or pick is None :
            print (" ")
        else:
            if 1 <= int(pick) <=3:
                print ("Top 3 First round pick")
            elif 4 <= int(pick) <=16:
                print ("First round middle pick")
            elif 16 <= int(pick) <=32:
                print ("Later First round pick")
            elif 32 <= int(pick) < 64:
                print ("Second round pick")
            elif 64 <= int(pick) < 97:
                print ("Third round pick")
            else:
                print (" ")
    """


