def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.lower().strip()
    return cmd, *args

def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added"
    except:
        print("Enter 'add <name> <number>'")

def change_contact(args, contacts):
    try: 
        name, new_number = args
        if name in contacts:
            contacts[name] = new_number
            return "Contact updated"
        return "Contact not found"
    except:
        print("Enter 'change <name> <new_number>'")

def show_phone(args, contacts):
    try:
        name = args[0]
        if name in contacts:
            return contacts[name]
        return "Contact not found" 
    except:
        print("Enter 'phone <name>'")
    
def show_all(args, contacts):
    if contacts:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    return "No contacts available."
    
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ").strip().lower()
        command, *args = parse_input(user_input)
        
        match command:
            case 'exit' | 'close':
                print('Good bye!')
                break
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, contacts))
            case "change": 
                print(change_contact(args, contacts))
            case "phone": 
                print(show_phone(args, contacts))
            case "all":
                print(show_all(args, contacts))
            case _:
                print("Invalid command")
    
if __name__ == "__main__":
    main()