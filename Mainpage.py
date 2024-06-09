import os
from tkinter import *
from PIL import Image, ImageTk

class Main:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Page")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")

        self.load_background()

        login_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        login_frame.place(x=430, y=140, width=550, height=340)

        title = Label(text="Logistic Management System", font=("Noto Sans", 25, "bold"))
        title.place(x=0, y=30, relwidth=1)

        self.create_button(login_frame, "Tracking", self.tracking, 45, 50)
        self.create_button(login_frame, "Report", self.report, 255, 50)
        self.create_button(login_frame, "Order Management", self.job_registration, 45, 180)
        self.create_button(login_frame, "Inventory", self.availble_jobs, 255, 180)

        self.root.bind("<Configure>", self.resize_bg)

    def load_background(self):
        # Load a higher resolution image
        self.bg_image = Image.open("105.png")
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.lbl_bg = Label(self.root, image=self.bg_photo)
        self.lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

    def resize_bg(self, event):
        width = event.width
        height = event.height

        # Calculate the aspect ratio of the image
        aspect_ratio = self.bg_image.width / self.bg_image.height

        # Calculate the new width and height while maintaining the aspect ratio
        new_width = width
        new_height = int(new_width / aspect_ratio)

        # If the new height is greater than the window height, adjust the width and height accordingly
        if new_height > height:
            new_height = height
            new_width = int(new_height * aspect_ratio)

        # Resize the image
        self.bg_image_resized = self.bg_image.resize((new_width, new_height), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image_resized)

        # Update the label with the resized image
        self.lbl_bg.config(image=self.bg_photo)

    def create_button(self, frame, text, command, x, y):
        btn = Button(frame, text=text, command=command, font=("Elephant", 13),
                     bg="#00a8e8", activebackground="#005ea6", fg="black", activeforeground="white",
                     cursor="hand2")
        btn.place(x=x, y=y, width=200, height=45)

    def job_registration(self):
        self.root.destroy()
        import order_page

    def availble_jobs(self):
        self.root.destroy()
        import inventory_page

    def tracking(self):
        self.root.destroy()
        import tracking_page

    def report(self):
        # self.root.destroy()
        os.system("python date_tracking.py")


root = Tk()
obj = Main(root)
root.mainloop()
