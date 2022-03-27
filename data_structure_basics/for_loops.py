#/////////////////////////for loops///////////////////////////
# concepts: for loops are useful for iterating over each item in a list
# each item holds only one value
# for loop advantages over while loops
# 1. no len() function
# 2. no square brackets
# 3. no start i condition
# 4. no increment code

#for loop
numbers = [1, 2, 3, 4, 5]
for item in numbers:
    print(item) #this will print each item on a new line

#this can also be achieved with while loop, just takes extra code writing
i = 0
while i < len(numbers):
    print(numbers[i]) 
    i+=1