#!/usr/bin/python3
# this is used in working out who won a match
import random
import os
import func_other_game_settings

# sync up the spacing of chars


#####

# Def ourteamscores these are to give the user an idea on how good their team is
# Def sortourteam used by gameday to get our team scores , formation=442 at moment but trying to future proof,printoutput =print to screen
# Def report, main item called


def ourteamscores(ourfirstx1, printoutput, totalchar, totaldet, totalexp):


    '''

    ourteamscores these are to give the user an idea on how good their team is
    it is called by the report function
    ourteamscores(ourfirstx1, printoutput, totalchar, totaldet, totalexp)
    return(masterdefscore, masteratascore)

    maths involved(we already know our first 11):
    for each player in the relevant position the following are added together

    average fitness/age/char/determination/luck/experience are added up and divied by 11 to get a team average

    average gkskill/deds/defa/midd/mida/atad/ataa  are worked out (total score / players in that position)

    team scores are then based on:

                   D       A       Total
           GK      6.5     0       6.5
           D       4.5     2.5     7
           M       3       4       7
           A       1       8.5     9.5
           Fit     1       1       2
           Char    1       1       2
           Det     1       1       2
           Luck    1       1       2
           Exp     1       1       2

           Total   20      20
           Total * 5 = total score
     so if gk score is 90 (out of 100)
     (6.5/100)*90 =  a contribution to the defensive score of 5.85 (out of a maximum 6.5 for the position)
     Out of a maximum 20 defensive score we have 5.85 from our GK
     All the other (D/M/A....) are added together to get the masterdefscore
     the total is then *5 to make it out of 100 (just to make it nicer on the eyes)
    
    

    #gkd=
    #gks

    # defensive skills
    gkd = 0
    defd = 0
    midd = 0
    atad = 0

    #attacking skills
    gka = 0
    defa = 0
    mida = 0
    ataa = 0

    gkinteam = 0
    definteam = 0
    midinteam = 0
    atainteam = 0

    fitscores = 0
    expscores = 0
    agescores = 0
    chascores = 0
    detscores = 0
    lucscores = 0

    for player in ourfirstx1:
        # set variables
        position = player[0]
        ageskill = player[3]
        gkskill = player[4]
        defskill = player[5]
        ataskill = player[6]
        fitskill = player[7]
        abiskill = player[8]
        chaskill = player[9]
        detskill = player[10]
        lucskill = player[11]
        expskill = player[12]

        # globalvalues
        fitscores = fitscores+int(fitskill)
        expscores = expscores+int(expskill)
        agescores = agescores+ageskill
        chascores = chascores+int(chaskill)
        detscores = detscores+int(detskill)
        lucscores = lucscores+int(lucskill)

        if position == "Gk":
            gkd = gkd+int(gkskill)
            gka = gka+int(ataskill)
            gkinteam = gkinteam+1
        if position == "Def":
            defd = defd+int(defskill)
            defa = defa+int(ataskill)
            definteam = definteam+1
        if position == "Mid":
            midd = midd+int(defskill)
            mida = mida+int(ataskill)
            midinteam = midinteam+1
        if position == "Ata":
            atad = atad+int(defskill)
            ataa = ataa+int(ataskill)
            atainteam = atainteam+1

    # sort out averages and spacings for output values

    gkvaluetoteam=0.6
    defdvaluetoteam=0.5
    defavaluetoteam=0.25
    middvaluetoteam=0.333
    midaaluetoteam=0.40
    atadvaluetoteam=0
    ataavaluetoteam=0.9175
    valuetoteam=0.2

    fit_average = int(fitscores/11)
    age_average = int(agescores/11)
    cha_average = int(chascores/11)
    det_average = int(detscores/11)
    luc_average = int(lucscores/11)
    exp_average = int(expscores/11)

    defd = int(defd/int(definteam))
    defa = int(defa/int(definteam))
    midd = int(midd/int(midinteam))
    mida = int(mida/int(midinteam))
    atad = int(atad/int(atainteam))
    ataa = int(ataa/int(atainteam))

    gkdvaluettoteam=round((gkd*gkvaluetoteam))
    defdvaluettoteam=round((defd*defdvaluetoteam)/4)
    defavaluettoteam=round((defa*defavaluetoteam)/3)
    middvaluettoteam=round((midd*middvaluetoteam)/4)
    midavaluettoteam=round((mida*midaaluetoteam)/1.5)
    atadvaluettoteam=round((atad*atadvaluetoteam)/2)
    ataavaluettoteam=round((ataa*ataavaluetoteam)/2)
    #breakpoint()

    teamvaluetoteam=(fit_average + cha_average + det_average + luc_average + exp_average)*valuetoteam
    teamvaluetoteam=round(teamvaluetoteam)

    masterdefscore=totaldefensescore= gkdvaluettoteam+defdvaluettoteam+middvaluettoteam+atadvaluettoteam+teamvaluetoteam
    masteratascore=totalatackscore = defavaluettoteam+midavaluettoteam+ataavaluettoteam+teamvaluetoteam
    #masterdefscore=totaldefensescore= 13
    #masteratascore=totalatackscore = 12
    '''

    # defensive skills
    gkd = 0
    defd = 0
    midd = 0
    atad = 0

    #attacking skills
    gka = 0
    defa = 0
    mida = 0
    ataa = 0

    gkinteam = 0
    definteam = 0
    midinteam = 0
    atainteam = 0

    fitscores = 0
    expscores = 0
    agescores = 0
    chascores = 0
    detscores = 0
    lucscores = 0

    for player in ourfirstx1:
        # set variables
        position = player[0]
        ageskill = player[3]
        gkskill = player[4]
        defskill = player[5]
        ataskill = player[6]
        fitskill = player[7]
        abiskill = player[8]
        chaskill = player[9]
        detskill = player[10]
        lucskill = player[11]
        expskill = player[12]
        vttskill=player[13]

        # globalvalues
        fitscores = fitscores+int(fitskill)
        expscores = expscores+int(expskill)
        agescores = agescores+ageskill
        chascores = chascores+int(chaskill)
        detscores = detscores+int(detskill)
        lucscores = lucscores+int(lucskill)

        if position == "Gk":
            gkd = gkd+int(vttskill)
        if position == "Def":
            defd = defd+int(vttskill)
        if position == "Mid":
            midd = midd+int(vttskill)
        if position == "Ata":
            ataa = ataa+int(vttskill)

    fit_average = int(fitscores/11)
    age_average = int(agescores/11)
    cha_average = int(chascores/11)
    det_average = int(detscores/11)
    luc_average = int(lucscores/11)
    exp_average = int(expscores/11)

    masterdefscore=round((gkd+defd+(midd/4))/6)
    masteratascore=round(((midd/4)+ataa)/3)
    #print (masterdefscore,masteratascore)
    #input()

    

    if printoutput == "y":

        #print("\nContribution to team score\n")
        print ("{:<24}{:<5}{:<2}".format("\nAverage Fitness",fit_average,"Out of 100"))
        print ("{:<23}{:<5}".format("Average Age of team",age_average))
        print ("{:<23}{:<5}{:<2}".format("Average Char of team",cha_average,"Out of 20"))
        print ("{:<23}{:<5}{:<2}".format("Average Luck of team",luc_average,"Out of 20"))
        print ("{:<23}{:<5}{:<2}".format("Average Det of team",det_average,"Out of 20"))
        print ("{:<23}{:<5}".format("Average Exp of team",exp_average))

        print ("\nAverage of Skills by position group (used for end of season training)")

        print("\n                   | Gk | Def | Mid | Ata ")
        #print("====================================================")
        print("Exp  {:<14}| {:<3}| {:<4}| {:<4}| {:<3} ".format ("",gke,defe,mide,atae))
        print("Ability  {:<10}| {:<3}| {:<4}| {:<4}| {:<3} ".format ("",gkab,defab,midab,ataab))
        print("Char  {:<13}| {:<3}| {:<4}| {:<4}| {:<3} ".format ("",gkc,defc,midc,atac))
        print("Superb Role Models {:<0}| {:<3}| {:<4}| {:<4}| {:<3} ".format ("",gksp,defsp,midsp,atasp))
        print("Good Role Models{:<3}| {:<3}| {:<4}| {:<4}| {:<3} ".format ("",gkgp,defgp,midgp,atagp))

    return(masterdefscore, masteratascore)

