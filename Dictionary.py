print("\n---------- MENU --------------")
print("""      1 -----> Add an item
      2 -----> Search
      3 ------> Exit (y/n)
------------------------------""")

option = int(input("What do you want to do? (1-3): "))
if option == 1:
    full_name = input("Full name: ")
    gender = input("Gender: ")
    age = input("Age: ")
    bday = input("Birthday: ")
    address = input("Address: ")
    number = input("Phone Number: ")

