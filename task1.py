DATA_FILE = 'contacts.txt'

def load_contacts():
    contacts = []
    try:
        with open(DATA_FILE, 'r') as f:
            for line in f:
                name, phone, email = line.strip().split(',')
                contacts.append({'name': name, 'phone': phone, 'email': email})
    except FileNotFoundError:
        pass
    return contacts

def save_contacts(contacts):
    with open(DATA_FILE, 'w') as f:
        for c in contacts:
            f.write(f"{c['name']},{c['phone']},{c['email']}\n")

def add_contact(contacts):
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    contacts.append({'name': name, 'phone': phone, 'email': email})
    save_contacts(contacts)
    print("Contact added.\n")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for i, c in enumerate(contacts, 1):
            print(f"{i}. {c['name']} - {c['phone']} - {c['email']}")
    print()

def main():
    contacts = load_contacts()
    while True:
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Exit")
        choice = input("Choose option: ")
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == '__main__':
    main()
