import os

# BECAUSE NT AIN'T MY BEST FRIEND
os.system('clear' if os.name != 'nt' else 'cls')


def avgWordLen(values,delimiter = " "):
    """
    #### returns the average length of given values: 
    if not specified, space will be the basic delimiter
    #### Example:
        x = avgWordLen("One two three four five six")
    ###  print("avg is: ",x)
     >>> avg is 3.6666666666666665
    """
    enteredValues=values.split(" ")
    x=0
    for value in range(len(enteredValues)):
        x=x+len(enteredValues[value])
    return x/len(enteredValues)
