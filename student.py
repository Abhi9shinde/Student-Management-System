from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk  #To Display Images on Screen

class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("STUDENT MANAGEMENT SYSTEM")
        self.root.geometry("1510x810+0+0")
 
        #uni Image
        uni_img=Image.open(r"img\uni.png")
        uni_img=uni_img.resize((540,160),Image.ANTIALIAS)
        self.photouni_img=ImageTk.PhotoImage(uni_img)

        self.btn2=Button(self.root,image=self.photouni_img,cursor="hand2")
        self.btn2.place(x=500,y=0,width=540,height=160)

        #for Background Image
        img=Image.open(r"img\image1_0.jpg")
        img=img.resize((1510,840),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        bg_lbl=Label(self.root,image=self.photoimg,bd=2,relief=RIDGE)
        bg_lbl.place(x=0,y=160,width=1510,height=840)


        #Title
        lbl_title=Label(bg_lbl,bd=10,text="STUDENT MANAGEMENT SYSTEM",font=("Arial Baltic",37,"bold"),fg="teal",bg="white")
        lbl_title.place(x=0,y=0,width=1510,height=50)

        #Frames on GUI
        Create_frame=Frame(bg_lbl,bd=2,relief=RIDGE,bg="white")
        Create_frame.place(x=15,y=55,width=1470,height=560)

############################################LEFT FRAME##########################################################
       
        Left_Data_Frame=LabelFrame(Create_frame,bd=4,relief=RIDGE,padx=3,text="Student Info",font=("Arial Baltic",12,"bold"),fg="red",bg="white")
        Left_Data_Frame.place(x=10,y=10,width=650,height=540)

        #College Image
        col_img=Image.open(r"img\college.png")
        col_img=col_img.resize((100,100),Image.ANTIALIAS)
        self.photocol_img=ImageTk.PhotoImage(col_img)
        
        cl_lbl=Label(Left_Data_Frame,image=self.photocol_img,bd=2,relief=RIDGE)
        cl_lbl.place(x=0,y=0,width=100,height=100)

        #College Name
        Col_title=Label(Left_Data_Frame,bd=10,text="P.E.S.Moden College of Engineering",font=("Arial Baltic",20,"bold"),fg="black",bg="white")
        Col_title.place(x=100,y=0,width=500,height=120)

        #Current course Info Frame in Left Frame
        StudentInfo_Frame=LabelFrame(Left_Data_Frame,bd=4,relief=RIDGE,padx=3,text="Current Course Info",font=("Arial Baltic",12,"bold"),fg="red",bg="white")
        StudentInfo_Frame.place(x=0,y=120,width=630,height=115)

        #Department
        lbl_Dept=Label(StudentInfo_Frame,text="Deprtment",font=("Arial",12,"bold"),bg="white")
        lbl_Dept.grid(row=0,column=0,padx=2,sticky=W)
        Drop_Dept=ttk.Combobox(StudentInfo_Frame,font=("Arial ",12,"bold"),width=17,state="readonly")
        Drop_Dept["value"]=("Select Deprtment","Computer Science","Information Technology","EnTC","AIDS","AIML","Mechanical")
        Drop_Dept.current(0)
        Drop_Dept.grid(row=0,column=1)

        #Course
        lbl_Course=Label(StudentInfo_Frame,text="Course",font=("Arial",12,"bold"),bg="white")
        lbl_Course.grid(row=0,column=2,padx=3,sticky=W)
        Drop_Course=ttk.Combobox(StudentInfo_Frame,font=("Arial ",12,"bold"),width=17,state="readonly")
        Drop_Course["value"]=("Select Course","FE","SE","TE","TE")
        Drop_Course.current(0)
        Drop_Course.grid(row=0,column=3)

        #Year
        lbl_year=Label(StudentInfo_Frame,text="Academic Year",font=("Arial",12,"bold"),bg="white")
        lbl_year.grid(row=1,column=0,padx=2,sticky=W,pady=10)
        Drop_year=ttk.Combobox(StudentInfo_Frame,font=("Arial ",12,"bold"),width=17,state="readonly")
        Drop_year["value"]=("Select Academic Year","2020-21","2021-22","2022-23","2023-24")
        Drop_year.current(0)
        Drop_year.grid(row=1,column=1,pady=10)

        #Semester
        lbl_sem=Label(StudentInfo_Frame,text="Semester",font=("Arial",12,"bold"),bg="white")
        lbl_sem.grid(row=1,column=2,padx=2,sticky=W,pady=10)
        Drop_sem=ttk.Combobox(StudentInfo_Frame,font=("Arial ",12,"bold"),width=17,state="readonly")
        Drop_sem["value"]=("Select Semester","I","II")
        Drop_sem.current(0)
        Drop_sem.grid(row=1,column=3,pady=10)

        #Student Class Frame in Left Frame
        StudentClass_Frame=LabelFrame(Left_Data_Frame,bd=4,relief=RIDGE,padx=3,text="Student Class Information",font=("Arial Baltic",12,"bold"),fg="red",bg="white")
        StudentClass_Frame.place(x=0,y=240,width=640,height=275)
        #Student  ERP ID
        lbl_student_id=Label(StudentClass_Frame,text="Student ERP ID",font=("Arial",10,"bold"),bg="white")
        lbl_student_id.grid(row=0,column=0,padx=2,sticky=W,pady=10)

        id_entry=ttk.Entry(StudentClass_Frame,font=("Arial",10,"bold"),width=20)
        id_entry.grid(row=0,column=1,padx=2,sticky=W,pady=10)
        #Student Name
        lbl_student_name=Label(StudentClass_Frame,text="Student Name",font=("Arial",10,"bold"),bg="white")
        lbl_student_name.grid(row=0,column=2,padx=2,sticky=W,pady=10)

        name_entry=ttk.Entry(StudentClass_Frame,font=("Arial",10,"bold"),width=20)
        name_entry.grid(row=0,column=3,padx=2,sticky=W,pady=10)
        #Student Division
        lbl_student_div=Label(StudentClass_Frame,text="Division",font=("Arial",10,"bold"),bg="white")
        lbl_student_div.grid(row=1,column=0,padx=2,sticky=W,pady=10)

        div_entry=ttk.Entry(StudentClass_Frame,font=("Arial",10,"bold"),width=20)
        div_entry.grid(row=1,column=1,padx=2,sticky=W,pady=10)
        #Student Class Roll No
        lbl_student_roll=Label(StudentClass_Frame,text="Class Roll No.",font=("Arial",10,"bold"),bg="white")
        lbl_student_roll.grid(row=1,column=2,padx=2,sticky=W,pady=10)

        roll_entry=ttk.Entry(StudentClass_Frame,font=("Arial",10,"bold"),width=20)
        roll_entry.grid(row=1,column=3,padx=2,sticky=W,pady=10)
        #Student Gender
        lbl_student_gender=Label(StudentClass_Frame,text="Gender",font=("Arial",10,"bold"),bg="white")
        lbl_student_gender.grid(row=2,column=0,padx=2,sticky=W,pady=10)

        Drop_gender=ttk.Combobox(StudentClass_Frame,font=("Arial ",10,"bold"),width=17,state="readonly")
        Drop_gender["value"]=("Select Gender","Male","Female","Else you don't exist")
        Drop_gender.current(0)
        Drop_gender.grid(row=2,column=1,pady=10)
        #Student Date of Birth
        lbl_student_dob=Label(StudentClass_Frame,text="DOB",font=("Arial",10,"bold"),bg="white")
        lbl_student_dob.grid(row=2,column=2,padx=5,sticky=W,pady=10)

        dob_entry=ttk.Entry(StudentClass_Frame,font=("Arial",10,"bold"),width=20)
        dob_entry.grid(row=2,column=3,padx=2,sticky=W,pady=10)
        #Student Email
        lbl_student_email=Label(StudentClass_Frame,text="Email",font=("Arial",10,"bold"),bg="white")
        lbl_student_email.grid(row=3,column=0,padx=5,sticky=W,pady=10)

        email_entry=ttk.Entry(StudentClass_Frame,font=("Arial",10,"bold"),width=20)
        email_entry.grid(row=3,column=1,padx=2,sticky=W,pady=10)
        #Student Phone
        lbl_student_phone=Label(StudentClass_Frame,text="Phone",font=("Arial",10,"bold"),bg="white")
        lbl_student_phone.grid(row=3,column=2,padx=5,sticky=W,pady=10)

        phone_entry=ttk.Entry(StudentClass_Frame,font=("Arial",10,"bold"),width=20)
        phone_entry.grid(row=3,column=3,padx=2,sticky=W,pady=10)
        #Student Address
        lbl_student_add=Label(StudentClass_Frame,text="Address",font=("Arial",10,"bold"),bg="white")
        lbl_student_add.grid(row=4,column=0,padx=5,sticky=W,pady=10)

        add_entry=ttk.Entry(StudentClass_Frame,font=("Arial",10,"bold"),width=20)
        add_entry.grid(row=4,column=1,padx=2,sticky=W,pady=10)

        #Button Frame
        btn_frame=Frame(Left_Data_Frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=3,y=470,width=635,height=40)
        #ADD Button
        add_btn=Button(btn_frame,text="ADD",font=("Arial",10,"bold"),width=17,bg="white",fg="black")
        add_btn.grid(row=0,column=0,padx=6)
        #UPDATE Button
        update_btn=Button(btn_frame,text="UPDATE",font=("Arial",10,"bold"),width=17,bg="white",fg="black")
        update_btn.grid(row=0,column=1,padx=6)
        #DELETE Button
        delete_btn=Button(btn_frame,text="DELETE",font=("Arial",10,"bold"),width=17,bg="white",fg="black")
        delete_btn.grid(row=0,column=2,padx=6)
        #RESET Button
        reset_btn=Button(btn_frame,text="RESET",font=("Arial",10,"bold"),width=17,bg="white",fg="black")
        reset_btn.grid(row=0,column=3,padx=6)
        
############################################RIGHT FRAME##########################################################
        Right_Data_Frame=LabelFrame(Create_frame,bd=4,relief=RIDGE,padx=3,text="Student Info",font=("Arial Baltic",12,"bold"),fg="red",bg="white")
        Right_Data_Frame.place(x=680,y=10,width=770,height=540)




if __name__== "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()