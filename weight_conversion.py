#purpose: convert input into kg or lbs
#concepts: variables, inputs, control flow, round()
#obstacles: type conversions: int() and str()

weight = str(input("Enter number: "))
units = str(input("kg or lbs? "))

if units.lower() == "kg":
    conversion = round(int(weight)//2.205, 2)
    print(weight + " " + units + " is " + str(conversion) + " pounds")
elif units.lower() == "lbs":
    units = "lbs"
    conversion = round(int(weight)*2.205, 2)
    print(weight + " " + units + " is " + str(conversion) + " kg")
else:
    print("Error. Please write units as 'kg' or 'lbs' ")