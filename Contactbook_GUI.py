# username = admin
# password = password
from tkinter import * 
from tkinter import messagebox
import csv

root = Tk()
contacts = []

def save_new_contact():
    contact = {
        "Name": name_entry.get(),
        "Phone": phone_entry.get(),
        "Email": email_entry.get(),
        "Address": address_entry.get()
    }
    contacts.append(contact)
    save_contact()
    display_contact()
    add_window.destroy()

# New window for add contact
def add_contact():
    
    global name_entry, phone_entry, email_entry, address_entry, add_window
    add_window = Toplevel(root)
    add_window.title("Add contact")
    add_window.geometry("500x400")
    contact_f1 = Frame(add_window, border=2, bg="blue", width=500, height=60, relief=RIDGE)
    contact_f1.grid(row=0, columnspan=2)

    Label(add_window, text="Add contact", font="times 28 bold", fg="white", bg="blue").grid(row=0, column=0, columnspan=2, sticky=S)
    
    name_label = Label(add_window, text="Name: ", font="times 15")
    name_label.grid(row=1, column=0, pady=20)
    name_value = StringVar()
    name_entry = Entry(add_window, textvariable=name_value, font="Times 15", justify=RIGHT, relief=GROOVE, border=2)
    name_entry.grid(row=1, column=1, pady=20)

    phone_label = Label(add_window, text="Phone: ", font="times 15")
    phone_label.grid(row=2, column=0, pady=20)
    phone_value = StringVar()
    phone_entry = Entry(add_window, textvariable=phone_value, font="Times 15", justify=RIGHT, relief=GROOVE, border=2)
    phone_entry.grid(row=2, column=1, pady=20)

    email_label = Label(add_window, text="Email: ", font="times 15")
    email_label.grid(row=3, column=0, pady=20)
    email_value = StringVar()
    email_entry = Entry(add_window, textvariable=email_value, font="Times 15", justify=RIGHT, relief=GROOVE, border=2)
    email_entry.grid(row=3, column=1, pady=20)

    address_label = Label(add_window, text="Address: ", font="times 15")
    address_label.grid(row=4, column=0, pady=20)
    address_value = StringVar()
    address_entry = Entry(add_window, textvariable=address_value, font="Times 15", justify=RIGHT, relief=GROOVE, border=2)
    address_entry.grid(row=4, column=1, pady=20)

    Button(add_window, text="SAVE", font="times 15", width=5, border=2, relief=RAISED, bg="blue", fg="white", command=save_new_contact).grid(row=5, column=1)

