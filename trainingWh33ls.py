def justInts(string):
    """
    ### returns a list of integers 
    ### from a specified string
    #### Example:
        x = justInts(input("Just get ints: "))
    ###  print(x)
     >>> ['1', '1', '2']
    """
    import re
    return re.findall(r"\d+",string)

def allRand(upTo=50):
    """
    ### returns as many random numbers
    ### up to the given number in a list
    if nothing's set basic will be 50
    #### Example:
        x = anyRand(10)
    ###  print(x)
     >>> [9, 8, 2, 5, 2, 6, 2, 0, 4, 1]
    """
    x=[]
    import random
    for nums in range(upTo):
        x.append(int(random.randrange(0,upTo)))
    return x

# TODO Add more helpful functions
"""
I didn’t knew python comments where formatable as well in vscode!
Figured out accidentally :D
"""
