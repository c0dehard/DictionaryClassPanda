def check(elem, seq):
    """
    #### returns True or False
    ###  checks if element exists in the given sequence
    #### Example:
        x = check("d","abcde")
    ###  print(x)
    ### True
	"""
    return elem in seq

def reversed_list(n,downToZero=True):
    """
    #### returns a list from n to lowest in a descending order
    ###  input has to be an integer
    #### Example:
        x = reversed_list(10,False)
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

def count_vowels(string):
    """
    #### returns amount of vowels in given string
    #### Example:
        x = count_vowels("The meaning of life, 42 to proof this, is this text"*3)
    ###  print(x)
    ### 42
	"""
    vowels,counter = ("aeiou"),0
    for i in string:
        if i.lower() in vowels : counter+=1
    return counter

def increment_arr(array,increment=1):
    """
    #### returns an incremented array
    #### Example:
       x = [1,2,3,4,5]
     increment_arr(x)
    ###  print(x)
    ### [2, 3, 4, 5, 6]
	"""
    for num in range(len(array)):
        array[num]=array[num]+increment
    return array

def decrement_arr(array,decrement=1):
    """
    #### returns an decremented array
    #### Example:
       x = [1,2,3,4,5]
     decrement_arr(x)
    ###  print(x)
    ### [0, 1, 2, 3, 4]
	"""
    for num in range(len(array)):
        array[num]=array[num]-decrement
    return array

def ytv_id(url):
	"""
    #### returns YouTube Video ID
    ##### wheter regular or shortened format
    ##### Example:
	 x = ytv_id(input('enter url: '))
    ###  print(x)
	 >>> enter url: https://www.youtube.com/watch?v=jNQXAC9IVRw
    ### jNQXAC9IVRw
	"""
	vid = url.split('/') ; return vid[-1].split('watch?v=')[-1]

def just_ints(string,as_int=True):
	"""
	#### returns a list of integers as string or integer
	##### by default as integer list
	#### Example:
		x = just_ints("1.1 example now 2 or four words",False)
	###  print(x)
	 >>> ['1', '1', '2']
	"""
	import re
	results = re.findall(r"\d+",string)
	if as_int:
		# TODO: need to learn more about -> map
		# new solution is inspired by
		# https://stackoverflow.com/questions/7368789/convert-all-strings-in-a-list-to-int
		return list(map(int, results))
	return results

def all_rand(upTo=50):
    """
    ### returns as many random numbers
    ### up to the given number in a list
    if nothing's set basic will be 50
    #### Example:
        x = all_rand(10)
    ###  print(x)
     >>> [9, 8, 2, 5, 2, 6, 2, 0, 4, 1]
    """
    x=[]
    import random
    for nums in range(upTo) : x.append(int(random.randrange(0,upTo)))
    return x

def avg_wordlen(values,delimiter = " "):
    """
    #### returns the average length of given values: 
    if not specified, space will be the basic delimiter
    #### Example:
        x = avg_wordlen("One two three four five six")
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
Figured out accidentally, LOVE IT..
Well, maybe I'll just shrink the docstrings down as i regular write 'em
it’s better for CLI e.g. if a user writes help(function) ..
In my opinion are documentation strings very ugly to look they ain't formated.
"""
