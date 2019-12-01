#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Panda():
    def __init__(self,name,age,hungry):
        self.data = {"name":name,"age":age,"hungry":hungry}
        if self.data.get("hungry") == True:
            print("I'am Hungry!")

pan = Panda("Big Panda","N/A",True)

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
