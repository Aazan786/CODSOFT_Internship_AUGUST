class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("Contact book is empty.")
        else:
            print("Contact List:")
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. {contact.name} - Phone: {contact.phone}")

    def search_contact(self, query):
        results = []
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone:
                results.append(contact)
        return results

    def update_contact(self, old_name, new_contact):
        for idx, contact in enumerate(self.contacts):
            if contact.name == old_name:
                self.contacts[idx] = new_contact
                break

    def delete_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name != name]

def main():
    contact_book = ContactBook()

    while True:
        print("Contact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            email = input("Enter contact email: ")
            address = input("Enter contact address: ")
            contact = Contact(name, phone, email, address)
            contact_book.add_contact(contact)
            print("Contact added successfully.")

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            results = contact_book.search_contact(query)
            if results:
                print("Search Results:")
                for idx, contact in enumerate(results, start=1):
                    print(f"{idx}. {contact.name} - Phone: {contact.phone}")
            else:
                print("No matching contacts found.")

        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            new_name = input("Enter updated contact name: ")
            new_phone = input("Enter updated contact phone number: ")
            new_email = input("Enter updated contact email: ")
            new_address = input("Enter updated contact address: ")
            new_contact = Contact(new_name, new_phone, new_email, new_address)
            contact_book.update_contact(name, new_contact)
            print("Contact updated successfully.")

        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)
            print("Contact deleted successfully.")

        elif choice == '6':
            break

if __name__ == "__main__":
    main()
