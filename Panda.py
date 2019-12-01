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

pandasInZoo={"male":pan,"female":meng,}

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
          
#new examples, but this time from the pandasInZoo from line 13
#results mengmeng likes None, because not defined yet
favFoodOf(pandasInZoo["female"])
#now assign the favfood for mengmeng as well..
pandasInZoo["female"].data["favfood"] = "Bamboo"
          
          #print again
favFoodOf(pandasInZoo["female"])
#there we go it prints she likes bamboo as well!

         
