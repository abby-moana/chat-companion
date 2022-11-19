dictionary = {}

print("\nHello! I'm CC your chat companion.")


while True:
    user = input("\nYou: ")
    if user == "exit":
        break
    elif user == "hi" or "hello" or "hey":
        print("What is your name?")
        name = input("You: ").title()
        print("How are you, ", name, "?")
        user = input("You: ")
        print("CC is happy that you are doing well, ", name, ".")
        print("\nTeach me anything. y/n")

