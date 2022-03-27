#/////////////////////////lists///////////////////////////
#lists in python are arrays in ruby
#concepts: lists(arrays), negative index[-i], range[0:i]

names = ["Jericho", "Elijah", "Dudley", "Minister Miner", "Jasmine"]
print(names[0])

#/////////////////////////negative index///////////////////////////
print(names[-1]) #negative index grabs from the end of the list

#/////////////////////////change values in the list///////////////////////////
names[0] = "Excalibur" #this changes the value at index 0
print(names) #['Excalibur', 'Elijah', 'Dudley', 'Minister Miner', 'Jasmine']

#/////////////////////////range///////////////////////////
print(names[0:3]) #will print names in index 0-2, not including 3
# ['Excalibur', 'Elijah', 'Dudley']

#/////////////////////////list methods///////////////////////////
numbers = [1, 2, 3, 4, 5]
numbers.append(6) # adds 6 to numbers list
numbers.insert(4, "Joby") #at index 4, insert "Joby" // #[1, 2, 3, 4, 'Joby', 5, 6]
numbers.remove(3) #removes 3 from list
numbers.clear() #doesn't receive parameter, removes everything inside list
print(numbers)
print(1 in numbers) #returns boolean value, in this case it's False because we .clear() everything
print(len(numbers)) #this is python's equivalent of .length() in javascript

