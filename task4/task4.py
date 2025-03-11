from utility import parse_input, add_contact, change_contact, show_phone, show_all

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(f"{"Name":>10}{"Phone":>15}")
            for i in show_all(contacts):
                print(f"{i[0]:>10}{i[1]:>15}")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
