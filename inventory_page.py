from tkinter import *
from PIL import ImageTk, Image
import os

class Main:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")

        self.load_background()

        login_frame = Frame(self.root, bd=2, relief=RIDGE, bg="beige")
        login_frame.place(x=430, y=140, width=550, height=340)

        title = Label(text="Logistic Management System", font=("Noto Sans", 25, "bold")).place(x=0, y=30,relwidth=1)

        self.create_button(login_frame, "VIEW INVENTORY", self.Login, 45, 50)
        self.create_button(login_frame, "Menu", self.menu, 255, 50)
        self.create_button(login_frame, "Update", self.update, 175, 250)
        self.create_button(login_frame, "ADD INVENTORY", self.job_registration, 45, 180)
        self.create_button(login_frame, "DELETE INVENTORY", self.availble_jobs, 255, 180)

        self.root.bind("<Configure>", self.resize_bg)

    def load_background(self):
        self.bg_image = Image.open("105.png")
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.lbl_bg = Label(self.root, image=self.bg_photo)
        self.lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

    def resize_bg(self, event):
        width = event.width
        height = event.height

        # Resize the background image
        resized_image = self.bg_image.resize((width, height), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(resized_image)
        self.lbl_bg.config(image=self.bg_photo)

    def create_button(self, frame, text, command, x, y):
        btn = Button(frame, text=text, command=command, font=("Elephant", 13),
                     bg="#00a8e8", activebackground="#005ea6", fg="black", activeforeground="white",
                     cursor="hand2")
        btn.place(x=x, y=y, width=200, height=45)

    def job_registration(self):
        os.system('python add_inventory.py')

    def availble_jobs(self):
        os.system('python delete_inventory.py')

    def Login(self):
        os.system('python view_inventory.py')

    def menu(self):
        self.root.destroy()
        os.system('python Mainpage.py')

    def update(self):
        os.system('python update_inventory.py')

root = Tk()
obj = Main(root)
root.mainloop()
