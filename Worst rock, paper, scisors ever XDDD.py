import random
#Kámen, nůžky, papír

ot = print('Ahoj chceš si se mnou zahrát kámen nůžky papír ? Y/N ')
odot = input()

odotY = "Y"
odotN = "N"

def odp(odot):
    if odot == odotY:
        print("Dobře jdeme na to >.< " )
    elif odot == odotN:
        print("Achjo škoda tak někdy příště :( ")

odp(odot)

print("Tak jdem na to :p ")
print("Kámen, nůžky, papír, teď !!! ")

pl1CH = input()

km = "kámen"
nž = "nůžky"
pp = "papír"

lkmp = ("kámen", "nůžky", "papír")
pl2CH = random.choice(lkmp) 


def hra(pl1CH, pl2CH, km, nž, pp):
   if pl1CH == pl2CH:
        print("A sakra plichta tak nic jdem na čaj")
if pl1CH == km:
    if pl2CH == nž:
        print("Achjo, vyhrál jsi, díky za hru <3")
if pl1CH == km:
    if pl2CH == pp:
        print("Jupíí vyhrál jsem, ale nesmutni třeba vyhraješ příště")
if pl1CH == nž:
    if pl2CH == pp:
        print("Achjo, vyhrál jsi, díky za hru <3")
if pl1CH == nž:
    if pl2CH == km:
        print("Jupíí vyhrál jsem, ale nesmutni třeba vyhraješ příště")
if pl1CH == pp:
    if pl2CH == km:
        print("Achjo, vyhrál jsi, díky za hru <3")
if pl1CH == pp:
    if pl2CH == nž:
        print("Jupíí vyhrál jsem, ale nesmutni třeba vyhraješ příště")



hra(pl1CH, pl2CH, km, nž, pp)
