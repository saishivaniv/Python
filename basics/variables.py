# Variables
# It is a name you create to store a value, in order to use it later in your code

name = "maria"
print(name,"learning python")
print(name,"wants to become python expert")

language = "Python"
print(name,"learning", language)
print(name,"wants to become", language, "expert")


info = "info@maria.com"
print("Contact",info)




# input() - get something from the users   built-in function 
input("enter your name") #reads the user's response but immediately discards
name = input("Enter your Name:")
print("You are", name)

# Hard Coded(Static)Values - fixed piece of data written directly into your code that never changesat runtime.
# Dynamic Values - data entered by the user that can vary each time the program runs. 

name = input("Enter your Name:")
country = "India"
print(name, "comes from", country)