def player_potential(playerin):

    #formula is:
    #char 25% + det 25% + luck 10% + ability 40%
    #breakpoint()
    player_position=playerin[0]
    player_first_name=playerin[1]
    player_second_name=playerin[2]
    player_gs=playerin[4]
    player_ds=playerin[5]
    player_as=playerin[6]
    player_fitness=playerin[7]
    player_ablity=playerin[8]
    player_char=playerin[9]
    player_determination=playerin[10]
    player_luck=playerin[11]
    player_exp=playerin[12]

    player_potential=round((player_char*1.25)+(player_determination*1.25)+(player_luck/2)+(player_ablity*2))
    
    playerin[14]= player_potential

    playerout=playerin

    return (playerout)


def vtt(playerin):

    i=playerin

    # only expecting 1 player so no loop

    player_position=i[0]
    player_first_name=i[1]
    player_second_name=i[2]
    player_gs=i[4]
    player_ds=i[5]
    player_as=i[6]
    player_fitness=i[7]
    player_ablity=i[8]
    player_char=i[9]
    player_determination=i[10]
    player_luck=i[11]
    player_exp=i[12]
    if player_exp >10:
        player_exp=10

    #gk_gk=61 # highest score with value of 60 was initally 99.4 and being rounded down to 99, this is a nasty hack to allow a 100 VTT to be hit
    #gk_ab=8
    #gk_ch=8
    #gk_det=6
    #gk_luck=8
    #gk_exp=10

    gk_gk=76 # highest score with value of 60 was initally 99.4 and being rounded down to 99, this is a nasty hack to allow a 100 VTT to be hit
    gk_fitness=10

    def_def=60
    def_fitness=20

    mid_def=30
    mid_ata=30
    mid_fitness=20

    ata_ata=60
    ata_fitness=20


    p_ab=5
    p_ch=5
    p_det=5
    p_luck=5
    p_exp=5

    '''
    def_def=60
    def_fitness=10
    def_ab=5
    def_ch=5
    def_det=5
    def_luck=5
    def_exp=10

    mid_def=30
    mid_ata=30
    mid_fitness=10
    mid_ab=5
    mid_ch=5
    mid_det=5
    mid_luck=5
    mid_exp=10

    ata_ata=60
    ata_fitness=10
    ata_ab=5
    ata_ch=5
    ata_det=5
    ata_luck=5
    ata_exp=10
    '''


    
           #this is where VTT / vtt (value to team) is added
           # bit messey i am adding GK 10,Def/Mid +15,ata-10 to their VTT scores to give them a score out of 100 (without it GK would never hit 100)
    if player_position == "Gk":
        #tempvtt=(player_gs/(100/gk_gk))+(player_ablity*(p_ab/20))+(player_char*(p_ch/20))+(player_determination*(p_det/20))+(player_luck*(p_luck/20))+(p_exp)
        tempvtt=((player_gs/100)*gk_gk)+(player_ablity*(p_ab/20))+(player_fitness/2)+(player_determination*(p_det/20))+(player_luck*(p_luck/20))+player_exp
        #breakpoint()
        tempvtt=round(tempvtt)
        if tempvtt > 100:
            tempvtt=100
        i[13]=int(tempvtt)
    if player_position == "Def":
        tempvtt=(player_ds/(100/def_def))+(player_fitness*(def_fitness/20))+(player_ablity*(p_ab/20))+(player_char*(p_ch/20))+(player_determination*(p_det/20))+(player_luck*(p_luck/20))+player_exp
        tempvtt=round(tempvtt)
        if tempvtt > 100:
            tempvtt=100
        i[13]=tempvtt
    if player_position == "Mid":
        tempvtt=(player_as/(100/mid_ata))+(player_ds/(100/mid_def))+(player_fitness*(mid_fitness/20))+(player_ablity*(p_ab/20))+(player_char*(p_ch/20))+(player_determination*(p_det/20))+(player_luck*(p_luck/20))+player_exp
        tempvtt=round(tempvtt)
        if tempvtt > 100:
            tempvtt=100
        i[13]=tempvtt
    if player_position == "Ata":
        tempvtt=(player_as/(100/ata_ata))+(player_fitness*(ata_fitness/20))+(player_ablity*(p_ab/20))+(player_char*(p_ch/20))+(player_determination*(p_det/20))+(player_luck*(p_luck/20))+player_exp
        tempvtt=round(tempvtt)
        if tempvtt > 100:
            tempvtt=100
        i[13]=tempvtt
    

    players_out=i

    return(players_out,tempvtt)

