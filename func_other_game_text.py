#!/usr/bin/python3

import os


def intro(printrules="n"):
    '''
    Part of getting the "Intro" section in place...


    Welcome the user with the rules & how things work...
    input intro()
    output is printed
    

    '''

    newteam = 0
    teamiwant = "random"
    players = ""
    print("""Welcome to Football Manager Draft
===============
This game is a mashup of football and NFL
The aim of the game is to win the Superbowl
And to give you 30ish mins of fun.

Each game will by default last 20 seasons (a lot of these seeing can be changed through pressing a)
You will be given a randomised poor squad at the begening of the game.

A squad constist of 3 Goalkeeper,8 Defenders,7 Midfielders & 6 Atackers
Your team score is based on the skill ratings of your top 11 players in a 4-4-2 formation.

Typically a top team score is 100.

If you draw a game the game will go to overtime to try and force a result.

You will play 16 games in a season and if you win enough games you will enter the playoffs (depending on the number of wins you will enter at a different point)
The playoff has 4 rounds, with the 4th being the Superbowl.

After the season has finished your players will lose/gain skill based on age/character/experience of other players in the squad/luck/ability.
At a random(ish!) age players skills will start to drop as they become to old (each game will have a different 'old' value)

Then you will have a chance to improve your team by drafting young players through the draft or you can swap your picks for established players.
There are 3 rounds to the draft , with the 1st Round having players with better skills.
You can swap your players for extra draft picks.
You can move up and down the draft (i.e if you have swapped your players for extra picks you can create another first or second pick, so if you have 2 great GK you could trade one for another pick to help strethen another position)

And then you start a new season.

At the top of the screen you will see a header giving you an overview of where you are in the game.


Good luck & enjoy :) 
""")

    if printrules=="n":

        userinput = input(
            "Press a to enter advanced settings or press enter to continue start the game\n")

        if userinput == "a":
            while True:
                os.system('clear')
                print("Team Choice=", teamiwant)

                whattodo = input(
                    "\nPress:\n\ne to Save & Exit this menu\n")

                if whattodo == "e":
                    break
                    #teamiwant, players = func_importrealplayers.getplayers()
                    #newteam = 1
        return(players, newteam)
        #return

def player_atrributes():
    '''

    '''
    print("""
    This is what effects players increase/decrease in skill & what is used in match day

              match day X1 | match day squad  | End of season training +- 
    ==========================================================
    |Age            N      |       N          |         Y    |  increments by 1 every year         
    |Gk skill       Y      |       N          |         N    |  can move up and down based on age and other charistics      Help defensive score    Max/Min
    |De skill       Y      |       N          |         N    |  can move up and down based on age and other charistics      Help defensive score
    |Ata skill      Y      |       N          |         N    |  can move up and down based on age and other charistics      Help Atacking score
    |Fitness        Y      |       N          |         N    |  
    |Ability        Y      |       T          |         Y    |
    |Char           Y      |       T          |         Y    |
    |Determination  Y      |       T          |         Y    |
    |Luck           Y      |       T          |         Y    |
    |Experience     Y      |       T          |         Y    |
    ==========================================================

    """)

def draftinfo():

    '''
    The draft gives you the ability to improve your squad/team with younger players
    You are given 1 pick in each of the first/second and third rounds
    The most valuable pick is number 1 (meaning you can draft any player you wish) -awarded to the worst team from the season before
    The worst pick is number 32 -awarded to the team who won the superbowl the season before
    You can sell you current players to get extra draft picks or you could trade down the draft
    If you have more than 1 pick left (assuming its not the first pick) you can trade in the picks to move up (but you would lose picks)
    To stop ending up with to many picks you are limited to 6 draft picks (in your 24 man squad that allows a 25% turnover)
    If you hit the 6 number you can trade up i.e trade 2 of your picks for 1 higher draft choice , taking the draft count down to 5
    
    You can move up and down the draft

    to add  <contracts>
    free agency
    caculating value of players (include age)
    '''

def initaldrafthelp():
    '''
    From here you can improve your team:


    
    '''


if __name__ == "__main__":
    import os
    os.system('clear')
    print ("Unit testing\n\n\n\n\n")
    intro()
    input("Press enter to continue")
    os.system('clear')
    intro(printrules="y")
    input("Press enter to continue")
    os.system('clear')
    player_atrributes()

    
    
