import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import random

def invenadd():
    product_id = songInfo1.get()
    name = songInfo2.get()
    stock_level = songInfo3.get()
    incoming_stock = songInfo4.get()
    outgoing_stock = songInfo5.get()
    cost = songInfo6.get()

    if name == "" or stock_level == "" or incoming_stock == "" or outgoing_stock == "" or cost == "":
        messagebox.showerror("Error", "Please fill in all the fields.")
        return

    query = "INSERT INTO products (product_id, name, stock_level, incoming_stock, outgoing_stock, cost) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (product_id, name, stock_level, incoming_stock, outgoing_stock, cost)

    try:
        cur.execute(query, values)
        con.commit()
        messagebox.showinfo("Success", "Inventory added successfully.")
        root.destroy()
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error adding Order: {e}")

def validate_stock(event):
    if not songInfo3.get().isdigit():
        songInfo3.delete(0, END)
        messagebox.showerror("Error", "Stock Level must be a number.")

def validate_incoming_stock(event):
    if not songInfo4.get().isdigit():
        songInfo4.delete(0, END)
        messagebox.showerror("Error", "Value must be a number.")

def validate_outgoing_stock(event):
    if not songInfo5.get().isdigit():
        songInfo5.delete(0, END)
        messagebox.showerror("Error", "Value must be a number.")

def validate_cost(event):
    if not songInfo6.get().isdigit():
        songInfo6.delete(0, END)
        messagebox.showerror("Error", "Cost must be a number.")

def generate_product_id():
    return str(random.randint(10000, 99999))

def addinven():
    global img, songInfo1, songInfo2, songInfo3, songInfo4, songInfo5, songInfo6, con, cur, root

    root = tk.Tk()
    root.title("Add New Inventory")
    root.minsize(width=400, height=400)
    root.geometry("800x600")

    con = mysql.connector.connect(host="localhost", user="root", password="Mayank@1312", database="lms")
    cur = con.cursor()

    headingFrame1 = tk.Frame(root, bg="#2f2e2e", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = tk.Label(headingFrame1, text="Add New Inventory", font='Helvetica 14 bold', bg="#00a8e8", fg='black')
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = tk.Frame(root, bg="#00a8e8")
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    lb1 = tk.Label(labelFrame, text="Product id:", font='Helvetica 13 bold', bg="#00a8e8", fg='black')
    lb1.place(relx=0.05, rely=0.10, relheight=0.08)

    songInfo1 = tk.Entry(labelFrame)
    songInfo1.place(relx=0.3, rely=0.10, relwidth=0.62, relheight=0.08)
    songInfo1.insert(0, generate_product_id())
    songInfo1.config(state='readonly')

    lb2 = Label(labelFrame, text="Product Name:", font='Helvetica 13 bold', bg="#00a8e8", fg='black')
    lb2.place(relx=0.05, rely=0.26, relheight=0.08)

    songInfo2 = Entry(labelFrame)
    songInfo2.place(relx=0.3, rely=0.26, relwidth=0.62, relheight=0.08)

    lb3 = Label(labelFrame, text="Stock Level:", font='Helvetica 13 bold', bg="#00a8e8", fg='black')
    lb3.place(relx=0.05, rely=0.42, relheight=0.08)

    songInfo3 = Entry(labelFrame)
    songInfo3.place(relx=0.3, rely=0.42, relwidth=0.62, relheight=0.08)
    songInfo3.bind("<KeyRelease>", validate_stock)

    lb4 = Label(labelFrame, text="Incoming Stock:", font='Helvetica 13 bold', bg="#00a8e8", fg='black')
    lb4.place(relx=0.05, rely=0.58, relheight=0.08)

    songInfo4 = Entry(labelFrame)
    songInfo4.place(relx=0.3, rely=0.58, relwidth=0.62, relheight=0.08)
    songInfo4.bind("<KeyRelease>", validate_incoming_stock)

    lb5 = Label(labelFrame, text="Outgoing Stock:", font='Helvetica 13 bold', bg="#00a8e8", fg='black')
    lb5.place(relx=0.05, rely=0.74, relheight=0.08)

    songInfo5 = Entry(labelFrame)
    songInfo5.place(relx=0.3, rely=0.74, relwidth=0.62, relheight=0.08)
    songInfo5.bind("<KeyRelease>", validate_outgoing_stock)

    lb5 = Label(labelFrame, text="Cost:", font='Helvetica 13 bold', bg="#00a8e8", fg='black')
    lb5.place(relx=0.05, rely=0.90, relheight=0.08)

    songInfo6 = Entry(labelFrame)
    songInfo6.place(relx=0.3, rely=0.90, relwidth=0.62, relheight=0.08)
    songInfo6.bind("<KeyRelease>", validate_cost)

    SubmitBtn = Button(root, text="Submit", font='Helvetica 12 bold', bg='#00a8e8', fg='black', command=invenadd)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", font='Helvetica 12 bold', bg='#00a8e8', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

addinven()
