### For better understanding what a metaclass is and how to use it...
#### Important, you'll need to know [how python builds classes](https://docs.python.org/3/reference/datamodel.html#creating-the-class-object) as well you should know [dunder methods](https://docs.python.org/3/reference/datamodel.html).

Yes [type()](https://docs.python.org/3/library/functions.html#type) can create classes
this is not for [Go](https://golang.org/) fans only, <small>maybe it's useful knowledge to someone else new to Python.
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
Gets printed at create time without even instance it, because of the overwritten metaclass.
```shell
{'__module__': '__main__', '__qualname__': 'Panda', '__doc__': 'I bet you see this docstring printed as well', 'fav_food': 'Bamboo', 'loves_code': True, 'activity': <function Panda.activity at 0x7f94b6fca0>}
```

## Metaclasses can be really powerful be careful with them, only use when there's a need!
For example, check for non dunder attributes names and make 'em uppercase, by adding to an internal dictionary if non dunder and return upper, so the new object will automatically have uppercase attributes after its created.
```python
class CustomMeta(type):
    def __new__(self,cname,bases,attrs):
        print(attrs)

        a = {}
          
        for name, val in attrs.items():
            if name.startswith("__"):
                 a[name] = val
            else:
                a[name.upper()] = val
        print(a)
        return type(cname,bases,a) 

class lowercase_class_name(metaclass=CustomMeta):
    lowercase_var_name = 1
    def hello(self):
        print("hi")

```
As you can see, all lower case letters are now written in capital letters.
```
{'__module__': '__main__', '__qualname__': 'lowercase_class_name', 'lowercase_var_name': 1, 'hello': <function lowercase_class_name.hello at 0x7f848b4c10>}
{'__module__': '__main__', '__qualname__': 'lowercase_class_name', 'LOWERCASE_VAR_NAME': 1, 'HELLO': <function lowercase_class_name.hello at 0x7f848b4c10>}
```
