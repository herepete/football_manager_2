#!/usr/bin/python3
import func_other_header
import func_other_menu
import os
import func_other_teamreport
import random

global playerskillchange
playerskillchange=[]



def add_experience():

    #global local_squad,local_devsquad
    #for i in local_squad:
    #    players_exp=int(i[12])+1
    #i[12]=players_exp
    pass

def add_year_to_age():

    global local_squad,local_devsquad
    #yep players get older

    for i in local_squad:
        players_age1=int(i[3])
        new_age1= players_age1+1
        i[3]=new_age1
    for j in local_devsquad:
        players_age1=int(j[3])
        new_age1= players_age1+1
        j[3]=new_age1



def remove_year_of_contract():

    #yep contracts reduce i am afraid

    global local_squad

    for i in local_squad:
        old_contract=int(i[15])
        new_contract= old_contract-1
        i[15]=new_contract

def caculate_positionrating():

    formation=1442
    #oursquad=local_squad
    
    #gp = good players,sp=special players,e=expereience,ab=ability,c=char)
    global gkgp,defgp,midgp,atagp,gksp,defsp,midsp,atasp,gke,defe,mide,atae,atae,defab,midab,ataab,gkc,defc,midc,atac

    tmasterdefscore, tmasteratascore,gkgp,defgp,midgp,atagp,gksp,defsp,midsp,atasp,gke,defe,mide,atae,gkab,defab,midab,ataab,gkc,defc,midc,atac=func_other_teamreport.report(local_squad, formation, printoutput="ft")

    #breakpoint()
   
    #for i in local_squad:
    #    print ("3",i)

    
    global gkrating,defrating,midrating,atarating
    gkrating=10+int(gke)+int(gkab)+int(gkc)+(int(gksp)*25)+(int(gkgp)*10)
    defrating=10+defe+defab+defc+(defsp*25)+(defgp*10)
    midrating=10+mide+midab+midc+(midsp*25)+(midgp*10)
    atarating=10+atae+ataab+atac+(atasp*25)+(atagp*10)

    if gkrating>99:
        gkrating=100
    if defrating>99:
        defrating=100
    if midrating>99:
        midrating=100
    if atarating>99:
        atarating=100

    print ("Positional Rating Gk =",gkrating," Out of 100")
    print ("Positional Rating Def=",defrating," Out of 100")
    print ("Positional Rating Mid=",midrating," Out of 100")
    print ("Positional Rating Ata=",atarating," Out of 100")
    print ()
    


def caculate_teamrating():

    # works out a single number rating for our team to be used to boost a players skills
    global local_teamrating_for_training
    local_teamrating_for_training=0
    local_age=0
    local_fitness=0
    local_char=0
    local_det=0
    local_abi=0
    local_exp=0

    #get squad averages (not just firstx1)
    for player in local_squad:
        local_age=int(player[3])+local_age
        local_fitness=int(player[7])+local_fitness
        local_char=int(player[9])+local_char
        local_det=int(player[10])+local_det
        local_abi=local_abi+int(player[8])
        local_exp=local_exp+int(player[12])
    local_age=int(local_age/23)
    local_fitness=int(local_fitness/23)
    local_char=int(local_char/23)
    local_det=int(local_det/23)
    local_abi=int(local_abi/23)
    local_exp=int(local_exp/23)

    #print ("Team Average Age ",local_age)
    #print ("Team Average Fitness ",local_fitness)
    #print ("Team Average Char ",local_char)
    #print ("Team Average Determination ",local_det)
    #print ("Team Average Ability ",local_abi)
    #print ("Team Average Experience ",local_exp)
    #print ()
    print ("Break down of team & position stats...\n")

    #age, every age above 18 scores a point
    local_age_score=int(local_age)
    
    #fitness every score above 13 scores a point
    local_fitness_score=int(local_fitness)

    #char anything below 15 scores minus
    local_char_score=int(local_char)

    #det
    local_det_score=int(local_det)
    
    #ability
    local_abi_score=int(local_abi)

    #exp
    local_exp_score=int(local_char)

    #add all together
    local_teamrating_for_training=local_fitness_score+local_char_score+local_det_score+local_abi_score+local_exp_score
    print ("Total team score ",local_teamrating_for_training," Out of 100")



