#!/usr/bin/python3
# this script will create a random name combining first and last names when called
# this is used in inital team creation and draft

import random
import os
import func_other_teamreport
import func_other_game_settings
import func_other_format_input
import csv
import pdb
import func_clear_screen

# Explanantion of skills


# gk = num of gk to create
# def = num of def to create
# mid = number of midfielders to create
# ata = number of attackers to create
# maxage= player can at most be this old
# exp = max experience (in draft/free agency we might allow more experience players)

# char = max Characteur of player
# gkskill = GK skill
# defskill = Defending skills
# passkill = Pass skills
# ataskill = Shooting skills
# nfskill = Natural Fitness skills
# potskill = Potential Skill
#tskill = Techique


# variables
choices = []

# logic
# pass me your variables and i will create you some players
# so create 2 gk with maxskill =20 skill =18 skillpeak=17,maxage=18 you would pass
## func_create_players.rn3(gk =2, defe =0, mid =0, ata =0, exp =0, maxskill =20, skill =18, skillpeak =17, char =0, maxage=18)
# anything with a value of 0 will create an output value of 0
# designed to hopefully allow for inital start up players, draft players and Free agency
# the format command below just adds some nice extra space to each line to make the output nicer

# def

# def playernames(numberof) 								return(firstname,lastname)
# create some random names
# def buildplayer (position,numberofplayer,qualityofplayer,maxageofplayer)
# create skill and names, calls playernames and passed info back to create players
# def createplayers(gk,defender,mid,ata,qualityofplayer)
# being called externally, call buildplayer to create the players list

