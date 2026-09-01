"""
DataTypes - 
            None datatype
            single value(Primitive datatype) - int, float, string, boolean,complex
            Multi-values/Data structures/Collections/Containers - list, tuple, dict
            Date&Time - date, time, datetime

"""


a = 10 # int
print(type(a))
b = 3.15 # float
c = "Hello" # string
d = "1" # str
e = 'Hi' # str
f = True # bool
g = False # bool
h = None # none datatype - no value/ nothing/ unknown, it's used to show absence of any data
i = "" # str - blank
j = " " # str - empty space 



"""
standard library
     |
functions 
    - standalone functions - print(),type()
    - method of class - upper(), replace()
    - operations - +, /, >, <, ==, in, or
    - 3rd party libraries - pandas, numpy, tensorflow
    - user-defined 
"""

"""
function - independent block of code
syntax :
function_name(value)
methods - functions belong to objects/classes
syntax :
value.method_name()
"""

text = "python"
number = 10
print(len(text))
#print(len(number))
print(text.upper())
#print(number.upper())
print(number.bit_length())
#print(text.bit_length())


age = 18
height = 5.5
name = "Mario"
student = str(input("Are you a student?"))
education = None
print("My name is",name,"age is",age,"height is",height,"I am student",student)
print(type(age))
print(type(height))
print(type(name))
print(type(student))
print(type(education))
print(len(name))
print(len(student))
