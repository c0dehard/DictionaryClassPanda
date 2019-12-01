#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Panda():
    def __init__(self,name,age,hungry):
        self.data = {"name":name,"age":age,"hungry":hungry}
        if self.data.get("hungry") == True:
            print("I'am Hungry!")

pan = Panda("Big Panda","N/A",True)

print(f'And my name is: ,,{pan.data.get("name")}"')
