# /////////////////////////while loops///////////////////////////
#purpose: understand syntax of while loops
#concepts: 3 parts of while loop: start condition, end condition, and change (increment)




i = 1 #start of loop
while i <= 1_000: #end condition
    print(i) #print i
    i += 1  #change, increment by 1; this can also be written i = i + 1
    
# /////////////////////////multiplication operator with i///////////////////////////
i = 1 
while i <= 10: #end condition
    print(i * "*") #whatever i is, multiply it by the string
    #i.e., if i = 5 then the console will print *****
    i += 1