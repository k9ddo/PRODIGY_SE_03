import tkinter as tk
from tkinter import simpledialog, messagebox

contacts = []

def add_contact():
    name = simpledialog.askstring("Input", "Enter Name")
    phone = simpledialog.askstring("Input", "Enter Phone")
    email = simpledialog.askstring("Input", "Enter Email")
    if name and phone and email:
        contacts.append({"name": name, "phone": phone, "email": email})
        update_list()

def delete_contact():
    selected = listbox.curselection()
    if selected:
        del contacts[selected[0]]
        update_list()

def update_list():
    listbox.delete(0, tk.END)
    for contact in contacts:
        listbox.insert(tk.END, f"{contact['name']} | {contact['phone']} | {contact['email']}")

cm_app = tk.Tk()
cm_app.title("Contact Manager")
cm_app.geometry("400x300")

tk.Button(cm_app, text="Add Contact", command=add_contact).pack(pady=5)
tk.Button(cm_app, text="Delete Contact", command=delete_contact).pack(pady=5)
listbox = tk.Listbox(cm_app, width=50)
listbox.pack(pady=10)

cm_app.mainloop()
