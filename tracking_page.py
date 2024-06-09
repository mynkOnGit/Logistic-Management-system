from tkinter import *
from PIL import ImageTk, Image
import os

class Main:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Page")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")

        self.load_background()

        login_frame = Frame(self.root, bd=2, relief=RIDGE, bg="beige")
        login_frame.place(x=430, y=140, width=550, height=340)

        title = Label(text="Logistic Management System", font=("Noto Sans", 25, "bold")).place(x=0, y=30,
                                                                                                           relwidth=1)


        btn_login = Button(login_frame, text="Manage Tracking", command=self.job_registration, font=("Elephant", 13),
                           bg="#00a8e8", activebackground="#005ea6", fg="black", activeforeground="white",
                           cursor="hand2")
        btn_login.place(x=45, y=180, width=200, height=45)
        btn_login=Button(login_frame,text="Report",command=self.report,font=("Elephant",13),bg="#00a8e8",activebackground="#005ea6",fg="black",activeforeground="white",cursor="hand2").place(x=45,y=50,width=200,height=45)


        btn_login=Button(login_frame,text="Menu",command=self.menu,font=("Elephant",13),bg="#00a8e8",activebackground="#005ea6",fg="black",activeforeground="white",cursor="hand2").place(x=255,y=50,width=200,height=45)


        btn_login = Button(login_frame, text="View Tracking", command=self.availble_jobs, font=("Elephant", 13),
                           bg="#00a8e8", activebackground="navy blue", fg="black", activeforeground="white",
                           cursor="hand2").place(x=255, y=180, width=200, height=45)

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

    def job_registration(self):
        os.system('python add_tracking.py')

    def availble_jobs(self):
        os.system('python view_tracking.py')

    def menu(self):
        self.root.destroy()
        os.system('python Mainpage.py')

    def report(self):
        os.system('python date_tracking.py')

root = Tk()
obj = Main(root)
root.mainloop()
