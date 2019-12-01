#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Panda():
    def __init__(self,name,age,hungry):
        self.data = {"name":name,"age":age,"hungry":hungry}
        if self.data.get("hungry") == True:
            print("I Am Hungry!")

pan = Panda("Big Panda","N/A",True)

print(f'And my name is: ,,{pan.data.get("name")}"')

#test namenändern / change name test      
pan.data["name"] = "c0deN@c0dehard"
print(f'Name changed to: {pan.data.get("name")}')
#YES i LOVE Format Strings!
