# /////////////////////////if statements///////////////////////////
# purpose: understand if else structure
# obstacles: none, this is an easy concept for me

# syntax:
# 1. unlike javascript there are no curly braces
# 2. blocks are defined with indentation
# 3. else if = elif 
# 4. after a condition, use (colon) :

temperature = int(input("What's the temperature outside? "))
if temperature >= 88:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature >= 70: # (70, 90]
    print("It's a nice day")
elif temperature >= 40: # (40, 70]
    print("It's chilly")
else:
    print("It's freezing.")
print("Have a great day.")