#!/usr/bin/python3

import os

def printplayers(input,vtt="n",draft="n",outputlimit=1000,justpostion="",playerswap="n",extra_field_at_front="n",sellplayer="n"):
    '''
    expecting a list full of players
    designed using format to avoid my previous pad functions and to deal with unexpedtley long names
    messing up format
    also stops having to code this multiple times in a script
    draft=n means is this the draft class? in which case do/don't print contract/wage/value to team, can be blank for things like playerswap, if yd = yes draft number ,ydc=draft number with contract
    outputlimit allows an option to only print out x lines (used in draft to show top 10 prospects)     
    playerswap - default n if y print normal stuff and 1 extra column of offer
    extra_field_at_front - default n if y shuffle everything over and print the extra first field mainly used for chosing players

    if extra_field_at_front=y
        edit fields
        print output
    if playerswap=y
        print output
    if draft=y
        if playercount hit break
        print header
            if position = ""
                print
            else print just that position
    if draft = n
        print
        
    '''


    count_letters_first_name=0
    count_letters_second_name=0


    for i in input:
        # get length of the longest names
        if extra_field_at_front=="y":
            try:
                firstname=len(i[2])
                secondname=len(i[3])
            except:
                print ("I have errored so dropping into debug mode,check extra_field_at_front=='y' is expected, if not try altering to n and rerunning ")
                breakpoint()
        else:
            try:
                firstname=len(i[1])
                secondname=len(i[2])
            except:
                print ("I have errored")
                breakpoint()
        if firstname > count_letters_first_name:
            count_letters_first_name=firstname
        if secondname > count_letters_second_name:
            count_letters_second_name=secondname

    #print (count_letters_first_name,count_letters_second_name)
    #print ()
    #add 1
    count_letters_first_name+=1
    count_letters_second_name+=1
    count_fullname_max_size=count_letters_first_name+count_letters_second_name
    default_spacing=3
    playercount=0

    for index,i in enumerate(input):
        position=i[0]
        fname=i[1]
        sname=i[2]
        age=i[3]
        gskill=i[4]
        dskill=i[5]
        askill=i[6]
        fitness=i[7]
        ability=i[8]
        chara=i[9]
        determination=i[10]
        luck=i[11]
        experience=i[12]
        Valuetoteam=i[13]
        Potentialablity=i[14]
        Contract=i[15]
        wage=i[16]
        special_skill=i[17]

        if extra_field_at_front=="y":
            field0=i[0]
            position=i[1]
            fname=i[2]
            sname=i[3]
            age=i[4]
            gskill=i[5]
            dskill=i[6]
            askill=i[7]
            fitness=i[8]
            ability=i[9]
            chara=i[10]
            determination=i[11]
            luck=i[12]
            experience=i[13]
            Valuetoteam=i[14]
            Potentialablity=i[15]
            Contract=i[16]
            wage=i[17]
            if sellplayer=="y":
                #18032019 incremented by 1 after adding special skills
                offer_p=i[19]
                oround=i[20]


            if sellplayer=="n":

                if (playercount==0):
                    print ('{:<3}{:<4}{:<{}}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}'.format("N","P","Name",count_fullname_max_size,"A","GS","DS","AS","F","Ab","C","D","L","E","VTT","PA","Co","Wa","Sc"))
                    print('{:<3}{:<5}{:<{}}{:<{}}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}'.format(field0,position,fname,count_letters_first_name,sname,count_letters_second_name,age,gskill,dskill,askill,fitness,ability,chara,determination,luck,experience,Valuetoteam,Potentialablity,Contract,wage,i[18]))
                    playercount+=1
                else:
                    print('{:<3}{:<5}{:<{}}{:<{}}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}'.format(field0,position,fname,count_letters_first_name,sname,count_letters_second_name,age,gskill,dskill,askill,fitness,ability,chara,determination,luck,experience,Valuetoteam,Potentialablity,Contract,wage,i[18]))
                    playercount+=1

            if sellplayer=="y":
                if (playercount==0):
                    print ('{:<3}{:<5}{:<{}}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<5}{:<7}'.format("N","P","Name",count_fullname_max_size,"A","GS","DS","AS","F","Ab","C","D","L","E","VTT","PA","Co","Wa","Sc","Pick","Offer"))
                    print('{:<3}{:<5}{:<{}}{:<{}}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<5}{:<4}'.format(field0,position,fname,count_letters_first_name,sname,count_letters_second_name,age,gskill,dskill,askill,fitness,ability,chara,determination,luck,experience,Valuetoteam,Potentialablity,Contract,wage,i[18],offer_p,oround))
                    playercount+=1
                else:
                    print('{:<3}{:<5}{:<{}}{:<{}}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<5}{:<4}'.format(field0,position,fname,count_letters_first_name,sname,count_letters_second_name,age,gskill,dskill,askill,fitness,ability,chara,determination,luck,experience,Valuetoteam,Potentialablity,Contract,wage,i[18],offer_p,oround))
                    playercount+=1




        if playerswap=="y" and sellplayer=="n":

            if (playercount==0):
                print ('{:<4}{:<{}}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<5}{:<4}'.format("P","Name",count_fullname_max_size,"A","GS","DS","AS","F","Ab","C","D","L","E","VTT","PA","Co","Wa","Sc","Pick","Offer"))
                
                try:
                    print('{:<4}{:<{}}{:<{}}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<5}{:<4}'.format(position,fname,count_letters_first_name,sname,count_letters_second_name,age,gskill,dskill,askill,fitness,ability,chara,determination,luck,experience,Valuetoteam,Potentialablity,Contract,wage,i[17],i[18],i[19]))
                except Exception as e:
                    print (e)
                    print ("Woops i errored please help me oh great one")
                    breakpoint()

                playercount+=1
            else:
                try:
                    print('{:<4}{:<{}}{:<{}}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<5}{:<4}'.format(position,fname,count_letters_first_name,sname,count_letters_second_name,age,gskill,dskill,askill,fitness,ability,chara,determination,luck,experience,Valuetoteam,Potentialablity,Contract,wage,i[17],i[18],i[19]))
                    playercount+=1
                except:
                    print("\nOops i have errored , lets see why \n probable bad incoming data, run 'for i in input: print (i)' for a better idea")
                    breakpoint()
            #break
        if draft=="ydc":

            if (playercount==outputlimit):
                break
            if (playercount==0):
                print ('{:<4}{:<4}{:<{}}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}'.format("N","P","Name",count_fullname_max_size,"A","GS","DS","AS","F","Ab","C","D","L","E","VTT","PA","Co","Wa","Sc"))
                if justpostion=="":
                    print('{:<4}{:<4}{:<{}}{:<{}}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}'.format(playercount,position,fname,count_letters_first_name,sname,count_letters_second_name,age,gskill,dskill,askill,fitness,ability,chara,determination,luck,experience,Valuetoteam,Potentialablity,Contract,wage,special_skill))
                else:
                    if position==justpostion:
                        print('{:<4}{:<4}{:<{}}{:<{}}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}'.format(playercount,position,fname,count_letters_first_name,sname,count_letters_second_name,age,gskill,dskill,askill,fitness,ability,chara,determination,luck,experience,Valuetoteam,Potentialablity,Contract,wage,special_skill))
                playercount+=1

            else:
                if justpostion=="":
                #if no position specified carry on as normal (i.e don't filter results)
                    print('{:<4}{:<4}{:<{}}{:<{}}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}'.format(playercount,position,fname,count_letters_first_name,sname,count_letters_second_name,age,gskill,dskill,askill,fitness,ability,chara,determination,luck,experience,Valuetoteam,Potentialablity,Contract,wage,special_skill))
                    playercount+=1
                else:
                # we only want a subset printed i.e 1 position
                    if position==justpostion:
                        try:
                            print('{:<4}{:<4}{:<{}}{:<{}}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}'.format(playercount,position,fname,count_letters_first_name,sname,count_letters_second_name,age,gskill,dskill,askill,fitness,ability,chara,determination,luck,experience,Valuetoteam,Potentialablity,Contract,wage,special_skill))
                        except:
                            print ("oops")
                            breakpoint()
                         
                        playercount+=1

        if draft=="yd":
            #breakpoint()
            if (playercount==outputlimit):
                break
            if (playercount==0):
                try:
                    #breakpoint()
                    print ('{:<4}{:<4}{:<{}}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}'.format("N","P","Name",count_fullname_max_size,"A","GS","DS","AS","F","Ab","C","D","L","E","VTT","PA","Co","Wa","Sc"))    
                except Exception as e:
                    print (e)
                    breakpoint()
                if justpostion=="":
                    print('{:<4}{:<4}{:<{}}{:<{}}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}'.format(playercount,position,fname,count_letters_first_name,sname,count_letters_second_name,age,gskill,dskill,askill,fitness,ability,chara,determination,luck,experience,Valuetoteam,Potentialablity,Contract,wage,special_skill))
                else:
                    if position==justpostion:
                        try:
                            print('{:<4}{:<4}{:<{}}{:<{}}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}'.format(playercount,position,fname,count_letters_first_name,sname,count_letters_second_name,age,gskill,dskill,askill,fitness,ability,chara,determination,luck,experience,Valuetoteam,Potentialablity,Contract,wage,special_skill))
                        except:
                            print ("Err error error error... lets drop into debug mode")
                            breakpoint()
                playercount+=1

            else:
                if justpostion=="":
                #if no position specified carry on as normal (i.e don't filter results)
                    print('{:<4}{:<4}{:<{}}{:<{}}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}'.format(playercount,position,fname,count_letters_first_name,sname,count_letters_second_name,age,gskill,dskill,askill,fitness,ability,chara,determination,luck,experience,Valuetoteam,Potentialablity,Contract,wage,special_skill))
                    playercount+=1
                else:
                # we only want a subset printed i.e 1 position
                    if position==justpostion:
                        print('{:<4}{:<4}{:<{}}{:<{}}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}'.format(playercount,position,fname,count_letters_first_name,sname,count_letters_second_name,age,gskill,dskill,askill,fitness,ability,chara,determination,luck,experience,Valuetoteam,Potentialablity,Contract,wage,special_skill))
                        playercount+=1

        if draft=="y":
            if (playercount==outputlimit):
                break
            if (playercount==0):
                print ('{:<4}{:<{}}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}'.format("P","Name",count_fullname_max_size,"A","GS","DS","AS","F","Ab","C","D","L","E","VTT","PA"))    
                playercount+=1

                if justpostion=="":
                    print('{:<4}{:<{}}{:<{}}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}'.format(position,fname,count_letters_first_name,sname,count_letters_second_name,age,gskill,dskill,askill,fitness,ability,chara,determination,luck,experience,Valuetoteam,Potentialablity))

                else:
                    if position==justpostion:
                        print('{:<4}{:<{}}{:<{}}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}'.format(position,fname,count_letters_first_name,sname,count_letters_second_name,age,gskill,dskill,askill,fitness,ability,chara,determination,luck,experience,Valuetoteam,Potentialablity))
            else:
                if justpostion=="":
                #if no position specified carry on as normal (i.e don't filter results)
                    print('{:<4}{:<{}}{:<{}}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}'.format(position,fname,count_letters_first_name,sname,count_letters_second_name,age,gskill,dskill,askill,fitness,ability,chara,determination,luck,experience,Valuetoteam,Potentialablity))
                    playercount+=1
                else:
                    # we only want a subset printed i.e 1 position
                    if position==justpostion:
                        print('{:<4}{:<{}}{:<{}}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}'.format(position,fname,count_letters_first_name,sname,count_letters_second_name,age,gskill,dskill,askill,fitness,ability,chara,determination,luck,experience,Valuetoteam,Potentialablity))
                        playercount+=1

        if draft=="n":
            if (playercount==outputlimit):
                break
            if (playercount==0):
                print ('{:<4}{:<{}}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}'.format("P","Name",count_fullname_max_size,"A","GS","DS","AS","F","Ab","C","D","L","E","VTT","PA","Co","Wa","Sc"))    
                print('{:<4}{:<{}}{:<{}}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}'.format(position,fname,count_letters_first_name,sname,count_letters_second_name,age,gskill,dskill,askill,fitness,ability,chara,determination,luck,experience,Valuetoteam,Potentialablity,Contract,wage,special_skill))
                playercount+=1
            else:
                print('{:<4}{:<{}}{:<{}}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}{:<4}'.format(position,fname,count_letters_first_name,sname,count_letters_second_name,age,gskill,dskill,askill,fitness,ability,chara,determination,luck,experience,Valuetoteam,Potentialablity,Contract,wage,special_skill))
                playercount+=1