def special_player_check(player_exp,player_ablity,player_char,playerage,org_sc=""):
    
    playerage=int(playerage)

    #lets stop young players getting super powers, this also allows us to sign players to D or undrafted Contracts

    agfs=func_other_game_settings.age_for_super_powers
    ssfgt=func_other_game_settings.skill_set_for_Good_trainer
    sstst=func_other_game_settings.skill_set_for_Superb_trainer

    if (player_exp+player_ablity+player_char)> int(sstst) and playerage>int(agfs):
        return ("ST")
    elif (player_exp+player_ablity+player_char)> int(ssfgt) and playerage>int(agfs):
        return("GT")
    elif org_sc=="D":
        return ("D")
    elif org_sc=="U":
        return ("U")
    else:
        return("")

    
def sortourteam(oursquad, formation, printoutput):


    '''

    input = (oursquad, formation, printoutput)
    This is where we break down a squad into a match day 11
    players get split into a list based on their posistions i.e gklist/deflist/midlist/atalist
    all players char/det/exp get added together for some team stats
    players are sorted by skill using lambda although this logic needs to be changed
    each position list is then looped through to match the formation i.e in a 4-4-2 formation
    4 defenders will be chosen from the deflist
    if print output =y , your team will be printed
    return(ourch, ourdet, ourexp, firstx1)

    
    '''
    ourgs = 0
    ourds = 0
    ouras = 0
    ourfi = 0
    ourch = 0
    ourdet = 0
    ourexp = 0
    gklist = []
    deflist = []
    midlist = []
    atalist = []
    firstx1 = []
    totalchar = 0
    totaldetermination = 0
    totalexperience = 0

    #char
    global gkc,defc,midc,atac
    gkc=0
    defc=0
    midc=0
    atac=0

    #experience
    global gke,defe,mide,atae
    gke=0
    defe=0
    mide=0
    atae =0

    #ability
    global gkab,defab,midab,ataab
    gkab=0
    defab=0
    midab=0
    ataab=0

    #special player
    global gksp,defsp,midsp,atasp
    gksp=0
    defsp=0
    midsp=0
    atasp=0

    #very good players
    global gkgp,defgp,midgp,atagp
    gkgp=0
    defgp=0
    midgp=0
    atagp=0

    # sort out formation into a format for us
    formation = str(formation)
    formationgk = (formation[0:1])
    formationde = (formation[1:2])
    formationmi = (formation[2:3])
    formationat = (formation[3:4])

    # split list into position
    # ugly but effective it will keep adding to the xxxlist pot until it see another position then it will switch xxxlistpot
    tempcount=0

    for i in oursquad:
        player_position=i[0]
        player_first_name=i[1]
        player_second_name=i[2]
        player_gs=i[4]
        player_ds=i[5]
        player_as=i[6]
        player_fitness=i[7]
        player_ablity=i[8]
        player_char=i[9]
        player_determination=i[10]
        player_luck=i[11]
        player_exp=i[12]
        try:
            player_special_skills=i[17]
        except:
            player_special_skills=""
        

        #this is where VTT / vtt (value to team) is added
        for j in  i: 
            #breakpoint()
            position = j
            special_result=special_player_check(player_exp,player_ablity,player_char,playerage=i[3],org_sc=i[17])
            i[17]=special_result


            if position == "Gk":
                vtt(i)
                player_potential(i)
                gklist.append(i)
                gke=gke+player_exp
                gkab=gkab+player_ablity
                gkc=gkc+player_char
                if player_special_skills =="GT":
                    gkgp+=1
                if player_special_skills =="ST":
                    gksp+=1



            if position == "Def":
                vtt(i)
                player_potential(i)
                deflist.append(i)
                defe=defe+player_exp
                defab=defab+player_ablity
                defc=defc+player_char
                if player_special_skills =="GT":
                    defgp+=1
                if player_special_skills =="ST":
                    defsp+=1

            if position == "Mid":
                vtt(i)
                player_potential(i)
                midlist.append(i)
                mide=mide+player_exp
                midab=midab+player_ablity
                midc=midc+player_char
                if player_special_skills =="GT":
                    midgp+=1
                if player_special_skills =="ST":
                    midsp+=1

            if position == "Ata":
                vtt(i)
                player_potential(i)
                atalist.append(i)
                atae=atae+player_exp
                ataab=ataab+player_ablity
                atac=atac+player_char
                if player_special_skills =="GT":
                    atagp+=1
                if player_special_skills =="ST":
                    atasp+=1

 
    # add up char and determination
        indvidualchar = i[9]
        indvidualdet = i[10]
        invidualexp = i[12]

        totalchar = totalchar+int(indvidualchar)
        totaldetermination = totaldetermination+int(indvidualdet)
        totalexperience = totalexperience+int(invidualexp)

    # sort players by skill level
    
    gklist.sort(key=lambda gklist: gklist[13], reverse=True)
    deflist.sort(key=lambda deflist: deflist[13], reverse=True)
    midlist.sort(key=lambda midlist: midlist[13], reverse=True)
    atalist.sort(key=lambda atalist: atalist[13], reverse=True)
    print ()

    #experience
    gke=round(gke/3)
    defe=round(defe/8)
    mide=round(mide/8)
    atae=round(atae/5)

    #ablility
    gkab=round(gkab/3)
    defab=round(defab/8)
    midab=round(midab/8)
    ataab=round(ataab/5)

    #char
    gkc=round(gkc/3)
    defc=round(defc/8)
    midc=round(midc/8)
    atac=round(atac/5)

    # build list of first x1 based on sorting above

    positioncount = 0
    notfirstx1=[]

    for i in gklist:
        if int(positioncount) < int(formationgk):
            firstx1.append(i)
            positioncount = positioncount+1
        else:
            notfirstx1.append(i)

    positioncount = 0
    for i in deflist:
        if int(positioncount) < int(formationde):
            firstx1.append(i)
            positioncount = positioncount+1
        else:
            notfirstx1.append(i)

    positioncount = 0
    for i in midlist:
        if int(positioncount) < int(formationmi):
            firstx1.append(i)
            positioncount = positioncount+1
        else:
            notfirstx1.append(i)

    positioncount = 0
    for i in atalist:
        if int(positioncount) < int(formationat):
            firstx1.append(i)
            positioncount = positioncount+1
        else:
            notfirstx1.append(i)
            
    if printoutput == "y":
        print("Here is your first X1...(VTT=Value to team, summarizing all players skills to try and rank our players, the higher the better)\n")
        import func_other_format_input
        func_other_format_input.printplayers(firstx1,vtt="y")
        #print ("====================================================================")
        print ("\nAnd here is the rest of your squad who are not good enough to get into the firstXI\n")
        func_other_format_input.printplayers(notfirstx1,vtt="y")
        

    ourch = int(totalchar)
    ourdet = int(totaldetermination)
    ourexp = int(totalexperience)

    return(ourch, ourdet, ourexp, firstx1)


