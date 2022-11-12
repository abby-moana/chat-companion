print("\n---------- MENU --------------")
print("""      1 -----> Add an item
      2 -----> Search
      3 ------> Exit (y/n)
------------------------------""")

personal_data = {}

option = int(input("What do you want to do? (1-3): "))

if option == 1:
    fullname = input("Full Name: ").title()
    age = input("Age: ")
    gender = input("Gender: ").title()
    address = input("Address: ").title()
    number = input("Phone Number: ")
    print("Saved!")

    personal_data[fullname] = {}
    personal_data[fullname]["Full Name"] = fullname
    personal_data[fullname]["Age"] = age
    personal_data[fullname]["Gender"] = gender
    personal_data[fullname]["Address"] = address
    personal_data[fullname]["Phone Number"] = number

    print(personal_data)