if __name__=="__main__":

    a=os.system('cls||clear')
    print ("basic_output")
    input=[['Gk', 'Ada', 'Dunn', 26, 96, 3, 6, 17, 13, 12, 20, 7, 6, 83, 70, 0, 7], ['Gk', 'Austin', 'Amor', 35, 90, 8, 7, 20, 13, 19, 18, 19, 8, 89, 82, 1, 8], ['Gk', 'Elias', 'Mccoy', 34, 80, 9, 4, 18, 17, 17, 10, 7, 5, 73, 71, 1, 5], ['Def', 'Charlie', 'Hart', 32, 1, 80, 18, 18, 12, 18, 11, 18, 8, 80, 69, 2, 7], ['Def', 'Britton', 'Easen', 32, 9, 86, 36, 20, 8, 8, 11, 10, 8, 79, 45, 0, 6], ['Def', 'Ben', 'Bello', 35, 6, 86, 24, 20, 15, 7, 20, 18, 8, 85, 73, 1, 8], ['Def', 'Myles', 'Dixon', 18, 8, 97, 31, 8, 12, 12, 20, 13, 2, 78, 70, 0, 6], ['Def', 'Jonas', 'Bates', 20, 7, 83, 27, 18, 11, 10, 16, 17, 3, 75, 63, 0, 6], ['Def', 'Jamar', 'Love', 22, 1, 82, 49, 12, 6, 18, 19, 10, 5, 73, 63, 1, 5], ['Def', 'Thiago', 'Mayfield', 18, 1, 95, 24, 8, 11, 16, 18, 18, 2, 79, 74, 2, 6], ['Def', 'Davit', 'Dixon', 26, 2, 84, 26, 17, 14, 15, 19, 19, 7, 83, 80, 1, 7], ['Mid', 'Brogan', 'Fabino', 26, 9, 83, 79, 13, 15, 11, 8, 11, 6, 72, 59, 1, 5], ['Mid', 'Marvin', 'Ozel', 35, 1, 71, 98, 15, 14, 11, 15, 14, 8, 80, 68, 2, 7], ['Mid', 'Duncan', 'Stewart', 34, 7, 81, 56, 20, 20, 9, 14, 11, 6, 71, 74, 0, 5], ['Mid', 'Hamada', 'Bello', 18, 3, 57, 87, 9, 7, 5, 7, 15, 2, 58, 36, 1, 2], ['Mid', 'Joe', 'Shelton', 30, 2, 73, 53, 19, 18, 5, 20, 16, 8, 70, 75, 0, 5], ['Mid', 'Davo', 'Corben', 29, 1, 95, 90, 15, 5, 10, 10, 12, 5, 77, 41, 1, 6], ['Mid', 'Myles', 'Duke', 34, 6, 94, 58, 17, 19, 15, 20, 6, 8, 77, 85, 1, 6], ['Mid', 'Harper', 'Webb', 20, 4, 55, 92, 18, 5, 11, 20, 19, 2, 69, 58, 0, 4], ['Ata', 'Bobby', 'Lawson', 22, 8, 7, 96, 11, 9, 9, 14, 14, 6, 81, 54, 2, 7], ['Ata', 'Davo', 'Nicol', 18, 5, 5, 97, 17, 19, 8, 19, 7, 1, 81, 75, 0, 7], ['Ata', 'Elijah', 'Forrest', 23, 10, 3, 90, 9, 18, 20, 17, 11, 3, 78, 88, 0, 6], ['Ata', 'Seb', 'Major', 22, 5, 8, 92, 16, 13, 11, 16, 17, 4, 81, 68, 1, 7], ['Ata', 'Louis', 'Nash', 19, 3, 9, 84, 12, 14, 15, 7, 14, 4, 73, 62, 2, 5]]
    printplayers(input,vtt="n",draft="n",outputlimit=1000,justpostion="",playerswap="n",extra_field_at_front="n")

    print ("Out of contract")
    
    outofcontract=[['Def', 'Myles', 'Swenney', 22, 4, 97, 46, 20, 15, 8, 15, 14, 4, 85, 66, 0, 8], ['Def', 'Jeremy', 'Dreyer', 18, 7, 88, 14, 18, 18, 13, 15, 6, 2, 77, 74, 0, 6], ['Def', 'Russel', 'Ould', 31, 10, 89, 48, 10, 12, 9, 8, 12, 8, 77, 51, 0, 6], ['Def', 'Jan', 'Webb', 24, 5, 80, 22, 7, 12, 13, 13, 17, 4, 69, 65, 0, 4], ['Mid', 'Josh', 'Clark', 33, 4, 54, 93, 11, 15, 8, 13, 7, 8, 68, 60, 0, 4], ['Mid', 'Luke ', 'Diamond', 23, 2, 67, 52, 8, 12, 10, 16, 7, 6, 57, 60, 0, 2], ['Mid', 'Dillan', 'Owen', 18, 1, 89, 57, 14, 7, 19, 15, 15, 2, 67, 64, 0, 4], ['Mid', 'Tomas', 'Watson', 32, 3, 52, 62, 12, 7, 17, 9, 12, 5, 56, 52, 0, 2]]
    printplayers(outofcontract,draft="n",outputlimit=100,justpostion="")


    print ("Sell build")
    sellbuild=[[0, 'Def', 'Bobby', 'Riley', 34, 4, 92, 29, 18, 15, 7, 19, 11, 8, 85, 68, 2, 8, '66', 'Third round pick'], [1, 'Ata', 'Jim', 'Harper', 29, 9, 1, 96, 13, 19, 11, 19, 14, 6, 86, 82, 1, 8, '53', 'Second round pick'], [2, 'Ata', 'Melin', 'Cajuste', 33, 6, 4, 90, 18, 6, 8, 18, 14, 8, 82, 52, 2, 7, '89', 'Third round pick']]
    printplayers(sellbuild,draft="",outputlimit=25,justpostion="",playerswap="y",extra_field_at_front="y",sellplayer="y")
    
    
    print ("inital player offer")
    playerstosell_l=[['Gk', 'Jeremy', 'Khan', 34, 98, 10, 10, 13, 8, 12, 20, 11, 7, 85, 62, 2, 8, '66', 'Third round pick'], ['Def', 'Johnny', 'Baver', 25, 1, 97, 24, 15, 17, 17, 13, 13, 3, 84, 78, 1, 7, '70', 'Third round pick']]
    printplayers(playerstosell_l,draft="",outputlimit=25,justpostion="",playerswap="y")
    print ()
    printplayers(playerstosell_l,draft="",outputlimit=25,justpostion="",playerswap="y",sellplayer="n")


    print ("test output-broken?")


    createdraft=[['Def', 'Jim', 'Khan', 19, 83, 2, 9, 16, 17, 20, 20, 13, 1, 78, 90, 3, 0], ['Mid', 'Seren', 'Graham', 21, 8, 57, 52, 8, 16, 18, 17, 18, 1, 55, 85, 1, 0], ['Ata', 'Keith', 'Jones', 20, 9, 8, 70, 16, 20, 14, 15, 15, 1, 67, 84, 1, 0], ['Mid', 'Alfa  ', 'Neale', 21, 8, 65, 63, 8, 20, 20, 11, 10, 1, 59, 84, 3, 0], ['Mid', 'Donald', 'Edge', 21, 9, 57, 64, 9, 16, 18, 20, 10, 1, 58, 84, 3, 0], ['Ata', 'Gareth', 'Ould', 19, 3, 2, 78, 6, 18, 18, 17, 6, 1, 66, 83, 3, 0], ['Gk', 'Jude', 'Cajuste', 21, 89, 4, 7, 10, 16, 18, 14, 19, 1, 81, 82, 1, 0], ['Def', 'Derron', 'Ahmed', 20, 8, 72, 44, 11, 14, 20, 17, 16, 1, 66, 82, 3, 0], ['Ata', 'Tomas', 'Gay', 22, 9, 59, 63, 19, 17, 17, 19, 5, 1, 62, 82, 1, 0]]
    printplayers(createdraft,draft="y",outputlimit=5,justpostion="Ata")
    for i in createdraft:
            if "Ata" in i:
                print (i)

    print("\n\n\n\n")
    flawedcreatedraft= [['Gk', 'Mychal', 'Hawkins', 22, 80, 1, 2, 10, 18, 5, 17, 11, 1, 68, 69, 1, 0], ['Gk', 'Mychal1', 'Hawkins1', 22, 80, 1, 2, 10, 18, 5, 17, 11, 1, 68, 69, 1, 0]]
    printplayers(flawedcreatedraft,draft="y",outputlimit=5)

    printplayers(flawedcreatedraft,vtt="n",draft="n",outputlimit=5,justpostion="",playerswap="n",extra_field_at_front="n")
