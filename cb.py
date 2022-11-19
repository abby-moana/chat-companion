dictionary = {}

print("\nHello! I'm CC your chat companion.")

user = input("\nYou: ").title()
if user == "exit":
    exit()
elif user == "hi" or "hello" or "hey":
    print("Hi! What is your name?")
    name = input("You: ").title()

while True:
    print("\n", name, ", teach me anything. (y/n)")
    answer = input("\nReply: ")
    if answer == "y":
        while True:
            print("\nType 'Done' if already satisfied in teaching CC.")
            user = input("If I say: ").title()
            if user == "Done":
                break
            cc = input("CC will say: ").title()
            dictionary[user] = cc

        print("\nTalk with CC.")
        while True:
            user = input("You: ").title()
            if user == "Exit":
                break
            if user in dictionary:
                print("CC: ", dictionary[user])
            else:
                print("I'm sorry I haven't learned that one yet.")
                continue