def report(oursquad, formation, printoutput):


    '''

    input oursquad, formation, printoutput
    formation is hardcoded to 4-4-2 no matter what the input at the moment
    are sorted and narrowed down to a first x1 and then...
    if printoutput = y a report is printed
                   = n masterdefscore, masteratascore are returned for things like matchday caculations
                   = ft for end of season training , pass back everything

    '''

    formation = 1442  # hardcoded for the moment as just working with 442 at the moment
    # printoutput="y"

    ourch, ourdet, ourexp, firstx1 = sortourteam(oursquad, formation, printoutput)

    if printoutput == "ft":
        masterdefscore, masteratascore = ourteamscores(firstx1, printoutput, totalchar=ourch, totaldet=ourdet, totalexp=ourexp)
        #return(masterdefscore, masteratascore,totalchar, totaldet, totalexp,gkgp,defgp,midgp,atagp,gksp,defsp,midsp,atasp,gke,defe,mide,atae,atae,defab,midab,ataab,gkc,defc,midc,atac)
        return(masterdefscore, masteratascore,gkgp,defgp,midgp,atagp,gksp,defsp,midsp,atasp,gke,defe,mide,atae,gkab,defab,midab,ataab,gkc,defc,midc,atac)
    if printoutput == "y":
        ourteamscores(firstx1, printoutput, totalchar=ourch, totaldet=ourdet, totalexp=ourexp)

    if printoutput == "n":  # silent output wanted for some kind of caculation
        try:
           masterdefscore, masteratascore = ourteamscores(firstx1, printoutput, totalchar=ourch, totaldet=ourdet, totalexp=ourexp)
        except Exception as e :
            print ("Error code",e)
            breakpoint()
        #masterdefscore=masteratascore=69
        return(masterdefscore, masteratascore)


