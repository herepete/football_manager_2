#!/usr/bin/python3

import os
import func_other_teamreport
import func_other_game_text
import os
from func_other_game_settings import maxbudget
import func_other_create_players

def finance_report(oursquad,returnv="n"):

    #oursquad = input to add up
    #returnv = return values (used in free agency signing to make sure values are not breached

    players_wages=0
    for i in oursquad:
        wage=int(i[16])
        players_wages+=wage
    
    if returnv=="n":
        print ("Finance report")
        print ("Budget=",maxbudget)
        print ("Players wages=",players_wages)
        print ("Money left over=",maxbudget-players_wages)
    else:
        return(maxbudget,players_wages,maxbudget-players_wages)

def End_of_Season_Draft_text():
    print ("""
    So you have played a season and here is your chance to wheel and deal and improve your team.
    The broad steps are:
    1) pre draft - you are given 3 draft picks based on your previous seasons perforamnce , you can Move up and down draft, sell players for extra draft picks , renew/release players
    2) draft - use your draft picks to aquire new players 
    3) post draft - Sign free agents, sign undrafted players to improve the development squad, make final descsions on renew/relasing players.
    4) all finished of to the next season for you

    a few notes:
    you can only sell players for draft picks if they have 1 year or more left on their contact
    you can exceed the budget during the draft but not when siging free agents or renewing contracts



    """)
    input("Press a button to continue")

def development_squad_text():

    print (""" the main squad consists of 3 GK, 8 Def, 8 Mid, 5 Ata
    the Development squad constsits of 2 GK, 2 Def, 2 Mid, 2 Ata (players can only be under 24 years old in the dev squad)
    the Dev Squad is designed as a place to store good young players not good enough to get into the main squad at the moment
    Dev squad players are all on 1 year contract for 1£
    Dev squad players have no impact on the wage bill (unless they are promoted)
    You cannot move a player back to the Dev squad after they have been promoted

    When you release/sell a player you will need to promote a member of your Dev squad.
    After the draft has finished you can sign new undrafted players to replace members of your dev squad

    If you don't have the time/energy/intrest to play with new dev players, after the draft has finished , you can auto release all out of contract players and replace them with random players    
    When the dev players get to old they will be released.


                                         
    

    """)  

def training_info():

    print ("""
     Bill Belichick 'Talent sets the floor, character sets the ceiling.'
     Napoleon 'I would rather have lucky generals than good ones.'

    Total team score  x = Average Fitness of Squad + Average Char of Squad  Average local Determination of squad + Average ability of squad + average exp of squad
    Positional Rating x = positions average exp + positions average ability + positions average char + (positions special players *20) + (positions good players *10)
    
    player rating x =

    contribution to increase:
    team score =20%
    Positional Rating = 40%
    player rating =40%

    Top increase is 5% per year
    Anyone over 30 will increasingley lose skills for every year
    Depending on luck/char/randomness some players will lose skills
    """)




def players_potential():

    print ("""

Highest is 100 this is caculated in func_other_create_players.py
pa=round((char*1.50)+(determination/2)+(luck/2)+(ability*1.5)+fitness)

Example 
char    15 * 1.5 =22.5 
Det     15 / 2   =7.5
Char    10 * 1.5 =15
Abil    15 * 1.5 =22.5
Fitness 10       =10
Total Potential  = 77.5 (rounded to 78)  

    """)

def player_vtt():

    print ("""
Highest is 100 & here is how its made up

            GK  Def  Ata Fit Luc Det Abi exp
GK          70   0    0   10  5   5   5   5
DEF         0    60   0   20  5   5   5   5
MID         0    30   30  20  5   5   5   5
ATA         0    0    60  20  5   5   5   5

Fitness is quite a large part as its an easy variable to increase/decrease, throughout the season
to reflect injuries/age this can also play an intresting part in non drafted/out of contract players moving into the next season

from func_other_teamreport.vtt
    """)

