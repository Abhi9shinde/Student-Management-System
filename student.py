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
        reset_btn.grid(row=0,column=3,padx=6,pady=4)
        
############################################RIGHT FRAME##########################################################
        Right_Data_Frame=LabelFrame(Create_frame,bd=4,relief=RIDGE,padx=3,text="Student Info",font=("Arial Baltic",12,"bold"),fg="red",bg="white")
        Right_Data_Frame.place(x=680,y=10,width=775,height=540)

        #Search Frame
        Search_Frame=LabelFrame(Right_Data_Frame,bd=4,relief=RIDGE,padx=3,text="Get Student Details",font=("Arial Baltic",12,"bold"),fg="red",bg="white")
        Search_Frame.place(x=0,y=0,width=760,height=55)
        #Search By
        lbl_search_student=Label(Search_Frame,text="Search By:",font=("Arial",10,"bold"),fg="red",bg="white")
        lbl_search_student.grid(row=0,column=0,padx=5,sticky=W )

        Drop_search=ttk.Combobox(Search_Frame,font=("Arial ",10,"bold"),width=17,state="readonly")
        Drop_search["value"]=("Select :","Student ERP ID","Roll No.","Phone no.")
        Drop_search.current(0)
        Drop_search.grid(row=0,column=2)

        search_entry=ttk.Entry(Search_Frame,font=("Arial",10,"bold"),width=25)
        search_entry.grid(row=0,column=3,padx=10,sticky=W)
        #Search Button
        Search_btn=Button(Search_Frame,text="SEARCH",font=("Arial",10,"bold"),width=17,bg="white",fg="black")
        Search_btn.grid(row=0,column=4,padx=10)
        #Show all students
        Showall_btn=Button(Search_Frame,text="SHOW ALL",font=("Arial",10,"bold"),width=17,bg="white",fg="black")
        Showall_btn.grid(row=0,column=5,padx=10)

        #Table FRAME
        table_frame=Frame(Right_Data_Frame,bd=4,relief=RIDGE)
        table_frame.place(x=0,y=56,width=760,height=455)

        #scroll
        scroll=ttk.Scrollbar(table_frame,orient=HORIZONTAL)

        self.student_tab=ttk.Treeview(table_frame,columns=("Student_ID","Roll_no","Student_name","Dept_name","Course","Year","Sem","Div","Teacher","Gender","DOB","Email","Phone","Address"),xscrollcommand=scroll.set)
        scroll.pack(side=BOTTOM,fill=X)
        scroll.config(command=self.student_tab.xview)
        
        self.student_tab.heading("Student_ID",text="Student_ID")
        self.student_tab.heading("Roll_no",text="Roll_no")
        self.student_tab.heading("Student_name",text="Student_name")
        self.student_tab.heading("Dept_name",text="Dept_name")
        self.student_tab.heading("Course",text="Course")
        self.student_tab.heading("Year",text="Year")
        self.student_tab.heading("Sem",text="Sem")
        self.student_tab.heading("Div",text="Div")
        self.student_tab.heading("Teacher",text="Teacher")
        self.student_tab.heading("Gender",text="Gender")
        self.student_tab.heading("DOB",text="DOB")
        self.student_tab.heading("Email",text="Email")
        self.student_tab.heading("Phone",text="Phone")
        self.student_tab.heading("Address",text="Address")

        self.student_tab["show"]="headings"

        self.student_tab.column("Student_ID",width=100)
        self.student_tab.column("Roll_no",width=100)
        self.student_tab.column("Student_name",width=200)
        self.student_tab.column("Dept_name",width=150)
        self.student_tab.column("Course",width=100)
        self.student_tab.column("Year",width=100)
        self.student_tab.column("Sem",width=50)
        self.student_tab.column("Div",width=50)
        self.student_tab.column("Teacher",width=100)
        self.student_tab.column("Gender",width=100)
        self.student_tab.column("DOB",width=100)
        self.student_tab.column("Email",width=100)
        self.student_tab.column("Phone",width=100)
        self.student_tab.column("Address",width=100)
        
        self.student_tab.pack(fill=BOTH,expand=0)




if __name__== "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()