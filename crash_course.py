# 1-hour python crash course based off the 
# youtube video: https://www.youtube.com/watch?v=kqtD5dpn9C8&ab_channel=ProgrammingwithMosh

#/////////////////////////variables///////////////////////////
age = 29
ethnicity = "Hmong-American"

# multiple word variables are separated by _ (underscore) and no capital letters
first_name = 'Avery'
last_name = 'Yang'

# boolean values are case-sensitive
is_online = True 
# is_online = true //true will cause an error


#/////////////////////////inputs///////////////////////////
name = input('What is your name? ')
print('Hello '+name) #print is a general method that gives us what's inside it. 'Hello' +name is string concatenation

#/////////////////////////types///////////////////////////
# three different types of data
numbers = 10
string = "String"
boolean = True

# type conversion
birth_year = input("What year were you born? ")

# age = 2022 - birth_year #//error: (int)2022 and (str)birth_year are different data types

age = 2022 - int(birth_year) #data types have to match
# print('You are' + age + ' years old.') #//error: concatenation only allowed for str-to-str; nothing else

#these are the type conversations
int()
float()
bool()
str()

# simple calculator
num1 = input("First # ")
num2 = input("Second # ")
sum = int(num1) + int(num2)
print(sum)

#refactored calculator
num1 = float(input("First # ")) #if user inputs decimal, float() will manage that better than int()
num2 = float(input("Second # "))
sum = num1 + num2
print(float(sum))

#/////////////////////////strings///////////////////////////
#strings are immutable, we cannot change them once created

course = 'Python for Beginners' #this is a string object
course.upper() #.upper is a method that is attached to the object named 'course'

print(course.upper()) #//PYTHON FOR BEGINNERS
print(course.lower()) #//python for beginners
print(course.find('y')) #//1; because the index of 'y' is 1 in 'Python for Beginners'
print(course.find('y')) #//-1; because 'Y' doesn't exist
print(course.replace('for', '4')) #//Python 4 Beginners
print('Python' in course) #//True, checking if 'Python' is in variable course; 'in' is an operator

#/////////////////////////math///////////////////////////
print(10 + 3) //13
print(10 - 3) //7
print(10 * 3) //30
print(10 ** 3) //1000
print(10 / 3) //3.3333333333333333
print(10 // 3) //3; this one just returns the integer, not the decimal part of it
print(10 % 3) //1

#augmented assignment operator
x = 10
(x = x + 3) is the same as (x += 3)

# /////////////////////////operator precedence///////////////////////////
this is the same idea as PEMDAS, order of operations
to change operator precedence, just use (10 + 3) * 2

# /////////////////////////comparison operators///////////////////////////
comparison operators
>   greater than
>=  greater than or equal to
<   less than
<=  less than or equal to
==  equal to
!=  not equal to

# /////////////////////////logical operators///////////////////////////
and (true only if both conditiosn are true)
or  (true if at least one condition is true)
not (inverse the boolean)

# /////////////////////////if statements///////////////////////////
temperature = 65
if temperature > 90:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 70: # (70, 90]
    print("It's a nice day")
elif temperature > 40: # (40, 70]
    print("It's chilly")
else:
    print("It's freezing.")
print("Have a great day.")

# syntax:
# 1. no curly braces, blocks are defined with indentation
# 2. else if = elif 
# 3. after a condition, use :#

# /////////////////////////while loops///////////////////////////