def caculate_individal_rating(player):

    global individual_player_rating
    global player_negative_value
    global individual_player_age
    global individual_player_position

    # using players poential
    individual_player_rating=player[14]
    individual_player_age=player[3]
    individual_player_position=player[0]

    player_negative_value=100-individual_player_rating
    if individual_player_age >35:
        player_negative_value=player_negative_value+570
    elif individual_player_age >33:
        player_negative_value=player_negative_value+40
    elif individual_player_age >30:
        player_negative_value=player_negative_value+20
    else:
        pass
        #not an old player

    #print (individual_player_rating)

def print_output():

    #print output for user

    #print ("Players Increase values")
    #print ("Increase")
    #print ("Player , Before-PA , After-PA, Before-VTT,After-VTT")
    #print ("Decrease")
    #print ("Player , PA , VTT")
    pass

def change_in_skills():

    #really designed to bring down skill of older players
    # with a bit of randomness throwen in

    global skilincrease
    global player_negative_value,random_number_loss


    skilincrease=0
    random_number_loss=0

    random_number=random.randint(1,200)
    if random_number < player_negative_value:
    #decrease skills
        if individual_player_age < 30:
            random_number_loss=random.randint(1,3)
        elif individual_player_age < 33:
            random_number_loss=random.randint(3,5)
        elif individual_player_age < 34:
            random_number_loss=random.randint(3,7)
        else:
            random_number_loss=random.randint(5,15)

        #print ("Age=%s,Pr=%s,-%s "%(individual_player_age,individual_player_rating,random_number_loss))

        return("loss")
    else:
    #increase skills
        #40% of player position
        #40% players potential
        #20% team


        if individual_player_position=="Gk":
            individual_postion_rating=gkrating
        if individual_player_position=="Def":
            individual_postion_rating=defrating
        if individual_player_position=="Mid":
            individual_postion_rating=midrating
        if individual_player_position=="Ata":
            individual_postion_rating=atarating
        
        ourpositive_number=round((int(local_teamrating_for_training/100)*20)+((individual_player_rating/100)*40)+((individual_postion_rating/100)*40))
        
        if int(individual_player_age) < 22:
            completerandomnumber=random.randint(1,8)
            #completerandomnumber=6
            if completerandomnumber==5:
                bottomeskillincrease=5
                topskillincrease=10
            if completerandomnumber==6:
                bottomeskillincrease=8
                topskillincrease=12
            elif ourpositive_number <41:
                bottomeskillincrease=0
                topskillincrease=1
            elif ourpositive_number <61:
                bottomeskillincrease=2
                topskillincrease=4
            elif ourpositive_number <71:
                bottomeskillincrease=3
                topskillincrease=5
            elif ourpositive_number <81:
                bottomeskillincrease=4
                topskillincrease=6
            elif ourpositive_number <91:
                bottomeskillincrease=6
                topskillincrease=8
            else:
                bottomeskillincrease=6
                topskillincrease=9
        elif int(individual_player_age) < 25:
            if ourpositive_number <41:
                bottomeskillincrease=0
                topskillincrease=1
            elif ourpositive_number <61:
                bottomeskillincrease=0
                topskillincrease=1
            elif ourpositive_number <81:
                bottomeskillincrease=2
                topskillincrease=4
            elif ourpositive_number <91:
                bottomeskillincrease=4
                topskillincrease=5
            else:
                bottomeskillincrease=4
                topskillincrease=6
        elif int(individual_player_age) < 30:
            if ourpositive_number <41:
                bottomeskillincrease=0
                topskillincrease=1
            elif ourpositive_number <61:
                bottomeskillincrease=0
                topskillincrease=1
            elif ourpositive_number <81:
                bottomeskillincrease=1
                topskillincrease=3
            elif ourpositive_number <91:
                bottomeskillincrease=3
                topskillincrease=4
            else:
                bottomeskillincrease=3
                topskillincrease=5
        elif int(individual_player_age) < 33:
            if ourpositive_number <41:
                bottomeskillincrease=0
                topskillincrease=0
            elif ourpositive_number <61:
                bottomeskillincrease=0
                topskillincrease=0
            elif ourpositive_number <81:
                bottomeskillincrease=1
                topskillincrease=2
            elif ourpositive_number <91:
                bottomeskillincrease=2
                topskillincrease=3
            else:
                bottomeskillincrease=2
                topskillincrease=4
        else:
        #older than 33
            bottomeskillincrease=0
            topskillincrease=0


        skilincrease=random.randint(bottomeskillincrease,topskillincrease)
        #print ("Skill increase=",skilincrease)

        #print ("Age=%s,Player rating=%s,+Skill increase=%s "%(individual_player_age,individual_player_rating,skilincrease))

        return ("gain")

