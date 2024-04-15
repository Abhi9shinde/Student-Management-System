from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from student import Student

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("900x700")

        self.username = StringVar()
        self.password = StringVar()
        bg_image = Image.open(r"img\background.webp")
        bg_image = bg_image.resize((900, 700), Image.ANTIALIAS)
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        # Create a label to display the background image
        bg_label = Label(self.root, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        col_img=Image.open(r"img\college.png")
        col_img=col_img.resize((100,100),Image.ANTIALIAS)
        self.photocol_img=ImageTk.PhotoImage(col_img)
        cl_lbl=Label(self.root,image=self.photocol_img,bd=2,relief=RIDGE)
        cl_lbl.place(x=390,y=80,width=100,height=100)

        Col_title=Label(self.root,bd=10,text="P.E.S.Moden College of Engineering",font=("Arial Baltic",20,"bold"),fg="black",bg="white")
        Col_title.place(x=200,y=250,width=500,height=50)

        lbl_username = Label(self.root, text="Username:")
        lbl_username.place(x=350, y=350)  

        entry_username = Entry(self.root, textvariable=self.username)
        entry_username.place(x=450, y=350)

        lbl_password = Label(self.root, text="Password:")
        lbl_password.place(x=350, y=380)  

        entry_password = Entry(self.root, textvariable=self.password, show="*")
        entry_password.place(x=450, y=380)  

        btn_login = Button(self.root, text="Login", command=self.login)
        btn_login.place(x=420, y=450)

    def login(self):
        username = self.username.get()
        password = self.password.get()

        # Check if username and password are correct
        if username == "admin" and password == "admin123":
            messagebox.showinfo("Success", "Login Successful")
            self.open_main_application()
            self.root.destroy()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def open_main_application(self):
        root_student = Toplevel(self.root)
        Student(root_student)
        root_student.mainloop()
        
        
        

if __name__ == "__main__":
    root = Tk()
    login_page = Login(root)
    root.mainloop()