def save_contact():
    with open('contacts.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Phone", "Email", "Address"])
        writer.writeheader()
        writer.writerows(contacts)

def display_contact():
    global contact_list
    contact_list.delete(0, END)
    for contact in contacts:
        contact_list.insert(END, f"NAME - {contact['Name']} - PHONE - {contact['Phone']} - EMAIL - {contact['Email']} - ADDRESS - {contact['Address']}")

def save_updated_contact():
    global selected_contact,new_window
    selected_contact["Name"] = name_entry.get()
    selected_contact["Phone"] = phone_entry.get()
    selected_contact["Email"] = email_entry.get()
    selected_contact["Address"] = address_entry.get()
    save_contact()
    display_contact()
    new_window.destroy()

def load_contacts():
    global contacts
    try:
        with open('contacts.csv', mode='r') as file:
            reader = csv.DictReader(file)
            contacts = list(reader)
    except FileNotFoundError:
        with open('contacts.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["Name", "Phone", "Email", "Address"])
            writer.writeheader()

def delete_contact():
    selected_contact_index = contact_list.curselection()
    if selected_contact_index:
        del contacts[selected_contact_index[0]]
        save_contact()
        display_contact()
    else:
        messagebox.showwarning("Selection Error", "Please select a contact to delete")

def search_contact():
    global search_entry,contact_list
    search_term = search_entry.get().lower()
    contact_list.delete(0, END)
    for contact in contacts:
        if search_term in contact['Name'].lower() or search_term in contact['Phone']:
            contact_list.insert(END, f"{contact['Name']} - {contact['Phone']}")


def update_contact():
    global name_entry, phone_entry, email_entry, address_entry, new_window, selected_contact
    selected_contact_index = contact_list.curselection()
    if selected_contact_index:
        selected_contact = contacts[selected_contact_index[0]]
        new_window = Toplevel(root)
        new_window.title("Update Contact")
        new_window.geometry("500x400")
        contact_f1 = Frame(new_window, border=2, bg="blue", width=500, height=60, relief=RIDGE)
        contact_f1.grid(row=0, columnspan=2)

        Label(new_window, text="Update contact", font="times 28 bold", fg="white", bg="blue").grid(row=0, column=0, columnspan=2, sticky=S)

        name_label = Label(new_window, text="Name: ", font="times 15")
        name_label.grid(row=1, column=0, pady=20)
        name_value = StringVar()
        name_entry = Entry(new_window, textvariable=name_value, font="Times 15", justify=RIGHT, relief=GROOVE, border=2)
        name_entry.grid(row=1, column=1, pady=20)
        name_entry.insert(0, selected_contact["Name"])

        phone_label = Label(new_window, text="Phone: ", font="times 15")
        phone_label.grid(row=2, column=0, pady=20)
        phone_value = StringVar()
        phone_entry = Entry(new_window, textvariable=phone_value, font="Times 15", justify=RIGHT, relief=GROOVE, border=2)
        phone_entry.grid(row=2, column=1, pady=20)
        phone_entry.insert(0, selected_contact["Phone"])

        email_label = Label(new_window, text="Email: ", font="times 15")
        email_label.grid(row=3, column=0, pady=20)
        email_value = StringVar()
        email_entry = Entry(new_window, textvariable=email_value, font="Times 15", justify=RIGHT, relief=GROOVE, border=2)
        email_entry.grid(row=3, column=1, pady=20)
        email_entry.insert(0, selected_contact["Email"])

        address_label = Label(new_window, text="Address: ", font="times 15")
        address_label.grid(row=4, column=0, pady=20)
        address_value = StringVar()
        address_entry = Entry(new_window, textvariable=address_value, font="Times 15", justify=RIGHT, relief=GROOVE, border=2)
        address_entry.grid(row=4, column=1, pady=20)
        address_entry.insert(0, selected_contact["Address"])

        Button(new_window, text="SAVE", font="times 15", width=5, border=2, relief=RAISED, bg="blue", fg="white", command=save_updated_contact).grid(row=5, column=1)
    else:
        messagebox.showwarning("Selection Error", "Please select a contact to update")

def open_contact_window():
    global contact_list,search_entry
    frame1.destroy()
    frame2.destroy()
    

    f1 = Frame(root, border=10, bg="blue", width=700, height=90)
    f1.grid(row=0)


    Label(root, text="Contact book", font="Times 50", bg="blue", fg="white").grid(row=0, sticky=S)
    f2 = Frame(root, width=700, height=150, borderwidth=0, relief=RIDGE, bg="white")
    f2.grid(row=1, padx=0, pady=10)

    add_b = Button(f2, text="ADD", relief=RAISED, borderwidth=4, background="blue", fg="white", width=10, font="times 12 bold", command=add_contact)
    add_b.grid(row=1, column=0, padx=50, pady=30)
    up_b = Button(f2, text="UPDATE", relief=RAISED, border=4, background="blue", fg="white", width=10, command=update_contact, font="times 12 bold")
    up_b.grid(row=1, column=1, padx=50, pady=30)
    del_b = Button(f2, text="DELETE", relief=RAISED, border=4, background="blue", fg="white", width=10, command=delete_contact, font="times 12 bold")
    del_b.grid(row=1, column=2, padx=50, pady=30)
    # Search frame
    f3 = Frame(root, width=700, height=150, borderwidth=0, relief=RIDGE, bg="white")
    f3.grid(row=2, padx=0, pady=20, columnspan=3)
    Label(f3, text="Search Contact:", font="Times 15", background="white").grid(row=2, column=0, padx=30)
    search_value = StringVar()
    search_entry = Entry(f3, textvariable=search_value, font="Times 18", fg="black", justify=RIGHT, relief=GROOVE, border=2)
    search_entry.grid(row=2, column=2, padx=30)

    search_b = Button(f3, text="SEARCH", relief=RAISED, border=4, background="blue", fg="white", width=10, font="times 12 bold", command=search_contact)
    search_b.grid(row=2, column=3, padx=30)

    contact_list = Listbox(root, borderwidth=5, width=100, relief=GROOVE)
    contact_list.grid(row=3, pady=20)
    load_contacts()
    display_contact()
     

def login():
    username = userentry.get()
    password = passentry.get()

    # Basic login validation (replace with your own logic)
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Success", "Welcome!")
        open_contact_window()   # Open contact window in the same window
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# Setting up the login window
frame1 = Frame(root, bg="#55d0ff", borderwidth=20, relief=FLAT, height=500, width=260)
frame1.grid(column=0, rowspan=10)
frame1.grid_propagate(False)

frame2 = Frame(root, borderwidth=20, relief=FLAT, height=500, width=440, background="white")
frame2.grid(column=1, row=1)
Label(frame2, text="Welcome to the contact list", font="arial 10 underline", background="white").grid(padx=20, column=1, row=1, sticky=W)
Label(frame2, text="Login to your account", font="arial 20 bold", background="white").grid(padx=20, pady=20, column=1, row=2, sticky=W)
Label(frame2, text="Username", font="arial 15", background="white").grid(padx=20, pady=10, column=1, row=5, sticky=W)

# Username
uservalue = StringVar()
userentry = Entry(frame2, textvariable=uservalue, font="Times 15", justify=RIGHT, border=2, relief=GROOVE, width=30)
userentry.grid(row=6, column=1, sticky=W, padx=20)

# Password
Label(frame2, text="Password", font="arial 15", background="white").grid(padx=20, pady=10, column=1, row=7, sticky=W)
passvalue = StringVar()
passentry = Entry(frame2, textvariable=passvalue, font="Times 15", justify=RIGHT, show="*", border=2, relief=GROOVE, width=30)
passentry.grid(row=8, column=1, sticky=W, padx=20)

# Load and display the image in f1
image = PhotoImage(file="pngegg5.png")
image_label = Label(frame1, image=image, height=50, width=50, background="#55d0ff")
image_label.grid(row=0, column=0, sticky="nsew")

login_button = Button(frame2, text="Login", font="Times 11", bg="#55d0ff", bd=2, relief=RIDGE, width=37, command=login)
login_button.grid(column=1, row=9, pady=30, sticky=W, padx=20)

# Center the image in the frame
frame1.grid_rowconfigure(0, weight=1)
frame1.grid_columnconfigure(0, weight=1)


root.title("Login_window")
root.geometry("700x500")
root.wm_iconbitmap("loggin.ico")
root.configure(background="white")
root.mainloop()
