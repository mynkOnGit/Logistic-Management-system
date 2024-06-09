import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random
import re
import mysql.connector

def generate_random_id():
    return str(random.randint(10000, 99999))

def validate_fields():
    order_id = songInfo1.get()
    order_date = songInfo2.get()
    sender_address = songInfo3.get()
    receiver_address = songInfo4.get()
    description = songInfo5.get()
    tracking_number = songInfo6.get()

    if order_id == "" or order_date == "" or sender_address == "" or receiver_address == "" or description == "" or tracking_number == "":
        messagebox.showerror("Error", "Please fill in all the fields.")
        return False

    return True

def validate_tracking_number(event):
    if not songInfo6.get().isdigit():
        songInfo6.delete(0, END)
        messagebox.showerror("Error", "Tracking ID must be a number.")

def validate_date(event):
    date_pattern = r"(\d{0,4}-\d{0,2}-\d{0,2})?"  # Regular expression pattern for optional YYYY-MM-DD format

    if not re.match(date_pattern, songInfo2.get()):
        songInfo2.delete(0, END)
        messagebox.showerror("Error", "Invalid date format. Please enter a date in YYYY-MM-DD format.")

def orderadd():
    if not validate_fields():
        return

    order_id = songInfo1.get()
    order_date = songInfo2.get()
    sender_address = songInfo3.get()
    receiver_address = songInfo4.get()
    description = songInfo5.get()
    tracking_number = songInfo6.get()

    query = "INSERT INTO orders (order_id, order_date, sender_address, receiver_address, description, tracking_number) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (order_id, order_date, sender_address, receiver_address, description, tracking_number)

    try:
        cur.execute(query, values)
        con.commit()
        messagebox.showinfo("Success", "Order added successfully.")
        root.destroy()
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error adding Order: {e}")

def addorder():
    global songInfo1, songInfo2, songInfo3, songInfo4, songInfo5, songInfo6, con, cur, root

    root = tk.Tk()
    root.title("Add New Order")
    root.minsize(width=400, height=400)
    root.geometry("800x600")

    con = mysql.connector.connect(host="localhost", user="root", password="Mayank@1312", database="lms")
    cur = con.cursor()

    headingFrame1 = tk.Frame(root, bg="#2f2e2e", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = tk.Label(headingFrame1, text="Add New Order", font='Helvetica 14 bold', bg="#00a8e8", fg='black')
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = tk.Frame(root, bg="#00a8e8")
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    lb1 = tk.Label(labelFrame, text="Order ID:", font='Helvetica 13 bold', bg="#00a8e8", fg='black')
    lb1.place(relx=0.05, rely=0.10, relheight=0.08)

    songInfo1 = tk.Entry(labelFrame)
    songInfo1.place(relx=0.3, rely=0.10, relwidth=0.62, relheight=0.08)
    songInfo1.insert(0, generate_random_id())
    songInfo1.config(state='readonly')  # Make the order ID field read-only

    lb2 = Label(labelFrame, text="Date:", font='Helvetica 13 bold', bg="#00a8e8", fg='black')
    lb2.place(relx=0.05, rely=0.26, relheight=0.08)

    songInfo2 = Entry(labelFrame)
    songInfo2.place(relx=0.3, rely=0.26, relwidth=0.62, relheight=0.08)
    songInfo2.bind("<KeyRelease>", validate_date)

    lb3 = Label(labelFrame, text="Sender Address:", font='Helvetica 13 bold', bg="#00a8e8", fg='black')
    lb3.place(relx=0.05, rely=0.42, relheight=0.08)

    songInfo3 = Entry(labelFrame)
    songInfo3.place(relx=0.3, rely=0.42, relwidth=0.62, relheight=0.08)

    lb4 = Label(labelFrame, text="Receiver Address:", font='Helvetica 13 bold', bg="#00a8e8", fg='black')
    lb4.place(relx=0.05, rely=0.58, relheight=0.08)

    songInfo4 = Entry(labelFrame)
    songInfo4.place(relx=0.3, rely=0.58, relwidth=0.62, relheight=0.08)

    lb5 = Label(labelFrame, text="Description:", font='Helvetica 13 bold', bg="#00a8e8", fg='black')
    lb5.place(relx=0.05, rely=0.74, relheight=0.08)

    songInfo5 = Entry(labelFrame)
    songInfo5.place(relx=0.3, rely=0.74, relwidth=0.62, relheight=0.08)

    lb6 = Label(labelFrame, text="Tracking No:", font='Helvetica 13 bold', bg="#00a8e8", fg='black')
    lb6.place(relx=0.05, rely=0.90, relheight=0.08)

    songInfo6 = Entry(labelFrame)
    songInfo6.place(relx=0.3, rely=0.90, relwidth=0.62, relheight=0.08)
    songInfo6.insert(0, generate_random_id())
    songInfo6.config(state='readonly')  # Make the tracking number field read-only

    SubmitBtn = Button(root, text="Submit", font='Helvetica 12 bold', bg='#00a8e8', fg='black', command=orderadd)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", font='Helvetica 12 bold', bg='#00a8e8', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

addorder()
