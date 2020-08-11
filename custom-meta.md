### For better understanding what a metaclass is and how to use it...
#### Important, you'll need to know [how python builds classes](https://docs.python.org/3/reference/datamodel.html#creating-the-class-object) as well you should know [dunder methods](https://docs.python.org/3/reference/datamodel.html)

> Yes [type()](https://docs.python.org/3/library/functions.html#type) can create classes

 this is not for [Go](https://golang.org/) fans only, <small>maybe it's useful knowledge to someone else new to Python</small>
```python
# This syntax is...
Foo = type('Foo',(),{})
# ..equivalent to this
# class Foo:
#   pass

class Bar:
    def laugh(self):
        print("hahaha")

# Demo of inheritance with this fun syntax
Test = type('Foo',(Bar,),{"just_a_number":7})   
t = Test()                              
t.laugh()
print(t.just_a_number)
```
```shell
hahaha
7
```


## Custom metaclass
```python
class CustomMeta(type):
    # Reminder, `new` dunder gets called before init. While object creation.
    def __new__(self,name,bases,attrs):
        print(attrs)
        return type(name,bases,attrs)

    def __init_(self):
        pass


# Sample animal inherits from custom metaclass
class Panda(metaclass=CustomMeta):
    """I bet you see this docstring printed as well"""
    fav_food = "Bamboo"
    loves_code = True

    def activity(self):
        print("Zzz...")
```
Gets printed at create time without even instance it, because of the overwritten metaclass
```shell
{'__module__': '__main__', '__qualname__': 'Panda', '__doc__': 'I bet you see this docstring printed as well', 'fav_food': 'Bamboo', 'loves_code': True, 'activity': <function Panda.activity at 0x7f94b6fca0>}
```
