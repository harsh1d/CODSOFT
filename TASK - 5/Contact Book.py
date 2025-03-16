"""
Contact Information: Store name, phone number, email, and address for each contact.
Add Contact: Allow users to add new contacts with their details.
View Contact List: Display a list of all saved contacts with names and phone numbers.
Search Contact: Implement a search function to find contacts by name or phone number.
Update Contact: Enable users to update contact details.
Delete Contact: Provide an option to delete a contact.
User Interface: Design a user-friendly interface for easy interaction
"""

import os
from datetime import datetime
import re

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        if not name.isalpha():
            print("Invalid name. Please enter only characters.")
            return
        if not phone.isdigit() or len(phone) != 10:
            print("Invalid phone number. Please enter a 10-digit number.")
            return
        if '@' not in email:
            print("Invalid email. Please include '@' in the email.")
            return
        if not re.match("^[A-Za-z0-9 ]+$", address):
            print("Invalid address. Please enter only characters and integers.")
            return
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print(f"Contact {name} added successfully.")
        self.save_contacts()

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for contact in self.contacts:
                print(contact)

    def search_contact(self, search_term):
        results = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        if not results:
            print("No contacts found.")
        else:
            for contact in results:
                print(contact)

    def update_contact(self, name, new_phone=None, new_email=None, new_address=None):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                if new_phone:
                    contact.phone = new_phone
                if new_email:
                    contact.email = new_email
                if new_address:
                    contact.address = new_address
                print(f"Contact {name} updated successfully.")
                self.save_contacts()
                return
        print("Contact not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Contact {name} deleted successfully.")
                self.save_contacts()
                return
        print("Contact not found.")

    def save_contacts(self):
        now = datetime.now()
        filename = f"Contact Book {now.strftime('%d-%m-%Y %H-%M-%S')}.txt"
        filepath = os.path.join(os.path.dirname(__file__), filename)
        with open(filepath, 'w') as file:
            for contact in self.contacts:
                file.write(str(contact) + '\n')

def main():
    contact_book = ContactBook()
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)
        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            new_phone = input("Enter new phone number (leave blank to keep current): ")
            new_email = input("Enter new email (leave blank to keep current): ")
            new_address = input("Enter new address (leave blank to keep current): ")
            contact_book.update_contact(name, new_phone, new_email, new_address)
        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