if __name__ == "__main__":

    import os
    a=os.system('cls||clear')
    #print ("Unit testing - function ourteamscores...\n")
    #print ("Here is a first X1 to work with...\n")

    #firstx1=[['Gk ', 'Vincent ', 'Riley        ', 27, '95 ', '4  ', '5  ', '91 ', '16 ', '8  ', '14 ', '8  ', '1  '], ['Def', 'Brogan  ', 'Johnson      ', 28, '4  ', '80 ', '21 ', '64 ', '17 ', '5  ', '15 ', '16 ', '1  '], ['Def', 'David   ', 'Bailey       ', 30, '1  ', '88 ', '40 ', '93 ', '16 ', '5  ', '6  ', '10 ', '1  '], ['Def', 'Flyn    ', 'Payne        ', 19, '10 ', '94 ', '31 ', '74 ', '18 ', '16 ', '15 ', '17 ', '1  '], ['Def', 'Franky  ', 'Mccoy        ', 23, '8  ', '92 ', '34 ', '85 ', '9  ', '10 ', '11 ', '16 ', '1  '], ['Mid', 'Ari     ', 'Hubbard      ', 24, '1  ', '76 ', '52 ', '78 ', '15 ', '12 ', '5  ', '20 ', '1  '], ['Mid', 'Jim     ', 'Wagner       ', 29, '2  ', '91 ', '68 ', '75 ', '8  ', '7  ', '6  ', '18 ', '1  '], ['Mid', 'Logan   ', 'Vogel        ', 30, '1  ', '54 ', '96 ', '88 ', '14 ', '19 ', '5  ', '18 ', '1  '], ['Mid', 'Louis   ', 'Mccoy        ', 19, '7  ', '90 ', '87 ', '70 ', '8  ', '14 ', '10 ', '14 ', '1  '],['Ata', 'Martyn  ', 'Davis        ', 21, '4  ', '3  ', '91 ', '93 ', '17 ', '6  ', '5  ', '12 ', '1  '], ['Ata', 'Marko   ', 'Whitehouse   ', 25, '2  ', '9  ', '93 ', '96 ', '14 ', '9  ', '11 ', '16 ', '1  ']] 

    #import func_other_format_input
    #func_other_format_input.printplayers(firstx1)

    #ourteamscores (ourfirstx1=firstx1, printoutput="y", totalchar=1, totaldet=2, totalexp=3)

    print (input("Press a button"))
    a=os.system('cls||clear')
    print ("Unit testing - function report & sortteam (hard to seperate)...\n")

    import func_other_create_players


    #squad=[['Gk', 'Chris   ', 'Kindred      ', 30, '89 ', '1  ', '7  ', '72 ', '5  ', '10 ', '12 ', '15 ', '1  '], ['Gk', 'Marko   ', 'Park         ', 29, '91 ', '3  ', '5  ', '90 ', '7  ', '16 ', '11 ', '6  ', '1  '], ['Gk', 'Bobby   ', 'Ford         ', 24, '92 ', '8  ', '3  ', '81 ', '13 ', '6  ', '18 ', '5  ', '1  '], ['Def', 'Merlin  ', 'Payne        ', 22, '6  ', '79 ', '10 ', '71 ', '20 ', '7  ', '6  ', '6  ', '1  '], ['Def', 'Ada     ', 'Hubbard      ', 27, '5  ', '88 ', '34 ', '81 ', '8  ', '7  ', '12 ', '8  ', '1  '], ['Def', 'Mitchel ', 'Clark        ', 29, '5  ', '88 ', '26 ', '82 ', '17 ', '7  ', '14 ', '6  ', '1  '], ['Def', 'Austin  ', 'Rogers       ', 23, '4  ', '85 ', '40 ', '60 ', '13 ', '15 ', '14 ', '16 ', '1  '], ['Def', 'Steven  ', 'Robert       ', 29, '4  ', '81 ', '49 ', '94 ', '12 ', '11 ', '8  ', '18 ', '1  '], ['Def', 'Ben     ', 'Forrest      ', 24, '8  ', '91 ', '20 ', '74 ', '9  ', '11 ', '6  ', '20 ', '1  '], ['Def', 'Mateo   ', 'Bird         ', 18, '7  ', '80 ', '21 ', '91 ', '8  ', '17 ', '18 ', '12 ', '1  '], ['Def', 'Luke    ', 'Ortiz        ', 19, '5  ', '96 ', '32 ', '99 ', '15 ', '19 ', '6  ', '18 ', '1  '], ['Mid', 'Ari     ', 'Read         ', 35, '9  ', '84 ', '97 ', '69 ', '15 ', '20 ', '19 ', '7  ', '1  '], ['Mid', 'Louis   ', 'Grace        ', 31, '9  ', '65 ', '86 ', '91 ', '6  ', '13 ', '11 ', '9  ', '1  '], ['Mid', 'Jenson  ', 'Ellis        ', 34, '10 ', '94 ', '61 ', '60 ', '5  ', '19 ', '14 ', '19 ', '1  '], ['Mid', 'Tank    ', 'Jackson      ', 33, '1  ', '75 ', '81 ', '65 ', '14 ', '5  ', '14 ', '5  ', '1  '], ['Mid', 'Noel    ', 'Dawson       ', 34, '7  ', '52 ', '54 ', '62 ', '18 ', '12 ', '15 ', '9  ', '1  '], ['Mid', 'Samuel  ', 'Graham       ', 29, '3  ', '85 ', '56 ', '89 ', '9  ', '20 ', '15 ', '6  ', '1  '], ['Mid', 'Callam  ', 'Sharp        ', 29, '7  ', '83 ', '89 ', '94 ', '7  ', '11 ', '12 ', '11 ', '1  '], ['Mid', 'Omar    ', 'Carter       ', 24, '7  ', '54 ', '92 ', '85 ', '17 ', '12 ', '14 ', '6  ', '1  '], ['Ata', 'Goran   ', 'Duncan       ', 30, '8  ', '2  ', '80 ', '96 ', '12 ', '19 ', '20 ', '15 ', '1  '], ['Ata', 'Junior  ', 'Fells        ', 29, '8  ', '2  ', '99 ', '74 ', '18 ', '8  ', '9  ', '13 ', '1  '], ['Ata', 'Tom     ', 'Plato        ', 33, '5  ', '9  ', '80 ', '80 ', '6  ', '19 ', '15 ', '7  ', '1  '], ['Ata', 'Jens    ', 'Janis        ', 35, '7  ', '8  ', '86 ', '87 ', '5  ', '6  ', '8  ', '16 ', '1  '], ['Ata', 'Hans    ', 'Fox          ', 25, '1  ', '3  ', '80 ', '83 ', '7  ', '11 ', '20 ', '15 ', '1  ']]

    #live import
    import func_other_create_players
    squad=func_other_create_players.createplayers(gk=3, defender=8, mid=8, ata=4, qualityofplayer=99, maxageofplayer=35, minageofplayer=18, ef="abc",cheat="y")
    #breakpoint()
    
    #print ("Squad before changes")
    #func_other_format_input.printplayers(squad)

    #print ("Here is the squad...")
    #import func_other_format_input
    #func_other_format_input.printplayers(squad)
    report(oursquad=squad, formation=1442, printoutput="y")
    print ()

    masterdefscore, masteratascore=report(oursquad=squad, formation=1442, printoutput="n")
    print ("Print = n , return values for masteratascore %s masteratascore %s" % (masterdefscore,masteratascore))
   
    import func_other_create_players 
   

    input("press a button to continue")     
    squad=func_other_create_players.createplayers(gk=3, defender=8, mid=8, ata=4, qualityofplayer=99, maxageofplayer=35, minageofplayer=18, ef="abc")

    report(oursquad=squad, formation=1442, printoutput="y")
    #print ()
    #masterdefscore, masteratascore=report(oursquad=squad, formation=1442, printoutput="n")


    input("perfect player")
    print ("P   Name             A   GS  DS  AS  F   Ab  C   D   L   E   VTT PA  Co  Wa")
    print ("Gk  Bob Jones        21  99  99  99 99   20  20  20  20, 0   5,  6")
    vtttemp=["Gk","Bob","Jones",21,99,99,99,99,20,20,20,20,20,5,6]
    notneeded,vttg=vtt(vtttemp)
    print ("GK-",vttg)
    
    vttd=""
    vtttempd=["Def","Bob","Jones",21,99,99,99,99,20,20,20,20,20,5,6]
    notneededd,vttd=vtt(vtttempd)
    print ("Def-",vttd)

    vtttempm=["Mid","Bob","Jones",21,99,99,99,99,20,20,20,20,20,5,6]
    notneeded,vttm=vtt(vtttempm)
    print ("Mid-",vttm)

    vtttempa=["Ata","Bob","Jones",21,99,99,99,99,20,20,20,20,20,5,6]
    notneeded,vtta=vtt(vtttempa)
    print ("ATA-",vtta)


