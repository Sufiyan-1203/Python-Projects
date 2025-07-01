import tkinter as tk
from tkinter import messagebox
import sqlite3

# Database setup
con = sqlite3.connect("contacts.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT)")
con.commit()

root = tk.Tk()
root.title("Contact Book")
root.geometry("500x400")
root.config(bg="#1e1e1e")

def refresh_contacts():
    contact_list.delete(0, tk.END)
    cur.execute("SELECT * FROM contacts")
    for row in cur.fetchall():
        contact_list.insert(tk.END, f"{row[0]}. {row[1]} | {row[2]} | {row[3]}")

def add_contact():
    n, p, e = name.get(), phone.get(), email.get()
    if not n or not p or not e:
        messagebox.showwarning("Error", "Fill all fields")
        return
    cur.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (n, p, e))
    con.commit()
    refresh_contacts()
    name.delete(0, tk.END)
    phone.delete(0, tk.END)
    email.delete(0, tk.END)

def delete_contact():
    sel = contact_list.curselection()
    if not sel:
        messagebox.showwarning("Error", "Select a contact")
        return
    contact_id = contact_list.get(sel[0]).split(".")[0]
    cur.execute("DELETE FROM contacts WHERE id=?", (contact_id,))
    con.commit()
    refresh_contacts()

def select_contact():
    sel = contact_list.curselection()
    if not sel:
        return
    contact_id = contact_list.get(sel[0]).split(".")[0]
    cur.execute("SELECT * FROM contacts WHERE id=?", (contact_id,))
    row = cur.fetchone()
    name.delete(0, tk.END)
    phone.delete(0, tk.END)
    email.delete(0, tk.END)
    name.insert(0, row[1])
    phone.insert(0, row[2])
    email.insert(0, row[3])

def update_contact():
    sel = contact_list.curselection()
    if not sel:
        messagebox.showwarning("Error", "Select a contact")
        return
    contact_id = contact_list.get(sel[0]).split(".")[0]
    n, p, e = name.get(), phone.get(), email.get()
    if not n or not p or not e:
        messagebox.showwarning("Error", "Fill all fields")
        return
    cur.execute("UPDATE contacts SET name=?, phone=?, email=? WHERE id=?", (n, p, e, contact_id))
    con.commit()
    refresh_contacts()
    name.delete(0, tk.END)
    phone.delete(0, tk.END)
    email.delete(0, tk.END)

tk.Label(root, text="Name", bg="#1e1e1e", fg="white").place(x=20, y=20)
tk.Label(root, text="Phone", bg="#1e1e1e", fg="white").place(x=20, y=60)
tk.Label(root, text="Email", bg="#1e1e1e", fg="white").place(x=20, y=100)

name = tk.Entry(root, width=30)
name.place(x=100, y=20)
phone = tk.Entry(root, width=30)
phone.place(x=100, y=60)
email = tk.Entry(root, width=30)
email.place(x=100, y=100)

tk.Button(root, text="Add", command=add_contact, bg="green", fg="white", width=10).place(x=360, y=20)
tk.Button(root, text="Update", command=update_contact, bg="blue", fg="white", width=10).place(x=360, y=60)
tk.Button(root, text="Delete", command=delete_contact, bg="red", fg="white", width=10).place(x=360, y=100)

contact_list = tk.Listbox(root, height=12, width=70)
contact_list.place(x=20, y=150)
contact_list.bind("<<ListboxSelect>>", lambda e: select_contact())

refresh_contacts()
root.mainloop()
