"""
String functions categories 
    1. Types - type(), str()
    2. Math - len(), count()
    3. Transformations - replace(), 'H' + 'i', f{}, split(), 'ha' * 2 Extraction('cat'[0])
    4. Cleaning - Clean Whitespaces(lstrip(),rstrip(),strip()), Clean cases(lower(),upper())
    5. Search - startswith(), endswith(), find(), 'a' in 'cat'
    6. Validation - isalpha(), isnumeric()

"""

# Types
name ="maria"
print(type(name))

age = 18
#print("your age is:" + age)
print("your age is:" + str(age))
age = age + 5
age = str(age)
print(type(age))
print('-----------------------------')

# Math
# len() - counts everything with spaces
password = "12345a"
print(len(password)) # no of numbers or string

number = "    789"
print(len(number))

# text
# count() - returns how often a word appears in string
text = """Python is programming language.Python is easy to learn."""
print(text.count("Python"))
print("------------------------------------------")

# Data Transformation
# replace(old value, new value)
price = "1234,56"
print(price.replace(",","."))

phone = "213-2345-65"
print(phone.replace("-","/"))

price = "$1488.33"
print(price.replace("$",""))

number = "+49 (176) 123-3456"
print(number.replace("+", "00").replace("(","").replace(")","").replace(" ","").replace("-",""))

# Join strings
first_name = "Michael"
last_name  = "Scott"
last_name = first_name + " " + last_name
print(last_name)

# f-string - formmated string
name = "Sam"
age = 19
is_student = False
print("Name is + name +","age " +str(age)+", student status " +str(is_student)+ ".")
print(f"name is {name}, age is {age}, student status is {is_student}")

print(f"2+ 3 = {2 + 3}")

print(f"{{This is me}}")