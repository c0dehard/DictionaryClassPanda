class node:
    def __init__(self,data=None):
        self.data = data
        self.next=None


    def __repr__(self):
        return f"{self.data}"

eins = node("Alpha")
# zwei = node("Beta")
# drei = node("Charlie")

#eins.next = zwei
#zwei.next = drei

eins= node(eins)
print(eins)
print(eins.next)


n = "abc"
if (n:= len(n) > 10):
    print("größer 10")
