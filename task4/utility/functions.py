def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact updated."

def show_phone(args, contacts):
    name = args[0]
    phone = contacts.get(name)
    return phone

def show_all(contacts):
    list_of_contacts = []
    for key, value in contacts.items():
        list_of_contacts.append([key, value])
    return list_of_contacts