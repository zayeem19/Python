name = input("enter your name: ")

if len(name) < 3:
    print("error! name should be atleast 3 character")

elif len(name) > 50:
    print("error! name cannot be 50 characters")

else:
    print(f"name is ok : {name}")
