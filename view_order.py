import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="Mayank@1312", database="lms")
cur = con.cursor()

def search_order_by_id():
    order_id = search_entry.get()
    if not order_id:
        messagebox.showinfo("Input Error", "Please enter an Order ID")
        return

    try:
        cur.execute("SELECT * FROM orders WHERE order_id = %s", (order_id,))
        rows = cur.fetchall()
        con.commit()
        if not rows:
            messagebox.showinfo("No Results", "No order found with this Order ID")
            return
        # Clear the treeview
        for row in tree.get_children():
            tree.delete(row)
        # Insert search results
        for row in rows:
            tree.insert("", tk.END, values=row)
    except:
        messagebox.showinfo("Error", "Failed to fetch the order from the database")

def refresh_treeview():
    try:
        cur.execute("SELECT * FROM orders")
        rows = cur.fetchall()
        con.commit()
        # Clear the treeview
        for row in tree.get_children():
            tree.delete(row)
        # Insert all orders
        for row in rows:
            tree.insert("", tk.END, values=row)
    except:
        messagebox.showinfo("Error", "Failed to fetch orders from the database")

def view_all_orders():
    global tree, search_entry
    root = tk.Tk()
    root.title("View All Orders")
    root.minsize(width=400, height=400)
    root.geometry("1000x400")

    # Frame for search bar and buttons
    search_frame = tk.Frame(root)
    search_frame.pack(pady=10)

    tk.Label(search_frame, text="Search by Order ID:").grid(row=0, column=0, padx=5)
    search_entry = tk.Entry(search_frame)
    search_entry.grid(row=0, column=1, padx=5)
    search_btn = tk.Button(search_frame, text="Search", command=search_order_by_id)
    search_btn.grid(row=0, column=2, padx=5)
    refresh_btn = tk.Button(search_frame, text="Refresh", command=refresh_treeview)
    refresh_btn.grid(row=0, column=3, padx=5)

    tree = ttk.Treeview(root, column=("c1", "c2", "c3", "c4", "c5", "c6"), show='headings')
    tree.column("#1", anchor=tk.CENTER)
    tree.heading("#1", text="Order id")
    tree.column("#2", anchor=tk.CENTER)
    tree.heading("#2", text="Date")
    tree.column("#3", anchor=tk.CENTER)
    tree.heading("#3", text="Sender Address")
    tree.column("#4", anchor=tk.CENTER)
    tree.heading("#4", text="Receiver Address")
    tree.column("#5", anchor=tk.CENTER)
    tree.heading("#5", text="Description")
    tree.column("#6", anchor=tk.CENTER)
    tree.heading("#6", text="Tracking No")
    tree.pack(expand=True, fill=tk.BOTH)

    # Initial load of all orders
    refresh_treeview()

    quit_btn = tk.Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quit_btn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

if __name__ == "__main__":
    view_all_orders()
