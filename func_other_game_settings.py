#!/usr/bin/python3
'''

This is a central lookup for (nearley) all configuable parameters used thorought the game
in general its best not to mess with them, as no real testing has taken place on how changes will work

'''

#can change (not advised to go to low espically or stuff will break


maxbudget = 120 #recomemned 100
picksperyearmax=5 # to high and you can change to much of your team, to low i.e below 4 will probable produce weird issues
quality_of_draft=80
size_of_draft_gk=40 # there are 96 picks in the draft so a good spread is needed recommend each number no lower than 40
size_of_draft_def=60 # see above
size_of_draft_mid=60 # see above
size_of_draft_ata=40 # see above
size_of_undrafted_class=300 # this is max size of undrafted and free agent players any more than this number will be removed
inital_top_range_player=65 # of initally created team, highest should be 99, the lower it is during the first season you will have a lot of money to upgrade in free agency
#inital_top_range_player=99 # of initally created team, highest should be 99, the lower it is during the first season you will have a lot of money to upgrade in free agency
inital_top_range_player_freeagency=90
freeagency_gk=15
freeagency_def=20
freeagency_mid=20
freeagency_ata=15
startseason = 1 # needs to be less than season to play
auto_save_game="y" # else = no, game is saved at end of every season


# used in testing
cheat="n" # all players skills at 99, for cheat needs to be cheat="y"
#cheat="y" # all players skills at 99, for cheat needs to be cheat="y"

# not tested what happens if you do change

minage = 18
maxage = 35
firstrounddraftpicks = 1
secondrounddraftpicks = 1
thirdrounddraftpicks = 1
seasonstoplay = 10
maxskillofinitalteam = 5
minskillofinitalteam = 1

# will break things if changed

defaultformation = 1442
squad_size_gk = 3
squad_size_def = 8
squad_size_mid = 8
squad_size_ata = 5

