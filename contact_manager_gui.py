import tkinter as tk
from tkinter import messagebox
import json
import os

# Load contacts from a file
def load_contacts():
    if os.path.exists("contacts.json"):
        with open("contacts.json", "r") as file:
            return json.load(file)
    return []

# Save contacts to a file
def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

# Add a new contact
def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    
    if name and phone and email:
        contact = {"name": name, "phone": phone, "email": email}
        contacts.append(contact)
        save_contacts()
        refresh_contact_list()
        clear_entries()
        message_label.config(text="Contact added successfully!")
    else:
        message_label.config(text="Please fill in all fields.")

# Edit an existing contact
def edit_contact():
    selected = contact_list.curselection()
    if selected:
        index = selected[0]
        contacts[index]["name"] = entry_name.get()
        contacts[index]["phone"] = entry_phone.get()
        contacts[index]["email"] = entry_email.get()
        save_contacts()
        refresh_contact_list()
        clear_entries()
        message_label.config(text="Contact updated successfully!")
    else:
        message_label.config(text="Select a contact to edit.")

# Delete a selected contact
def delete_contact():
    selected = contact_list.curselection()
    if selected:
        index = selected[0]
        contacts.pop(index)
        save_contacts()
        refresh_contact_list()
        clear_entries()
        message_label.config(text="Contact deleted successfully!")
    else:
        message_label.config(text="Select a contact to delete.")

# Refresh the contact list display
def refresh_contact_list():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Clear entry fields
def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)

# Load contacts and initialize
contacts = load_contacts()

# GUI setup
root = tk.Tk()
root.title("Contact Manager")

# Labels and Entries
tk.Label(root, text="Name:").grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Phone:").grid(row=1, column=0, padx=5, pady=5)
entry_phone = tk.Entry(root)
entry_phone.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Email:").grid(row=2, column=0, padx=5, pady=5)
entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1, padx=5, pady=5)

# Buttons
add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.grid(row=3, column=0, pady=5)

edit_button = tk.Button(root, text="Edit Contact", command=edit_contact)
edit_button.grid(row=3, column=1, pady=5)

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.grid(row=3, column=2, pady=5)

# Contact List Display
contact_list = tk.Listbox(root, width=50, height=10)
contact_list.grid(row=4, column=0, columnspan=3, padx=5, pady=5)
refresh_contact_list()

# Feedback Label
message_label = tk.Label(root, text="")
message_label.grid(row=5, column=0, columnspan=3)

# Run the application
root.mainloop()
