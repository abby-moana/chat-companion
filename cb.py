dictionary = {}

print("\nHello! I'm CC your chat companion.")

user = input("\nYou: ").title()
if user == "exit":
    exit()
elif user == "hi" or "hello" or "hey":
    print("Hello! What is your name?")
    name = input("You: ").title()
    print(name, ", teach me anything. y/n")

while True:
    answer = input("Answer: ")
    if answer == "y":
        while True:
            print("\nType 'Done' if already satisfied in teaching CC.")
            user = input("If I say: ").title()
            if user == "Done":
                break
            cc = input("CC will say: ").title()
            dictionary[user] = cc
    else:
        print("Too bad. Maybe you can teach me next time :D")
        break

while True:
    user = input("You: ").title()
    if user == "Exit":
        break
    if user in dictionary:
        print("CC: ", dictionary[user])
    else:
        print("I'm sorry I haven't learned that one yet.")
        continue
