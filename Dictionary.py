print("\n---------- CONTACT TRACING MENU --------------")
print("""      1 -----> Add an item
      2 -----> Search
      3 ------> Exit (y/n)
----------------------------------------------""")

personal_data = {}

while True:
    option = int(input("\nWhat do you want to do? (1-3): "))
    if option == 1:
        fullname = input("\nFull Name: ").title()
        age = input("Age: ")
        gender = input("Gender: ").title()
        address = input("Address: ").title()
        number = input("Phone Number: ")
        email = input("Email: ")
        time = input("Time of visit: ")
        temperature = input("Temperature: ")
        print("Saved!")

        personal_data[fullname] = {}
        personal_data[fullname]["Full Name"] = fullname
        personal_data[fullname]["Age"] = age
        personal_data[fullname]["Gender"] = gender
        personal_data[fullname]["Address"] = address
        personal_data[fullname]["Phone Number"] = number
        personal_data[fullname]["Email"] = email
        personal_data[fullname]["Time"] = time
        personal_data[fullname]["Temperature"] = temperature

    elif option == 2:
        search = input("Full name: ").title()
        for key, value in personal_data[search].items():
            print(key, ":", value)
    elif option == 3:
        Exit = input("\nExit? (y/n): ")
        if Exit == "n":
            continue
        else:
            print("\n----------Thank you for using the program----------")
            break
    else:
        print("\nInvalid input! \nExiting the program...")
        break
