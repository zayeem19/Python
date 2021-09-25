weight = int(input("enter your weight: "))

unit = input(f"is your weight in kg or lb? ")
if unit.upper() == "LB":
    print(weight*0.45)

else:
    unit.upper() == "KG"
    print(weight/0.45)
