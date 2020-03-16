def justInts(string):
    """
    ## returns a list of integers from the specified string
    #### Example:
        x = justInts(input("Just get ints: "))
    ###  print(x)
    """
    import re
    return re.findall(r"\d+",string)
    # del re # I'm a fool sometimes, no code execution in this scope after return statement
    
# TODO Add more helpful functions
"""
I didn’t knew python comments where formatable as well in vscode!
Figured out accidentally :D
"""