#moving name creation out of the functions so its only called once (previosuley the .csv where being called multiple times per run)
first_names =[]
with open('firstnames.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        first_names.append(row)
first_names=first_names[0]
first_names=tuple(first_names)

last_names =[]
with open('surnames.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        last_names.append(row)
last_names=last_names[0]
last_names=tuple(last_names)


def playernames():
    #create a random name from a list.
    '''

    Using random.choice to choose 1 item from first_names (space padded to 8 spaces) and 1 from last_names (padded to 10 spaces)
    Function needs to be called 5 times to create 5 players

    Note no error checking takes place on input
    '''


    #first_names = ('Wayne', 'Alan', 'David', 'Stuart', 'Luke ', 'Choper', 'Alfa  ', 'Joe', 'Mike', 'Steven', 'Tim', 'Jim', 'Dana', 'Jake', 'Ben', 'Davo', 'Nick', 'Rambo', 'Seb', 'Danny', 'Josh', 'Evan', 'Caleb', 'Sven', 'Tank', 'Austin', 'Seth', 'Matt', 'Jeremy', 'Darran', 'Myles', 'Lenny', 'Chris', 'Drew', 'Donald', 'Jamar', 'Baker', 'Payton', 'Antonio', 'Dylan', 'Charlie', 'Samuel', 'Gareth', 'Liam', 'Lucas', 'Jose', 'Mateo', 'Noel', 'Adam', 'Jonas', 'Elias', 'Marko', 'Johnny', 'Harry', 'Bobby', 'Logan', 'Phil', 'Vincent', 'Randy', 'Russel', 'Gabriel', 'Louis', 'Eugene', 'Ralph', 'Jordan', 'Noah', 'Bruce', 'Ethan', 'Keith', 'Jan', 'Cameron', 'Ahmed',
     #              'Hamada', 'Jens', 'Junior', 'Omar', 'Manish', 'Jude', 'Thiago', 'Alexis', 'Elijah', 'Javier', 'Ari', 'Rawiri', 'Lukas', 'Riccardo', 'Hans', 'Leon', 'Vicktor', 'Tommaso', 'Goran', 'Zoran', 'Flyn', 'Emil', 'Davit', 'Minik', 'Carlos', 'Damion', 'Denzel', 'Mychal', 'Genard', 'Brogan', 'Derron', 'Britton', 'Ross', 'Derrick', 'Zay', 'Tom', 'Merlin', 'Milan', 'Melin', 'Ace', 'Martin', 'Martyn', 'Marvin', 'Harper', 'Jace', 'Corvert', 'Glenn', 'Dai', 'Travis', 'Tomas', 'Ayat', 'Duncan', 'Seren', 'Hassan', 'Dillan', 'Ada', 'Kiran', 'Franky', 'Mitchel', 'Shay', 'Ray', 'Jenson', 'Miguel', 'Paisley', 'Antoni', 'Hugo', 'Arlo', 'Dexter', 'Callam', 'DJ','Glen', 'Taj', 'Mungo', 'Ash', 'Ian', 'Iain', 'Iakov', 'Ike', 'Illya', 'Idriys', 'Issac', 'Ivan', 'Will', 'William', 'Wyatt', 'Wade', 'Walter', 'Wes', 'Wesley', 'Winston', 'Wiley', 'Owen', 'Oliver', 'Oscar', 'Otis', 'Oz', 'Otto', 'Olly', 'Oswin', 'Paul', 'Pat', 'Patrick', 'Phillip', 'Phoenix', 'Pierre', 'Perry', 'Pierce', 'Paco', 'Paris','Val', 'Valerie', 'Valen', 'Vadim', 'Quain', 'Quade ', 'Nacho', 'Naal', 'Nadir', 'Nario', 'Nasim', 'Nat', 'Nathaniel', 'Frank', 'Francis', 'Finn', 'Felix', 'Fabio','Freddy')

    global fn
    #making global so it can be called during testing
    fn=first_names
    #breakpoint() 
    firstname = (random.choice(first_names))

    #last_names = ('Rooney', 'Smith', 'Beckam', 'Broad ', 'Jones', 'Ford', 'Stansfield', 'Abacus', 'Plato', 'Shaw', 'Robert', 'Sping ', 'Taylor', 'Wilson', 'Bailey', 'Hoss', 'Gavate', 'Green ', 'Oneil ', 'Thomon', 'Avery', 'Chubb', 'Mayfield', 'Ward', 'Thomas', 'Scott', 'Salako', 'Reiter', 'Nassib', 'Njoku', 'Ratley', 'Schobert', 'Kindred', 'Johnson', 'Dayes', 'Ekuale', 'Fells', 'Garrett', 'Rogers', 'Price', 'Bell', 'Gibson', 'Mills', 'Booth', 'Dixon', 'Lane', 'Harper', 'Walker', 'Watson', 'Jackson', 'Davis', 'Cox', 'Fox', 'Ali', 'Hart', 'Whiteman', 'Frazer', 'Clarke', 'Clark', 'Webb', 'Kelley', 'James', 'Barnes', 'Gill', 'Hudson', 'Cook', 'Allen', 'Poole', 'Lawson', 'Stewart', 'Read', 'Reid', 'Powell', 'Barker', 'Dawson', 'Cann', 'Brooks','Anderson','Ahmed','Archer','Asher','Adey','Ainsworth','Arrowsmith','Amor','Aylot','Atterbury','Dunn','Daniel','David','Dallas','Diamond','Ducon','Drain','Duke','Denney','Donaldson','Drew','Durrant','Deans','Dreyer', 'Eyett','Emms','Edler','Earl','Ealy','Easen','Emerson','English','Edwards','Elkin','Edge','Ellard','Ireland','Irvine','Isaacs','Imran','Ingermann','Neale','Nield','Nash','North','Nedd','Neish','Norcross','Newbury','Nickel','Nicol','Owen','Ould','Oddie', 'Ellis', 'Khan', 'Carter', 'Patel', 'Adams', 'Potter', 'Bishop', 'Field', 'Payne', 'Bolton', 'Hardy', 'Parry', 'Marsh', 'Burns', 'French', 'Park', 'Forrest', 'Banks', 'Lynch', 'Sharp', 'Bates', 'Riley', 'Atkins', 'Love', 'Hawkins', 'Duncan', 'Byrne', 'Pritchard', 'Simmons', 'Perry', 'Fabino', 'Orchard', 'Vogel', 'Rice', 'Berry', 'Cajuste', 'Tretter', 'Robinson', 'Bello', 'Currie', 'Grace', 'Gay', 'Stanton', 'Janis', 'Sankoh', 'Caldwell', 'Hubbard', 'Graham', 'Wagner', 'Stanley', 'Cunningham', 'Kennedy', 'Lee', 'Holt', 'Lowe', 'Ozel', 'Swenney', 'Weaver', 'Whyte', 'Black', 'Shelton', 'Olsen', 'Ortiz', 'Howarth', 'Pasons', 'Major', 'Corben', 'Bird', 'Santos', 'Whitehouse', 'Mccoy', 'Meyer', 'Laing', 'Blair', 'Bauer', 'Baver', 'Garze','Quinn', 'Quirk', 'Quintion', 'Quigley', 'Quirke', 'Yang', 'Yallop', 'Yard', 'Yeoman', 'Yeung', 'Young', 'York', 'Yeomans', 'Zaoui', 'Tagg', 'Tait', 'Tillett', 'Tomlin', 'Tollis', 'Tetlow', 'Tallon', 'Tapp', 'Tolmay', 'Tarr','Ibbs', 'Iddon', 'Ilet', 'Ingleby', 'Inker', 'Inglefield', 'Isbitt', 'Isherwoord', 'Irwin', 'Jacobs', 'Jewitt', 'John', 'Johansen', 'Jobson', 'Johnston', 'Jarman', 'Juey', 'Jowitt', 'Kalton', 'Kaul', 'Kirk', 'Kirkham', 'Keyte', 'Keys', 'Key', 'Kett', 'Keal', 'Keane', 'Kiddell' ,'Last')

    lastname = (random.choice(last_names))
    global ln
    ln = last_names

    return(firstname, lastname)

def player_wage(age,vtt,draft="n",round="1"):

    '''
    Helps us work out the contract value of a player based on age/value to team/is the person part of a draft 
    '''

    vttvalue=vtt

    if draft=="y":
        if round=="T1":
               wage=5
        elif round=="1":
               wage=4
        elif round=="2":
               wage=3
        elif round=="3":
               wage=2
        #undrafted
        else:
               wage=1

    # if draft = no , so normal players    
    else:

        if vttvalue  <55:
            wage=1
        elif vttvalue  <60:
            wage=2
        elif vttvalue  <65:
            wage=3
        elif vttvalue  <70:
            wage=4
        elif vttvalue  <75:
            wage=5
        elif vttvalue  <80:
            wage=6
        elif vttvalue  <85:
            wage=8
        elif vttvalue  <90:
            wage=10
        elif vttvalue  <95:
            wage=12
        else:
            wage=14

    
    return wage
    

def buildplayer(position, numberofplayer, qualityofplayer, maxageofplayer, minageofplayer,draftlist,developmentsquad="n",freeagent="n"):
    #This is where the magic of player creation happpens!
    '''

    This is the core function for player creation
    The following are supplied: position, numberofplayer, qualityofplayer, maxageofplayer, minageofplayer 
    
    And the following are created:
    P=Position - Passed as a Parameter
    A=Age - Random number between minageofplayer & maxageofplayer (both passed as parameters)
    GS=Goalkeeper Skill -Random number based on poisition and passed parameter qualityofplayer
    DS=Defense Skill -Random number based on poisition and passed parameter qualityofplayer
    AS=Attack Skill -Random number based on poisition and passed parameter qualityofplayer
    F=Fitness - Random number between 60 and 100
    A=Ability -Random number between 5 and 20
    C=Char -Random number between 5 and 20
    D=Determination -Random number between 5 and 20
    L=Luck -Random number between 5 and 20
    E=Experience - Random number between 1 and 10

    Its worth nothing that no error checking takes place on input provided
    '''


    players = []
    rangeofplayerskill = 20
    outofpositionskill = 10
    if freeagent=="y":
        semioutofposition = qualityofplayer-30
    else:
        semioutofposition = qualityofplayer/2
    semioutofposition = int(semioutofposition)
    prettyfaroutofposition = qualityofplayer/4
    prettyfaroutofposition = int(prettyfaroutofposition)

    for i in range(numberofplayer):
        # add intelligence to stop above range having problems at the lower end
        if qualityofplayer < 40:
            qualityofplayer = 40
            semioutofposition = 30
            prettyfaroutofposition = 20


# build skill
#               rmaxskill= "{:<2}".format(random.randint (rskilln,maxskill))
#               rchar = "{:<2}".format(random.randint  (minrchar,char))

# gkskill
        if position == "Gk":
            gkskill = random.randint(
                (qualityofplayer-rangeofplayerskill), qualityofplayer)
            #print (gkskill)
        else:
            gkskill = random.randint(1, outofpositionskill)

        #gkskill = pads3(gkskill)

# defskill

        if position == "Gk":
            defskill = random.randint(1, outofpositionskill)
        elif position == "Def":
            defskill = random.randint(
                (qualityofplayer-rangeofplayerskill), qualityofplayer)

        elif position == "Mid":
            defskill = random.randint(semioutofposition, qualityofplayer)
        elif position == "Ata":
            defskill = random.randint(1, outofpositionskill)
        else:
            #print ("Err something gone wrong, poistion=",position)
            return ("I have errored") 
        #defskill = pads3(defskill)

# ataskill

        if position == "Gk":
            ataskill = random.randint(1, outofpositionskill)
        if position == "Def":
            ataskill = random.randint(outofpositionskill, semioutofposition)
        if position == "Mid":
            ataskill = random.randint(semioutofposition, qualityofplayer)
        if position == "Ata":
            ataskill = random.randint(
                (qualityofplayer-rangeofplayerskill), qualityofplayer)

        #ataskill = pads3(ataskill)
        if freeagent=="y":
            baselinevalue=12
        else:
            baselinevalue=5
# fitness
    # using semioutofposition badly named but never the less useful
        fitness = random.randint(baselinevalue, 20)
        #fitness = pads3(fitness)

# abliity
    # might need furthe tweaking lets start with this
        ability = random.randint(baselinevalue, 20)
        #ability = pads3(ability)

# char
        char = random.randint(baselinevalue, 20)
        #char = pads3(char)

# determination
        determination = random.randint(baselinevalue, 20)
        #determination = pads3(determination)

# luck
        luck = random.randint(baselinevalue, 20)
        #luck = pads3(luck)

# age
#	age=
        age = random.randint(minageofplayer, maxageofplayer)

# experience

        if freeagent=="y":
            experience = random.randint(5,15)
        elif draftlist=="y":
            experience=1
        elif age <19:
            experience = random.randint(1,2)
        elif age  <22:
            experience = random.randint(1,4)
        elif age  <26:
            experience = random.randint(3,6)
            
        else:
            experiencetemp = (age-17)
            experience = random.randint(experiencetemp,experiencetemp+3)
            if experience > 8:
                experience = random.randint(5,8)


# name

        firstname, lastname = playernames()

#potential ablity
        #player_potential        
        #formula is:
        #char 25% + det 25% + luck 10% + ability 40%
        #pa=round((char*1.25)+(determination*1.25)+(luck/2)+(ability*2))
        pa=round((char*1.50)+(determination/2)+(luck/2)+(ability*1.5)+fitness)
        #pa=""

#contract (in years)
        #if developmentsquad=="y" or age >32:
        #    contract=1
        #else:
        #    contract=random.randint(1,3)
        contract=1


# wage (in years)
        #at the moment its blank but a few lines down after the Vtt is worked out its recaculated
        wage=""

#value toteam
        vtt=""
        vtttemp=[position, firstname, lastname, age, gkskill, defskill, ataskill, fitness, ability, char, determination, luck, experience,vtt,pa,contract,wage]
        notneeded,vtt=func_other_teamreport.vtt(vtttemp)


# wage (in years)
        if freeagent=="y":
            wage=player_wage(age=age,vtt=vtt,draft="n")
        elif draftlist=="y":
            wage=0
        else:
            wage=player_wage(age=age,vtt=vtt,draft="n")
            if developmentsquad=="y":
                wage=1

#special skill
        Special_skill=""
        special_result=func_other_teamreport.special_player_check(experience,ability,char,age)
        Special_skill=special_result

# build
        # 99 edit here
        # last field after experience is a blank field which can be used further along for temp items i.e sorting player value to team
        cheat_scores2=func_other_game_settings.cheat
        if cheat_scores=="y" or cheat_scores2=="y": 
            players.append([position, firstname, lastname, age, 99, 99,99, 20, 20, 20, 20, 20, 20,vtt,pa,contract,wage,Special_skill])
        else:
            #normal route
            players.append([position, firstname, lastname, age, gkskill, defskill,
                       ataskill, fitness, ability, char, determination, luck, experience,vtt,pa,contract,wage,Special_skill])

    return(players)


def createplayers(gk, defender, mid, ata, qualityofplayer, maxageofplayer, minageofplayer, ef,draftlist="n",developmentsquad="n",freeagent="n",cheat="n"):

    # this really splits down request by position and calls the above functions
    # a list is build based on positions requested and passed back
    # ef -is an extra flag for future proofing things i have missed
    '''

    This function splits down passed parameters by position and calls the buildplayer function.

    expected input:
    gk, defender, mid, ata = int based on how many players are needed 
    qualityofplayer = 0-100
    maxageofplayer = 20-35
    minageofplayer= 18-30
    ef-is an extra flag for future proofing things i have missed
    cheat= all 99

    Note no error checking takes place on input provided

    '''
    global cheat_scores
    cheat_scores=cheat

    masterplayerslist = []
    if gk != 0:
        gkbuildlist = buildplayer(position="Gk", numberofplayer=gk, qualityofplayer=qualityofplayer,
                                  maxageofplayer=maxageofplayer, minageofplayer=minageofplayer,draftlist=draftlist,developmentsquad=developmentsquad,freeagent=freeagent)
        masterplayerslist = masterplayerslist+gkbuildlist
    if defender != 0:
        defbuildlist = buildplayer(position="Def", numberofplayer=defender, qualityofplayer=qualityofplayer,
                                   maxageofplayer=maxageofplayer, minageofplayer=minageofplayer,draftlist=draftlist,developmentsquad=developmentsquad,freeagent=freeagent)
        masterplayerslist = masterplayerslist+defbuildlist
    if mid != 0:
        midbuildlist = buildplayer(position="Mid", numberofplayer=mid, qualityofplayer=qualityofplayer,
                                   maxageofplayer=maxageofplayer, minageofplayer=minageofplayer,draftlist=draftlist,developmentsquad=developmentsquad,freeagent=freeagent)
        masterplayerslist = masterplayerslist+midbuildlist
    if ata != 0:
        atabuildlist = buildplayer(position="Ata", numberofplayer=ata, qualityofplayer=qualityofplayer,
                                   maxageofplayer=maxageofplayer, minageofplayer=minageofplayer,draftlist=draftlist,developmentsquad=developmentsquad,freeagent=freeagent)
        masterplayerslist = masterplayerslist+atabuildlist


    players = masterplayerslist
    return(players)

if __name__ == "__main__":
# allow for batch testing

    import os
    func_clear_screen.clear_screen()
    print ("#############")
    print ("To play the game run main.py this will just run some units tests on all the functions in the file")
    print ("#############")








    freeagents= createplayers(gk=func_other_game_settings.freeagency_gk, defender=func_other_game_settings.freeagency_def, mid=func_other_game_settings.freeagency_mid, ata=func_other_game_settings.freeagency_ata, qualityofplayer=99, maxageofplayer=34, minageofplayer=27, ef="abc",draftlist="y",freeagent="y")
    freeagents.sort(key=lambda freeagents: freeagents[3], reverse=True)
    #func_other_format_input.printplayers(freeagents,draft="y",outputlimit=100)
    func_other_format_input.printplayers(freeagents,vtt="n",draft="n",outputlimit=25,justpostion="",playerswap="n",extra_field_at_front="n")

    #newplayer=createplayers(gk=50000, defender=0, mid=0, ata=0, qualityofplayer=50, maxageofplayer=21, minageofplayer=18, ef="abc",draftlist="n",developmentsquad="y")
    #print (newplayer)
    #func_other_format_input.printplayers(newplayer,draft="y",outputlimit=50000)

    #to batch test
    #[root@g4 football_manager_2]# ./func_other_create_players.py  > /tmp/123 ; cat /tmp/123 | awk '{print $2, $3}' | sort | uniq -c | sort -n

    #print(fn.sort)

    print ("Summary")
    print ("=======")

    fn_sorted=sorted(fn)
    fn_count=len(fn)
    print ("there are %s first names" %(fn_count))
    
    ln_sorted=sorted(ln)
    ln_count=len(ln)
    print ("there are %s last names" %(ln_count))

    import collections
    
    def count(listOfTuple,tvalue=2):
        flag=False
        val = collections.Counter(listOfTuple) 
        uniqueList = list(set(listOfTuple)) 

        for i in uniqueList: 
            if val[i]>= tvalue: 
                flag = True
                print(i, "-", val[i]) 
              
        if flag == False: 
            print("Duplicate doesn't exist")
    print ("checking for Duplicate First name...")
    count(fn_sorted)
    print ("checking for Duplicate Last name...")
    count(ln_sorted)

    user_input=input("\n\nPress...\na to check first names\nb to batch test 10,000 players\nc to check last lastnames")
    if user_input=="a":
        for i in fn_sorted:
            print (i)
    if user_input=="b":
        print ("")
        listplayernames=[]
        for i in range (10000):
            a,b=playernames()
            fullname=a+" "+b
            listplayernames.append(fullname)
       
        newp_tupel=tuple(listplayernames)
        print ("checking for Duplicate ...(more then 4)")
        count(newp_tupel,tvalue=4)
    if user_input=="c":
        for i in ln_sorted:
            print (i)

    



    '''
    players_names_test=playernames()
    print ("testing player name creation (playernames)")
    print ("random name =", players_names_test)
    print ()
    print ("Creating 20 random name = ")
    for i in range(20):
        print (playernames())

    print ("#############")
    print ("test buildplayer")
    buildplayertest=buildplayer(position="Gk", numberofplayer=5, qualityofplayer=50, maxageofplayer=34, minageofplayer=18,draftlist="n")
    #breakpoint()
    print ()
    print ("#############")
    print ("test createplayers")
    print ("lets add all that together")
    #createplayerstest=createplayers(gk=1, defender=4, mid=4, ata=2, qualityofplayer=99, maxageofplayer=35, minageofplayer=18, ef="abc")
    #breakpoint()
    #import func_other_format_input
    #func_other_format_input.printplayers(createplayerstest)
   
    player_from_practise_squad=createplayers(gk=0, defender=0, mid=0, ata=1, qualityofplayer=80, maxageofplayer=30, minageofplayer=18, ef="abc",draftlist="",freeagent="y")
    print(player_from_practise_squad)
    '''



 
