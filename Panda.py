#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Panda():
    def __init__(self,name,age,hungry):
        self.data = {"name":name,"age":age,"hungry":hungry}
        if self.data.get("hungry") == True:
            print("I Am Hungry!")

pan = Panda("Big Panda","N/A",True)
meng = Panda("MengMeng","N/A",False)
testo = Panda("Testo","N/A",False)

pandasInZoo={"male":pan,"female":meng,"testo":testo}

print(f'And my name is: ,,{pan.data.get("name")}"')


pan.data["name"] = "c0deN@c0dehard"
print(f'Name changed to: {pan.data.get("name")}')



#add key  and value to a dict
pan.data["favfood"] = "Bamboo"


#insert any panda to get his favfood printed
def favFoodOf(name):
    hisfavfood = name.data.get("favfood")
    print(f'{name.data.get("name")} likes {hisfavfood}')

# just pass the object as parameter of this function
favFoodOf(pan)
          
#example 2 and 3, but this time from the pandasInZoo on line 12
#results mengmeng likes None, because not defined yet
favFoodOf(pandasInZoo["female"])
#now assign the favfood for mengmeng as well..
pandasInZoo["female"].data["favfood"] = "Bamboo"
favFoodOf(pandasInZoo["female"])
#there we go it prints she likes bamboo as well!



#try to remove age of testo bc it's N/A
# and  insert it new with the value 1
print(testo.data.get("name")+"'s age was: ",testo.data.get("age"))
#remove
pandasInZoo["testo"].data.pop("age")
#add new key and value
pandasInZoo["testo"].data["age"]= 1
print(f"and it's age now is: {testo.data.get('age')} and, his age is a Datatype of: {type(testo.data.get('age'))}")
#OH i realy like format Strings!!!





'''
fresh spahetti

'''

aPan = Panda("AlbertPanda","",False)
bPan = Panda("BallPanda","",False)
cPan = Panda("CutiePan","",False)

typeof = {"m":(aPan.data.get("name"),bPan.data.get("name")),"f":cPan.data.get("name")}

#aint rly OOP im bored just messing a bit

#lets see what names in what basic gendertypes
print(f'Male Panda Names: {gender["m"]}\nFemale Panda Names: {typeof["f"]}')


          
