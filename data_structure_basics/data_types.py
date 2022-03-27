#/////////////////////////data types///////////////////////////
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