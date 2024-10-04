def add_contact(args, contacts):
    name, phone_number = args
    contacts[name] = phone_number

    return "Contact added."


def change_contact(args, contacts):
    name, new_phone_number = args
    contacts[name] = new_phone_number

    return "Contact updated."


def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return f"{name} has the following phone number: {contacts[name]}."
    else:
        return f"{name} is not found."


def show_all(contacts):
    result = ''
    for contact, phone in contacts.items():
        print(f"{contact} has phone number: {contacts[contact]}")
