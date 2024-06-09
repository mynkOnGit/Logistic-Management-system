import os
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

# Insert function
def insert():
    shipment_id = e_id.get()
    order_id = e_name.get()
    tracking_number = e_phone.get()
    current_location = e_bill.get()
    date = e_date.get()

    if shipment_id == "" or order_id == "" or tracking_number == "" or current_location == "":
        MessageBox.showinfo("Insert Status", "All Fields are Required!")
    else:
        con = mysql.connect(host="localhost", user="root", password="Mayank@1312", database="lms")
        cursor = con.cursor()
        query = "INSERT INTO shipments (shipment_id, order_id, tracking_number, current_location, date) VALUES (%s, %s, %s, %s, %s)"
        values = (shipment_id, order_id, tracking_number, current_location, date)
        cursor.execute(query, values)
        con.commit()
        clear_fields()
        show()
        MessageBox.showinfo("Insert Status", "Inserted Successfully!")
        con.close()

def clear_fields():
    e_id.delete(0, 'end')
    e_name.delete(0, 'end')
    e_phone.delete(0, 'end')
    e_bill.delete(0, 'end')
    e_date.delete(0, 'end')

def mainpage():
    os.system('python Mainpage.py')

# Delete function
def delete():
    if e_id.get() == "":
        MessageBox.showinfo("Delete Status", "You need to specify ID!")
    else:
        con = mysql.connect(host="localhost", user="root", password="Mayank@1312", database="lms")
        cursor = con.cursor()
        cursor.execute("DELETE FROM shipments WHERE shipment_id = %s", (e_id.get(),))
        cursor.execute("commit")
        clear_fields()
        show()
        MessageBox.showinfo("Delete Status", "Deleted Successfully!")
        con.close()

# Update function
def update():
    shipment_id = e_id.get()
    order_id = e_name.get()
    tracking_number = e_phone.get()
    current_location = e_bill.get()
    date = e_date.get()

    if shipment_id == "" or order_id == "" or tracking_number == "" or current_location == "":
        MessageBox.showinfo("Update Status", "All Fields are Required!")
    else:
        con = mysql.connect(host="localhost", user="root", password="Mayank@1312", database="lms")
        cursor = con.cursor()
        cursor.execute(
            "UPDATE shipments SET order_id = %s, tracking_number = %s, current_location = %s, date = %s WHERE shipment_id = %s",
            (order_id, tracking_number, current_location, date, shipment_id))
        cursor.execute("commit")
        clear_fields()
        show()
        MessageBox.showinfo("Update Status", "Updated Successfully!")
        con.close()

# Get function
def get():
    shipment_id = e_id.get()
    if e_id.get() == "":
        MessageBox.showinfo("Fetch Status", "You need to specify ID!")
    else:
        con = mysql.connect(host="localhost", user="root", password="Mayank@1312", database="lms")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM shipments WHERE shipment_id = %s", (e_id.get(),))

        rows = cursor.fetchall()

        for row in rows:
            e_name.insert(0, row[1])
            e_phone.insert(0, row[2])
            e_bill.insert(0, row[3])
            e_date.insert(0, row[4])

        con.close()

def show():
    con = mysql.connect(host="localhost", user="root", password="Mayank@1312", database="lms")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM shipments")
    rows = cursor.fetchall()

    # Clear the existing data in the treeview
    for row in tree.get_children():
        tree.delete(row)

    # Insert data into the treeview
    for row in rows:
        tree.insert("", END, values=row)

    con.close()

root = Tk()
root.geometry('800x600')
root.title('Logistic Management System')

header = Label(root, text="Manage Tracking", font=("Helvetica", 20, "bold"), bg="#00a8e8", fg="white")
header.pack(fill=X)

frame = Frame(root)
frame.pack(pady=20)

Label(frame, text='Enter Shipment ID', font=('bold', 14)).grid(row=0, column=0, pady=5, sticky=E)
Label(frame, text='Enter Order ID', font=('bold', 14)).grid(row=1, column=0, pady=5, sticky=E)
Label(frame, text='Enter Tracking No', font=('bold', 14)).grid(row=2, column=0, pady=5, sticky=E)
Label(frame, text='Enter Location', font=('bold', 14)).grid(row=3, column=0, pady=5, sticky=E)
Label(frame, text='Enter Date', font=('bold', 14)).grid(row=4, column=0, pady=5, sticky=E)

e_id = Entry(frame)
e_id.grid(row=0, column=1, padx=10)
e_name = Entry(frame)
e_name.grid(row=1, column=1, padx=10)
e_phone = Entry(frame)
e_phone.grid(row=2, column=1, padx=10)
e_bill = Entry(frame)
e_bill.grid(row=3, column=1, padx=10)
e_date = Entry(frame)
e_date.grid(row=4, column=1, padx=10)

button_frame = Frame(root)
button_frame.pack(pady=20)

Button(button_frame, text="Insert", font=("italic", 12), bg="#00a8e8", fg="white", command=insert).grid(row=0, column=0, padx=5)
Button(button_frame, text="Delete", font=("italic", 12), bg="#00a8e8", fg="white", command=delete).grid(row=0, column=1, padx=5)
Button(button_frame, text="Update", font=("italic", 12), bg="#00a8e8", fg="white", command=update).grid(row=0, column=2, padx=5)
Button(button_frame, text="Get", font=("italic", 12), bg="#00a8e8", fg="white", command=get).grid(row=0, column=3, padx=5)
Button(button_frame, text="Clear", font=("italic", 12), bg="#00a8e8", fg="white", command=clear_fields).grid(row=0, column=4, padx=5)
Button(button_frame, text="Menu", font=("italic", 12), bg="#00a8e8", fg="white", command=mainpage).grid(row=0, column=5, padx=5)

# Create a Treeview widget
columns = ("Shipment ID", "Order ID", "Tracking No", "Location", "Date")
tree = ttk.Treeview(root, columns=columns, show="headings")

# Define headings
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

tree.pack(pady=20, fill=BOTH, expand=True)

show()
mainloop()