def print_change(lplayer,new_vtt,org_vtt,org_pa,newpa):

    #badly named this really records the change

    lplayer[13]=new_vtt

    changeinvtt=str(int(new_vtt)-int(org_vtt))
    changeinpa=str(int(newpa)-int(org_pa))
    #if (int(changeinvtt) < 0) or (int(changeinpa)<0):
    #print ("cvtt",changeinvtt)
    #print ("cpa",changeinpa)
    #    breakpoint()
    tplayerpost=lplayer[0]
    tplayerfname=lplayer[1]
    tplayersname=lplayer[2]
    tplayersage=lplayer[3]
    #print ("change, %s %s %s %s"  %(tplayerpost,tplayerfname,tplayersname,changeinvtt))
    playerskillchange.append([tplayerpost,tplayerfname,tplayersname,tplayersage,new_vtt,changeinvtt,newpa,changeinpa])

def actually_print_changes():

    print ("Here are the players who have gained/lost major skills after training...\n")

    print ('{:<4}{:<25}{:<6}{:<6}{:<6}{:<6}{:<6}'.format("P","Name","Age","CVTT","+-VTT","CPA","+-PA"))

    '''count_letters_first_name=0
    count_letters_second_name=0
    for i in playerskillchange:
        firstname=len(i[1])
        secondname=len(i[2])

        if firstname > count_letters_first_name:
            count_letters_first_name=firstname
        if secondname > count_letters_second_name:
            count_letters_second_name=secondname

    count_letters_first_name+=1
    count_letters_second_name+=1
    count_fullname_max_size=count_letters_first_name+count_letters_second_name
    print (count_fullname_max_size)'''


    for i in playerskillchange:
        tposition=i[0]
        tname=i[1]+" "+ i[2]
        tcurrentage=i[3]
        tcurrentvtt=i[4]
        tchangevtt=i[5]
        tcurrentpa=i[6]
        tchangepa=i[7]
        if (int(tchangevtt)>1) or (int(tchangepa)>1):
            print ('{:<4}{:<25}{:<6}{:<6}{:<6}{:<6}{:<6}'.format(tposition,tname,tcurrentage,tcurrentvtt,tchangevtt,tcurrentpa,tchangepa))
        elif (int(tchangevtt)<-1) or (int(tchangepa)<-1):
            print ('{:<4}{:<25}{:<6}{:<6}{:<6}{:<6}{:<6}'.format(tposition,tname,tcurrentage,tcurrentvtt,tchangevtt,tcurrentpa,tchangepa))
        else:
            pass
            #not printing player with minor changes 


def change_soft_skills(fitness,deter,char,luck,skilincrease):

    random_list=[]
    lskilincrease=skilincrease/2
    if int(lskilincrease) < 2:
        lskilincrease=random.randint(1,2)

    if fitness !=20:
        random_list.append(7)
    if deter !=20:
        random_list.append(10)
    if char !=20:
        random_list.append(9)
    if luck !=20:
        random_list.append(11)
    #check if empty
    if  random_list:

        increase_soft_skill=random.choice(random_list)
        if increase_soft_skill == 7:
            fitness=round(fitness+lskilincrease)
            if fitness>20:
                fitness=20
        elif increase_soft_skill == 10:
            deter=round(deter+lskilincrease)
            if deter>20:
                deter=20
        elif increase_soft_skill == 9:
            char=round(char+lskilincrease)
            if char>20:
                char=20
        else:
            #11
            luck=round(luck+lskilincrease)
            if luck>20:
                luck=20

    else:
        # all 20 presumable
        pass

    return (fitness,deter,char,luck)




