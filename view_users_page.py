import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

class ViewUsers:
    def __init__(self, root):
        self.root = root
        self.root.title("View Users")
        self.root.geometry("800x600")

        self.create_widgets()
        self.load_users()

    def create_widgets(self):
        self.tree = ttk.Treeview(self.root, columns=("Email", "Username", "Password"), show="headings")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Username", text="Username")
        self.tree.heading("Password", text="Password")
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.edit_button = tk.Button(self.root, text="Edit", command=self.edit_user)
        self.edit_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.delete_button = tk.Button(self.root, text="Delete", command=self.delete_user)
        self.delete_button.pack(side=tk.LEFT, padx=10, pady=10)

    def load_users(self):
        con = mysql.connector.connect(host="localhost", user="root", password="Mayank@1312", database="lms")
        cur = con.cursor()
        cur.execute("SELECT email_id, username, password FROM login")
        rows = cur.fetchall()
        for row in rows:
            self.tree.insert("", tk.END, values=row)
        con.close()

    def edit_user(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "No user selected")
            return

        item = self.tree.item(selected_item)
        email, username, password = item["values"]

        self.edit_window = tk.Toplevel(self.root)
        self.edit_window.title("Edit User")
        self.edit_window.geometry("400x300")

        tk.Label(self.edit_window, text="Email").pack(pady=5)
        self.email_entry = tk.Entry(self.edit_window)
        self.email_entry.pack(pady=5)
        self.email_entry.insert(0, email)

        tk.Label(self.edit_window, text="Username").pack(pady=5)
        self.username_entry = tk.Entry(self.edit_window)
        self.username_entry.pack(pady=5)
        self.username_entry.insert(0, username)

        tk.Label(self.edit_window, text="Password").pack(pady=5)
        self.password_entry = tk.Entry(self.edit_window, show="*")
        self.password_entry.pack(pady=5)
        self.password_entry.insert(0, password)

        tk.Button(self.edit_window, text="Save", command=lambda: self.save_user(email)).pack(pady=20)

    def save_user(self, old_email):
        new_email = self.email_entry.get()
        new_username = self.username_entry.get()
        new_password = self.password_entry.get()

        con = mysql.connector.connect(host="localhost", user="root", password="Mayank@1312", database="lms")
        cur = con.cursor()
        query = "UPDATE login SET email_id=%s, username=%s, password=%s WHERE email_id=%s"
        cur.execute(query, (new_email, new_username, new_password, old_email))
        con.commit()
        con.close()

        self.tree.delete(*self.tree.get_children())
        self.load_users()
        self.edit_window.destroy()
        messagebox.showinfo("Success", "User updated successfully")

    def delete_user(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "No user selected")
            return

        item = self.tree.item(selected_item)
        email = item["values"][0]

        con = mysql.connector.connect(host="localhost", user="root", password="Mayank@1312", database="lms")
        cur = con.cursor()
        query = "DELETE FROM login WHERE email_id=%s"
        cur.execute(query, (email,))
        con.commit()
        con.close()

        self.tree.delete(selected_item)
        messagebox.showinfo("Success", "User deleted successfully")

if __name__ == "__main__":
    root = tk.Tk()
    app = ViewUsers(root)
    root.mainloop()
