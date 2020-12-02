# Resume Python for everyone: Cap 2

## Values and variables
A **value** is a unit of data that belongs a data type, and a **variable** is just a name given to a value.
As an analogy, a variable is a box that stores a value. 

## Type
A type is a category of values that share some similar characteristics. In python everything is a object, and so are the
types. For example when we refer to an integer  in python, we are talking about an instance
of the class "int".

To know the type of a object we need to do the type function:
```python
myobject = 1
type(object) # "int"

myobject =  "number 1"
type(object) # "str"

myobject = 2.2
type(myobject) # "Float

```
Even when we create a class, and an instance of that class, we are creating a new type.

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hi, I'm {self.name}"

peter = Person("Peter")
print(type(peter))
# <class '__main__'.Person> 
```

So yeah, Peter belongs to the class Person, and he has a type "Person".

There are seven built-in data types in Python: 
### Numeric:
Floats, Integers  
### Text:
Strings
### Boolean:
bool: True or False, 1 or 0
### Sequence
List, tuples and range