def training(season, game, defscore, atascore, squad,devsquad,experience_gained):

    # this is what is called by main.py
    # we are going to turn everything into "global variables" 
    #so we don't need to pass data back and forth everywhere
    os.system('clear')
    func_other_header.header(status="est", season=season, game=game,defscore=defscore, atascore=atascore)

    global local_season,local_game_local_defscore,local_atascore,local_squad,local_devsquad,skilincrease,random_number_loss
    local_season=season
    local_game=game
    local_defscore=defscore
    local_atascore=atascore
    local_squad=[]
    local_squad=squad
    local_devsquad=devsquad
    
    global playerskillchange
    playerskillchange=[]


    #original values
    org_values=[]
    for k in squad:
        vtt=k[13]
        pa=k[14]
        org_values.append([vtt,pa])
        
        
    #for k1 in org_values:
    #    print (k1)
    #for tplayer in local_squad:
    #    print (tplayer)


    # here is where the magic happens, contracts -1 , age +1 ,caculating team and personal scores
    #add_experience()
    caculate_teamrating()

    #for ttplayer in local_squad:
    #    print ("2 = ",ttplayer)

    caculate_positionrating()
    for index,lplayer in enumerate(local_squad):
        # bit hacky but need to get values from before squad has been touched
        org_vtt,org_pa=org_values[index]
        #print (index,org_vtt,org_pa,lplayer)


        #add exp, was a function but getting odd errors later on with  caculate_positionrating()recaculating vtt before i need 
        
        players_exp=lplayer[12]
        players_exp+=int(experience_gained)
        lplayer[12]=int(players_exp)

        #print ("org_vtt=",org_vtt,lplayer)
        caculate_individal_rating(lplayer)
        result_of_training=change_in_skills()
        
        if result_of_training=="gain":
            #print ("Gain points")

            # change fitness/deter/char/luck (skillincrease/2 as points will go into one of these attributes)

            lplayer[7],lplayer[10],lplayer[9],lplayer[11]=change_soft_skills(fitness=lplayer[7],deter=lplayer[10],char=lplayer[9],luck=lplayer[11],skilincrease=skilincrease)
           # org_vtt=lplayer[13]
            if individual_player_position=="Gk":
                skill_level=lplayer[4]
                new_skill_level=round((skill_level/100)*skilincrease)+skill_level
                if new_skill_level >100:
                    new_skill_level=100
                lplayer[4]=new_skill_level
                notneeded,vtt=func_other_teamreport.vtt(lplayer)
                updatedplayer=func_other_teamreport.player_potential(lplayer)
                new_pa=updatedplayer[14]
                new_vtt=vtt
                if (org_vtt != new_vtt) or (org_pa !=new_pa):
                    print_change(lplayer,new_vtt,org_vtt,org_pa,new_pa)



            elif  individual_player_position=="Def":
                skill_level=lplayer[5]
                new_skill_level=round((skill_level/100)*skilincrease)+skill_level
                if new_skill_level >100:
                    new_skill_level=100
                lplayer[5]=new_skill_level

                #add attacking skills for a defender
                #if they have high defensive skills give them an extra boost of attacking skills

                a_skill_level=lplayer[6]
                if new_skill_level >90:
                    add_extra=5
                else:
                    add_extra=0
                    
                a_new_skill_level=round((skill_level/100)*skilincrease)+a_skill_level+int(add_extra)
                if a_new_skill_level >100:
                    a_new_skill_level=100
                lplayer[6]=a_new_skill_level


                notneeded,vtt=func_other_teamreport.vtt(lplayer)
                updatedplayer=func_other_teamreport.player_potential(lplayer)
                new_pa=updatedplayer[14]
                new_vtt=vtt
                if (org_vtt != new_vtt) or (org_pa !=new_pa):
                    print_change(lplayer,new_vtt,org_vtt,org_pa,new_pa)

            elif  individual_player_position=="Mid":
                skill_level=lplayer[5]
                #lplayer[5]=new_skill_level
                new_skill_level=round((skill_level/100)*skilincrease)+skill_level
                if new_skill_level >100:
                    new_skill_level=100
                lplayer[5]=new_skill_level

                skill_level=lplayer[6]
                new_skill_level=round((skill_level/100)*skilincrease)+skill_level
                if new_skill_level >100:
                    new_skill_level=100
                lplayer[6]=new_skill_level

                notneeded,vtt=func_other_teamreport.vtt(lplayer)
                updatedplayer=func_other_teamreport.player_potential(lplayer)
                new_pa=updatedplayer[14]
                new_vtt=vtt
                if (org_vtt != new_vtt) or (org_pa !=new_pa):
                    print_change(lplayer,new_vtt,org_vtt,org_pa,new_pa)


            elif  individual_player_position=="Ata":
                skill_level=lplayer[6]
                new_skill_level=round((skill_level/100)*skilincrease)+skill_level
                if new_skill_level >100:
                    new_skill_level=100
                lplayer[6]=new_skill_level
                notneeded,vtt=func_other_teamreport.vtt(lplayer)
                updatedplayer=func_other_teamreport.player_potential(lplayer)
                new_pa=updatedplayer[14]
                new_vtt=vtt
                if (org_vtt != new_vtt) or (org_pa !=new_pa):
                    print_change(lplayer,new_vtt,org_vtt,org_pa,new_pa)


            else:
                input("Err pass")
                breakpoint()

        else:
            #lose of points
            if individual_player_position=="Gk":
                skill_level=lplayer[4]
                new_skill_level=skill_level-random_number_loss
                if new_skill_level <20:
                    new_skill_level=20
                lplayer[4]=new_skill_level
                notneeded,vtt=func_other_teamreport.vtt(lplayer)
                updatedplayer=func_other_teamreport.player_potential(lplayer)
                new_pa=updatedplayer[14]
                new_vtt=vtt
                if (org_vtt != new_vtt) or (org_pa !=new_pa):
                    print_change(lplayer,new_vtt,org_vtt,org_pa,new_pa)


            
            
            elif  individual_player_position=="Def":
                skill_level=lplayer[5]
                new_skill_level=skill_level-random_number_loss
                if new_skill_level <20:
                    new_skill_level=20
                lplayer[5]=new_skill_level
                notneeded,vtt=func_other_teamreport.vtt(lplayer)
                updatedplayer=func_other_teamreport.player_potential(lplayer)
                new_pa=updatedplayer[14]
                new_vtt=vtt
                if (org_vtt != new_vtt) or (org_pa !=new_pa):
                    print_change(lplayer,new_vtt,org_vtt,org_pa,new_pa)



            elif  individual_player_position=="Mid":
                skill_level=lplayer[5]
                #lplayer[5]=new_skill_level
                new_skill_level=skill_level-random_number_loss
                if new_skill_level <20:
                    new_skill_level=20
                lplayer[5]=new_skill_level

                skill_level=lplayer[6]
                new_skill_level=skill_level-random_number_loss
                if new_skill_level <20:
                    new_skill_level=20
                lplayer[6]=new_skill_level

                notneeded,vtt=func_other_teamreport.vtt(lplayer)
                new_vtt=vtt
                new_vtt=yer=func_other_teamreport.player_potential(lplayer)
                updatedplayer=func_other_teamreport.player_potential(lplayer)
                new_pa=updatedplayer[14]
                #new_pa=updatedplayer[14]
                new_vtt=vtt
                if (org_vtt != new_vtt) or (org_pa !=new_pa):
                    print_change(lplayer,new_vtt,org_vtt,org_pa,new_pa)


            elif  individual_player_position=="Ata":
                skill_level=lplayer[6]
                new_skill_level=skill_level-random_number_loss
                if new_skill_level <20:
                    new_skill_level=20
                lplayer[6]=new_skill_level
                notneeded,vtt=func_other_teamreport.vtt(lplayer)
                updatedplayer=func_other_teamreport.player_potential(lplayer)
                new_pa=updatedplayer[14]
                new_vtt=vtt
                if (org_vtt != new_vtt) or (org_pa !=new_pa):
                    print_change(lplayer,new_vtt,org_vtt,org_pa,new_pa)


            else:
                input("Err pass")
                breakpoint()


    
    remove_year_of_contract()
    add_year_to_age()
    #print_output()
    actually_print_changes()

    #print and get user input
    #there is nothing the end user can really do with this page, its a print out of what happened

    while True:

        #os.system('clear')
        #func_other_header.header(status="est", season=season, game=game,defscore=defscore, atascore=atascore)

        #input("Press a button to Continue")

        userinput= input("Press enter to continue or m for menu\n")

        if userinput=="m":
            func_other_menu.menu(oursquad=squad, formation=1442, printoutput="y")
        else:
            return(local_squad,local_devsquad)



