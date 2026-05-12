#Weight conversion program
weight=float(input("Enter your weight: "))
unit= input("kilogram or pound (K or LBS):")

if unit== "kg":
    result = weight * 2.205
    print(f"the weight in lbs will be: {round(result,3)}LBS")
else :
    result = weight / 2.205
    print(f"the weight in kg will be: {round(result,3)}kg")

