def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Enter user name."
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Give me name and phone please."
    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    return cmd.lower(), *args


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} added."


@input_error
def command_change(args, contacts):
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return f"Contact {name} updated."


@input_error
def command_phone(args, contacts):
    name = args[0]
    return f"{name}: {contacts[name]}"


@input_error
def command_all(contacts):
    if not contacts:
        raise KeyError
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ("exit", "close"):
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(command_change(args, contacts))

        elif command == "phone":
            print(command_phone(args, contacts))

        elif command == "all":
            print(command_all(contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