if __name__=="__main__":
    print ("***Script Called Directley****")
    season=game=1
    defscore=62
    atascore=60
    #squad=[['Gk', 'Myles', 'Sankoh', 33, 66, 5, 5, 12, 13, 9, 15, 9, 7, 67, 60, 1, 4], ['Gk', 'Omar', 'Parry', 21, 60, 8, 8, 13, 7, 17, 10, 8, 3, 61, 52, 3, 3], ['Gk', 'Cameron', 'Garrett', 31, 66, 5, 10, 20, 12, 5, 19, 11, 8, 67, 60, 2, 4], ['Def', 'Josh', 'Bird', 32, 2, 69, 19, 10, 6, 13, 15, 14, 5, 68, 54, 1, 4], ['Def', 'Seren', 'Brooks', 27, 2, 54, 15, 8, 8, 7, 17, 18, 5, 58, 55, 2, 2], ['Def', 'Tom', 'Stansfield', 24, 10, 70, 20, 19, 18, 6, 18, 7, 5, 78, 70, 2, 6], ['Def', 'Ahmed', 'Duncan', 26, 10, 51, 23, 8, 12, 20, 10, 14, 5, 58, 68, 3, 2], ['Def', 'Jim', 'Reiter', 25, 2, 58, 32, 11, 16, 7, 15, 17, 5, 65, 68, 1, 4], ['Def', 'Dylan', 'Denney', 23, 9, 58, 19, 17, 10, 13, 16, 11, 6, 69, 62, 1, 4], ['Def', 'Tomas', 'Potter', 20, 7, 59, 28, 10, 11, 7, 6, 11, 3, 59, 44, 3, 2], ['Def', 'Duncan', 'Bailey', 23, 8, 67, 11, 7, 9, 8, 5, 11, 6, 60, 40, 2, 3], ['Mid', 'Dylan', 'Payne', 33, 9, 38, 53, 18, 15, 20, 8, 16, 7, 65, 73, 1, 4], ['Mid', 'Liam', 'Gay', 31, 5, 65, 46, 7, 5, 11, 7, 12, 5, 54, 38, 3, 1], ['Mid', 'Travis', 'Bates', 33, 6, 45, 68, 15, 10, 15, 11, 15, 7, 67, 60, 1, 4], ['Mid', 'Carlos', 'Stanton', 23, 1, 56, 51, 6, 18, 14, 18, 15, 6, 59, 84, 2, 2], ['Mid', 'Harper', 'Neish', 33, 10, 54, 40, 12, 5, 16, 14, 16, 5, 58, 56, 1, 2], ['Mid', 'Travis', 'Shelton', 30, 5, 46, 38, 5, 8, 12, 19, 6, 5, 46, 58, 2, 1], ['Mid', 'Nick', 'Currie', 24, 5, 35, 49, 18, 14, 16, 15, 6, 6, 61, 70, 3, 3], ['Mid', 'Derron', 'Ward', 29, 4, 47, 50, 19, 16, 8, 8, 5, 7, 62, 54, 1, 3], ['Ata', 'Melin', 'Ealy', 18, 5, 2, 62, 5, 10, 18, 12, 15, 1, 61, 65, 2, 3], ['Ata', 'Payton', 'Dawson', 22, 4, 1, 59, 19, 9, 11, 11, 15, 3, 71, 53, 2, 5], ['Ata', 'Jose', 'Njoku', 23, 3, 8, 70, 9, 16, 13, 14, 20, 5, 72, 76, 3, 5], ['Ata', 'Samuel', 'James', 29, 7, 5, 57, 6, 18, 13, 9, 7, 5, 57, 67, 3, 2], ['Ata', 'Joe', 'Oddie', 30, 8, 6, 68, 14, 18, 18, 15, 10, 8, 75, 82, 1, 6]]
    devsquad=[['Gk', 'Miguel', 'Brooks', 19, 52, 1, 10, 12, 16, 16, 19, 14, 1, 61, 76, 1, 1], ['Gk', 'Caleb', 'Simmons', 22, 55, 7, 3, 10, 16, 5, 18, 14, 4, 60, 58, 1, 1], ['Def', 'Matt', 'Garrett', 18, 5, 67, 33, 10, 15, 15, 5, 12, 2, 67, 64, 1, 1], ['Def', 'Dana', 'Berry', 22, 8, 63, 16, 17, 8, 8, 6, 9, 6, 68, 48, 1, 1], ['Mid', 'Jim', 'Patel', 19, 4, 53, 68, 15, 8, 13, 15, 5, 3, 67, 56, 1, 1], ['Mid', 'Duncan', 'Marsh', 22, 8, 54, 40, 9, 17, 13, 13, 20, 5, 58, 70, 1, 1], ['Ata', 'Russel', 'Newbury', 22, 10, 8, 58, 17, 16, 15, 11, 10, 4, 70, 74, 1, 1], ['Ata', 'Duncan', 'Park', 21, 10, 5, 62, 17, 6, 9, 12, 18, 1, 70, 54, 1, 1]]
    #training(season, game, defscore, atascore, squad,devsquad)

    input("Part Deux")

    squad2=[['Gk', 'Mylesbbbbbbbb', 'Sankoh', 18, 66, 5, 5, 12, 13, 9, 15, 9, 7, 67, 60, 1, 4], ['Gk', 'Omar', 'Parry', 18, 66, 5, 5, 12, 13, 9, 15, 9, 7, 67, 60, 1, 4], ['Gk', 'Cameron', 'Garrett', 31, 66, 5, 10, 20, 12, 5, 19, 11, 8, 67, 60, 2, 4], ['Def', 'Josh', 'Bird', 18, 2, 69, 19, 10, 6, 13, 15, 14, 5, 68, 54, 1, 4], ['Def', 'Seren', 'Brooks', 18, 2, 69, 19, 10, 6, 13, 15, 14, 5, 68, 54, 2, 2], ['Def', 'Tom', 'Stansfield', 24, 10, 70, 20, 19, 18, 6, 18, 7, 5, 78, 70, 2, 6], ['Def', 'Ahmed', 'Duncan', 26, 10, 51, 23, 8, 12, 20, 10, 14, 5, 58, 68, 3, 2], ['Def', 'Jim', 'Reiter', 25, 2, 58, 32, 11, 16, 7, 15, 17, 5, 65, 68, 1, 4], ['Def', 'Dylan', 'Denney', 23, 9, 58, 19, 17, 10, 13, 16, 11, 6, 69, 62, 1, 4], ['Def', 'Tomas', 'Potter', 20, 7, 59, 28, 10, 11, 7, 6, 11, 3, 59, 44, 3, 2], ['Def', 'Duncan', 'Bailey', 23, 8, 67, 11, 7, 9, 8, 5, 11, 6, 60, 40, 2, 3], ['Mid', 'Dylan', 'Payne', 18, 9, 38, 53, 18, 15, 20, 8, 16, 7, 65, 73, 1, 4], ['Mid', 'Liam', 'Gay', 18, 9, 38, 53, 18, 15, 20, 8, 16, 7, 65, 73, 1, 4], ['Mid', 'Travis', 'Bates', 33, 6, 45, 68, 15, 10, 15, 11, 15, 7, 67, 60, 1, 4], ['Mid', 'Carlos', 'Stanton', 23, 1, 56, 51, 6, 18, 14, 18, 15, 6, 59, 84, 2, 2], ['Mid', 'Harper', 'Neish', 33, 10, 54, 40, 12, 5, 16, 14, 16, 5, 58, 56, 1, 2], ['Mid', 'Travis', 'Shelton', 30, 5, 46, 38, 5, 8, 12, 19, 6, 5, 46, 58, 2, 1], ['Mid', 'Nick', 'Currie', 24, 5, 35, 49, 18, 14, 16, 15, 6, 6, 61, 70, 3, 3], ['Mid', 'Derron', 'Ward', 29, 4, 47, 50, 19, 16, 8, 8, 5, 7, 62, 54, 1, 3], ['Ata', 'Melin', 'Ealy', 18, 5, 2, 62, 5, 10, 18, 12, 15, 1, 61, 65, 2, 3], ['Ata', 'Payton', 'Dawson', 18, 4, 1, 59, 19, 9, 11, 11, 15, 3, 71, 53, 2, 5], ['Ata', 'Jose', 'Njoku', 18, 4, 1, 59, 19, 9, 11, 11, 15, 3, 71, 53, 2, 5], ['Ata', 'Samuel', 'James', 29, 7, 5, 57, 6, 18, 13, 9, 7, 5, 57, 67, 3, 2], ['Ata', 'Joe', 'Oddie', 30, 8, 6, 68, 14, 18, 18, 15, 10, 8, 75, 82, 1, 6]]

    for i in squad2:
        print (i)
            
    training(season, game, defscore, atascore, squad2,devsquad)