def players_contracts():

    print("""
    Subject to change but 

VTT(contract-renewal) VTT(Free Agents) Wage  Contract(for draft players)     Notes
                      100               14
                                        13
                      95                12
                                        11
100                   90                10
95                                      9
90                    85                8
85                                      7
80                    80                6
75                    75                5      4                            Players seclected in Top 3 pick in draft
70                    70                4      4                            Players seclected in Rest of 1st Round of draft
65                    65                3      3                            Players seclected in Second Round of draft
60                    60                2      2                            Players seclected in Third Round of draft
55                    55                1      1                            Players seclected in Anyone in dev Squad,Anyone undrafted

draft players wages "./func_endofseason_draft.py" [Modified] line 1180 of 2223    
free agents func_other_create_players.py

Notes
====

you may have to pay a higher salary if you are replacing a player with 1 year or more left on the contract or a wage of above 1
1 year contract renewal has a preium of +1 (unless wage is 5 and then its +2)
2 year contract as above
3 year contract renewal -1

As above the top Tier of Free agents have a premium

Over age of 32 free agents you can initally only sign on a 1 year

The idea is to get you to draft young players and make them the nucules of your squad
A few Free agents spinglinged here and there can improve a team
As per the Nfl when a draft prospect from the 1st round reaches the end of the a contract there can be a heafty jump in wages

    """)

def  special_char ():

    print ("""

    Special chars meaning, by default is blank
                               Notes
    D =Drafted                 Means a better renewal wage unless they fall into GT/ST status
    U =Undrafted 
    ST=Special trainer         player_exp+player_ablity+player_char)> 48 , Large help in potential improvements to other team mates in same position as player
    GT=Good trainer            player_exp+player_ablity+player_char)> 43   helps in potential improvements to other team mates in same position as player





    """)

def menu(oursquad, formation, printoutput):

    '''

    input = oursquad, formation, printoutput
    output depends on option choosen
    This is a co-ordinator for calling other reports/rules etc
    It appears at the bottom of every page and aims to offer uniformity in the menu

    '''

    #os.system('clear')

    useroption=input("For help on ... Press:\nr for rules\na for player attribute breakdown\nf for finance \nd for draft logic\nt for training info \ne End of Season -Draft\nds for Development + Squad\npc for Players contracts\npp Caculating player Potential\npv Caculating players value to team (vtt)\nsc Special Char notes")
    
    if useroption == "d" or useroption == "r":
        input ("To code")
        input ("\nPress enter to continue")
    if useroption == "t":
        training_info()
        input ("\nPress enter to continue")
    if useroption == "pv":
        player_vtt()
        input ("\nPress enter to continue")
    if useroption == "pp":
        players_potential()
        input ("\nPress enter to continue")
    if useroption == "pc":
        players_contracts()
        input ("\nPress enter to continue")
    if useroption == "ds":
        development_squad_text()
        input ("\nPress enter to continue")
    if useroption == "e":
        End_of_Season_Draft_text()
    elif useroption == "a":
        func_other_game_text.player_atrributes()
        input ("\nPress enter to continue")
    elif useroption == "f":
        finance_report(oursquad)
        input ("\nPress enter to continue")
    elif useroption == "sc":
        special_char()
        input ("\nPress enter to continue")
    else:
        print ("Nothing entered")
    


