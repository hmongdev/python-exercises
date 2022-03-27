#/////////////////////////strings///////////////////////////
# concepts: strings can be manipulated via methods
# .replace("arg1", "arg2") //this finds arg1 inside the string and replaces it with arg2
# in operator checks to see if 'Python' is in variable course
# strings are immutable, we cannot change them once created

course = 'Python for Beginners' #this is a string object
course.upper() #.upper is a method that is attached to the object named 'course'

print(course.upper()) #//PYTHON FOR BEGINNERS
print(course.lower()) #//python for beginners
print(course.find('y')) #//1; because the index of 'y' is 1 in 'Python for Beginners'
print(course.find('y')) #//-1; because 'Y' doesn't exist
print(course.replace('for', '4')) #//Python 4 Beginners
print('Python' in course) #//True, checking if 'Python' is in variable course; 'in' is an operator