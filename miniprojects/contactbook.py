contacts = {}

def add_contacts():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
    print("Contact added.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("\nSaved Contacts:")
        for name, phone in contacts.items():
            print(f"Name: {name}, Phone: {phone}")

def search_contacts():
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"Name: {name}, Phone: {contacts[name]}")
    else:
        print("Contact not found!")

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")    
    
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_contacts()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contacts()
    elif choice == "4":
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1-4.")
