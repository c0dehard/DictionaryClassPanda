def reversedList(n,downToZero=True):
    """
    #### returns a list from n to lowest in a descending order
    ###  input has to be an integer
    #### Example:
        x = reversedList(10,False)
    ###  print(x)
    ### [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
	"""
    list=[]
    one = 0 if not downToZero else 1
    # todo improve this someday
    for i in range(n+one):
        list.append(n)
        n-=1
    return list

def countVowels(string):
    """
    #### returns amount of vowels in given string
    #### Example:
        x = countVowels("The meaning of life, 42 to proof this, is this text"*3)
    ###  print(x)
    ### 42
	"""
    vowels,counter = ("aeiou"),0
    for i in string:
        if i.lower() in vowels : counter+=1
    return counter

def incrementArr(array,increment=1):
    """
    #### returns the given array increments each number
    #### Example:
       x = [1,2,3,4,5]
     incrementArr(x)
    ###  print(x)
    ### [2, 3, 4, 5, 6]
	"""
    for num in range(len(array)):
        array[num]=array[num]+increment
    return array

def decrementArr(array,decrement=1):
    """
    #### returns the given array decrements each number
    #### Example:
       x = [1,2,3,4,5]
     decrementArr(x)
    ###  print(x)
    ### [0, 1, 2, 3, 4]
	"""
    for num in range(len(array)):
        array[num]=array[num]-decrement
    return array

def ytvID(url):
	"""
    #### returns YouTube Video ID from given URL
    ##### wheter regular or shortened format
    ##### Example:
	 x = ytvID(input('enter url: '))
    ###  print(x)
	 >>> enter url: https://www.youtube.com/watch?v=jNQXAC9IVRw
    ### jNQXAC9IVRw
	"""
	vid = url.split('/');return vid[-1].split('watch?v=')[-1]

def justInts(string):
    """
    #### returns a list of integers 
    ##### from a specified string
    #### Example:
        x = justInts("1.1 example now 2 or four words")
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
        x = allRand(10)
    ###  print(x)
     >>> [9, 8, 2, 5, 2, 6, 2, 0, 4, 1]
    """
    x=[]
    import random
    for nums in range(upTo):x.append(int(random.randrange(0,upTo)))
    return x

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

# TODO Add more helpful functions
"""
I didn’t knew python comments where formatable in vscode!
Figured out accidentally, LOVE IT :D
"""
