import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="Mayank@1312", database="lms")
cur = con.cursor()

def search_product_by_id():
    product_id = search_id_entry.get()
    if not product_id:
        messagebox.showinfo("Input Error", "Please enter a Product ID")
        return

    try:
        cur.execute("SELECT * FROM products WHERE product_id = %s", (product_id,))
        rows = cur.fetchall()
        con.commit()
        if not rows:
            messagebox.showinfo("No Results", "No product found with this Product ID")
            return
        # Clear the treeview
        for row in tree.get_children():
            tree.delete(row)
        # Insert search results
        for row in rows:
            tree.insert("", tk.END, values=row + ('Update Incoming', 'Update Outgoing'))
    except:
        messagebox.showinfo("Error", "Failed to fetch the product from the database")

def refresh_treeview():
    try:
        cur.execute("SELECT * FROM products")
        rows = cur.fetchall()
        con.commit()
        # Clear the treeview
        for row in tree.get_children():
            tree.delete(row)
        # Insert all products
        for row in rows:
            tree.insert("", tk.END, values=row + ('Update Incoming', 'Update Outgoing'))
    except:
        messagebox.showinfo("Error", "Failed to fetch products from the database")

def update_stock(stock_type, product_id, stock_level, incoming_stock, outgoing_stock):
    if stock_type == "incoming":
        stock_level += incoming_stock
        incoming_stock = 0
    elif stock_type == "outgoing":
        stock_level -= outgoing_stock
        outgoing_stock = 0

    try:
        cur.execute("UPDATE products SET stock_level = %s, incoming_stock = %s, outgoing_stock = %s WHERE product_id = %s",
                    (stock_level, incoming_stock, outgoing_stock, product_id))
        con.commit()
        refresh_treeview()
        messagebox.showinfo("Success", "Stock level updated successfully")
    except:
        messagebox.showinfo("Error", "Failed to update the stock level")

def on_treeview_click(event):
    item = tree.identify_row(event.y)
    column = tree.identify_column(event.x)
    if not item:
        return

    if column == '#7':  # Update Incoming
        values = tree.item(item, "values")
        product_id = values[0]
        stock_level = int(values[2])
        incoming_stock = int(values[3])
        outgoing_stock = int(values[4])
        update_stock("incoming", product_id, stock_level, incoming_stock, outgoing_stock)
    elif column == '#8':  # Update Outgoing
        values = tree.item(item, "values")
        product_id = values[0]
        stock_level = int(values[2])
        incoming_stock = int(values[3])
        outgoing_stock = int(values[4])
        update_stock("outgoing", product_id, stock_level, incoming_stock, outgoing_stock)

def search_product_by_name():
    product_name = search_name_entry.get()
    if not product_name:
        messagebox.showinfo("Input Error", "Please enter a Product Name")
        return

    try:
        cur.execute("SELECT * FROM products WHERE name LIKE %s", ('%' + product_name + '%',))
        rows = cur.fetchall()
        con.commit()
        if not rows:
            messagebox.showinfo("No Results", "No product found with this name")
            return
        # Clear the treeview
        for row in tree.get_children():
            tree.delete(row)
        # Insert search results
        for row in rows:
            tree.insert("", tk.END, values=row + ('Update Incoming', 'Update Outgoing'))
    except Exception as e:
        messagebox.showinfo("Error", f"Failed to fetch the product from the database: {str(e)}")

def view_all_songs():
    global tree, search_id_entry, search_name_entry
    root = tk.Tk()
    root.title("View All Inventory")
    root.minsize(width=400, height=400)
    root.geometry("1200x500")

    # Frame for search bar and buttons
    search_frame = tk.Frame(root)
    search_frame.pack(pady=10)

    tk.Label(search_frame, text="Search by Product ID:").grid(row=0, column=0, padx=5)
    search_id_entry = tk.Entry(search_frame)
    search_id_entry.grid(row=0, column=1, padx=5)
    search_id_btn = tk.Button(search_frame, text="Search", command=search_product_by_id)
    search_id_btn.grid(row=0, column=2, padx=5)

    tk.Label(search_frame, text="Search by Product Name:").grid(row=1, column=0, padx=5)
    search_name_entry = tk.Entry(search_frame)
    search_name_entry.grid(row=1, column=1, padx=5)
    search_name_btn = tk.Button(search_frame, text="Search", command=search_product_by_name)
    search_name_btn.grid(row=1, column=2, padx=5)

    refresh_btn = tk.Button(search_frame, text="Refresh", command=refresh_treeview)
    refresh_btn.grid(row=2, column=1, pady=10)

    tree = ttk.Treeview(root, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8"), show='headings')
    tree.column("#1", anchor=tk.CENTER)
    tree.heading("#1", text="Product id")
    tree.column("#2", anchor=tk.CENTER)
    tree.heading("#2", text="Product Name")
    tree.column("#3", anchor=tk.CENTER)
    tree.heading("#3", text="Stock Level")
    tree.column("#4", anchor=tk.CENTER)
    tree.heading("#4", text="Incoming Stock")
    tree.column("#5", anchor=tk.CENTER)
    tree.heading("#5", text="Outgoing Stock")
    tree.column("#6", anchor=tk.CENTER)
    tree.heading("#6", text="Cost")
    tree.column("#7", anchor=tk.CENTER)
    tree.heading("#7", text="Incoming")
    tree.column("#8", anchor=tk.CENTER)
    tree.heading("#8", text="Outgoing")
    tree.pack(expand=True, fill=tk.BOTH)

    # Bind the click event
    tree.bind("<Button-1>", on_treeview_click)

    # Initial load of all products
    refresh_treeview()

    quit_btn = tk.Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quit_btn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

if __name__ == "__main__":
    view_all_songs()
