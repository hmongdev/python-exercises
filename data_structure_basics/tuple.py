#/////////////////////////tuple///////////////////////////
#tuples are like lists, but they're immutable
#lists are defined by [], tuples use ()
#use cases: tuples are used when you don't want to change your data (i.e., sensitive information)

numbers = (1, 2, 3, 3)
# numbers[0] = 10 #//this would cause an error bc tuples are immutable

numbers.count(3) #would return 2 since there are 2 threes in numbers