if __name__=="__main__":
    print ("***Script Called Directley****")
    print ("***Unit testing****")

    #squad=[['Gk ', 'Chris   ', 'Kindred      ', 30, '89 ', '1  ', '7  ', '72 ', '5  ', '10 ', '12 ', '15 ', '1  '], ['Gk ', 'Marko   ', 'Park         ', 29, '91 ', '3  ', '5  ', '90 ', '7  ', '16 ', '11 ', '6  ', '1  '], ['Gk ', 'Bobby   ', 'Ford         ', 24, '92 ', '8  ', '3  ', '81 ', '13 ', '6  ', '18 ', '5  ', '1  '], ['Def', 'Merlin  ', 'Payne        ', 22, '6  ', '79 ', '10 ', '71 ', '20 ', '7  ', '6  ', '6  ', '1  '], ['Def', 'Ada     ', 'Hubbard      ', 27, '5  ', '88 ', '34 ', '81 ', '8  ', '7  ', '12 ', '8  ', '1  '], ['Def', 'Mitchel ', 'Clark        ', 29, '5  ', '88 ', '26 ', '82 ', '17 ', '7  ', '14 ', '6  ', '1  '], ['Def', 'Austin  ', 'Rogers       ', 23, '4  ', '85 ', '40 ', '60 ', '13 ', '15 ', '14 ', '16 ', '1  '], ['Def', 'Steven  ', 'Robert       ', 29, '4  ', '81 ', '49 ', '94 ', '12 ', '11 ', '8  ', '18 ', '1  '], ['Def', 'Ben     ', 'Forrest      ', 24, '8  ', '91 ', '20 ', '74 ', '9  ', '11 ', '6  ', '20 ', '1  '], ['Def', 'Mateo   ', 'Bird         ', 18, '7  ', '80 ', '21 ', '91 ', '8  ', '17 ', '18 ', '12 ', '1  '], ['Def', 'Luke    ', 'Ortiz        ', 19, '5  ', '96 ', '32 ', '99 ', '15 ', '19 ', '6  ', '18 ', '1  '], ['Mid', 'Ari     ', 'Read         ', 35, '9  ', '84 ', '97 ', '69 ', '15 ', '20 ', '19 ', '7  ', '1  '], ['Mid', 'Louis   ', 'Grace        ', 31, '9  ', '65 ', '86 ', '91 ', '6  ', '13 ', '11 ', '9  ', '1  '], ['Mid', 'Jenson  ', 'Ellis        ', 34, '10 ', '94 ', '61 ', '60 ', '5  ', '19 ', '14 ', '19 ', '1  '], ['Mid', 'Tank    ', 'Jackson      ', 33, '1  ', '75 ', '81 ', '65 ', '14 ', '5  ', '14 ', '5  ', '1  '], ['Mid', 'Noel    ', 'Dawson       ', 34, '7  ', '52 ', '54 ', '62 ', '18 ', '12 ', '15 ', '9  ', '1  '], ['Mid', 'Samuel  ', 'Graham       ', 29, '3  ', '85 ', '56 ', '89 ', '9  ', '20 ', '15 ', '6  ', '1  '], ['Mid', 'Callam  ', 'Sharp        ', 29, '7  ', '83 ', '89 ', '94 ', '7  ', '11 ', '12 ', '11 ', '1  '], ['Mid', 'Omar    ', 'Carter       ', 24, '7  ', '54 ', '92 ', '85 ', '17 ', '12 ', '14 ', '6  ', '1  '], ['Ata', 'Goran   ', 'Duncan       ', 30, '8  ', '2  ', '80 ', '96 ', '12 ', '19 ', '20 ', '15 ', '1  '], ['Ata', 'Junior  ', 'Fells        ', 29, '8  ', '2  ', '99 ', '74 ', '18 ', '8  ', '9  ', '13 ', '1  '], ['Ata', 'Tom     ', 'Plato        ', 33, '5  ', '9  ', '80 ', '80 ', '6  ', '19 ', '15 ', '7  ', '1  '], ['Ata', 'Jens    ', 'Janis        ', 35, '7  ', '8  ', '86 ', '87 ', '5  ', '6  ', '8  ', '16 ', '1  '], ['Ata', 'Hans    ', 'Fox          ', 25, '1  ', '3  ', '80 ', '83 ', '7  ', '11 ', '20 ', '15 ', '1  ']]

    squad=func_other_create_players.createplayers(gk=3, defender=8, mid=8, ata=4, qualityofplayer=99, maxageofplayer=35, minageofplayer=18, ef="abc")



    menu(oursquad=squad, formation=1442, printoutput="y")
