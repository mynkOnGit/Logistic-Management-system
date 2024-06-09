import os
from tkinter import *
from PIL import Image, ImageTk

class AdminPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Page")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")

        self.load_background()

        admin_frame = Frame(self.root, bd=2, relief=RIDGE, bg="beige")
        admin_frame.place(x=430, y=140, width=550, height=240)

        title = Label(text="Admin Dashboard", font=("Noto Sans", 25, "bold"))
        title.place(x=0, y=30, relwidth=1)

        self.create_button(admin_frame, "Reports", self.reports, 45, 50)
        self.create_button(admin_frame, "View Users", self.view_users, 255, 50)

        self.root.bind("<Configure>", self.resize_bg)

    def load_background(self):
        self.bg_image = Image.open("105.png")
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.lbl_bg = Label(self.root, image=self.bg_photo)
        self.lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

    def resize_bg(self, event):
        width, height = event.width, event.height
        aspect_ratio = self.bg_image.width / self.bg_image.height

        new_width = width if width < height * aspect_ratio else height * aspect_ratio
        new_height = height if height < width / aspect_ratio else width / aspect_ratio

        resized_image = self.bg_image.resize((int(new_width), int(new_height)), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(resized_image)
        self.lbl_bg.config(image=self.bg_photo)

    def create_button(self, frame, text, command, x, y):
        btn = Button(frame, text=text, command=command, font=("Elephant", 13),
                     bg="#0077be", activebackground="#005ea6", fg="black", activeforeground="white",
                     cursor="hand2")
        btn.place(x=x, y=y, width=200, height=45)

    def reports(self):
        os.system("python date_tracking.py")

    def view_users(self):
        os.system("python view_users_page.py")

if __name__ == "__main__":
    root = Tk()
    obj = AdminPage(root)
    root.mainloop()
