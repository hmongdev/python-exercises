#/////////////////////////range///////////////////////////
# range() is an object that carries a sequence of numbers
# concept: you can iterate over an object using for loop

numbers = range(5) #numbers contains range 0-4, excluding 5
print(numbers) #//range(0,5), this is standard notation for range

#what if we want to see all the numbers in the range?
for item in numbers:
    print(item)
    
#when using 2 params, param1 is starting, param2 is max
numbers = range(10, 15) #10 becomes starting value, 15 is the max value (excluded)
for item in numbers:
    print(item)
    
#when using 3 params, param1 is starting, param2 is max, param3 is the change/step
numbers = range(10, 15, 2) #10 becomes starting value, 15 is the max value (excluded)
for item in numbers:
    print(item)

#typically, you can call range() with for loop
for stuff in range(5):
    print(stuff)
