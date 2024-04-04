from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk  #To Display Images on Screen
import mysql.connector
from tkinter import messagebox

class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("STUDENT MANAGEMENT SYSTEM")
        self.root.geometry("1510x810+0+0")

        self.var_studid=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_div=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.teacher=StringVar()


        
        




 
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

        ##########################################LEFT FRAME##########################################################
       
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
        Drop_Dept=ttk.Combobox(StudentInfo_Frame,textvariable=self.var_dep,font=("Arial ",12,"bold"),width=17,state="readonly")
        Drop_Dept["value"]=("Select Deprtment","Computer Science","Information Technology","EnTC","AIDS","AIML","Mechanical")
        Drop_Dept.current(0)
        Drop_Dept.grid(row=0,column=1)

        #Course
        lbl_Course=Label(StudentInfo_Frame,text="Course",font=("Arial",12,"bold"),bg="white")
        lbl_Course.grid(row=0,column=2,padx=3,sticky=W)
        Drop_Course=ttk.Combobox(StudentInfo_Frame,textvariable=self.var_course,font=("Arial ",12,"bold"),width=17,state="readonly")
        Drop_Course["value"]=("Select Course","FE","SE","TE","TE")
        Drop_Course.current(0)
        Drop_Course.grid(row=0,column=3)

        #Year
        lbl_year=Label(StudentInfo_Frame,text="Academic Year",font=("Arial",12,"bold"),bg="white")
        lbl_year.grid(row=1,column=0,padx=2,sticky=W,pady=10)
        Drop_year=ttk.Combobox(StudentInfo_Frame,textvariable=self.var_year,font=("Arial ",12,"bold"),width=17,state="readonly")
        Drop_year["value"]=("Select Academic Year","2020-21","2021-22","2022-23","2023-24")
        Drop_year.current(0)
        Drop_year.grid(row=1,column=1,pady=10)

        #Semester
        lbl_sem=Label(StudentInfo_Frame,text="Semester",font=("Arial",12,"bold"),bg="white")
        lbl_sem.grid(row=1,column=2,padx=2,sticky=W,pady=10)
        Drop_sem=ttk.Combobox(StudentInfo_Frame,textvariable=self.var_sem,font=("Arial ",12,"bold"),width=17,state="readonly")
        Drop_sem["value"]=("Select Semester","I","II")
        Drop_sem.current(0)
        Drop_sem.grid(row=1,column=3,pady=10)

        #Student Class Frame in Left Frame
        StudentClass_Frame=LabelFrame(Left_Data_Frame,bd=4,relief=RIDGE,padx=3,text="Student Class Information",font=("Arial Baltic",12,"bold"),fg="red",bg="white")
        StudentClass_Frame.place(x=0,y=240,width=640,height=275)
        #Student  ERP ID
        lbl_student_id=Label(StudentClass_Frame,text="Student ERP ID",font=("Arial",10,"bold"),bg="white")
        lbl_student_id.grid(row=0,column=0,padx=2,sticky=W,pady=10)

        id_entry=ttk.Entry(StudentClass_Frame,textvariable=self.var_studid,font=("Arial",10,"bold"),width=20)
        id_entry.grid(row=0,column=1,padx=2,sticky=W,pady=10)
        #Student Name
        lbl_student_name=Label(StudentClass_Frame,text="Student Name",font=("Arial",10,"bold"),bg="white")
        lbl_student_name.grid(row=0,column=2,padx=2,sticky=W,pady=10)

        name_entry=ttk.Entry(StudentClass_Frame,textvariable=self.var_name,font=("Arial",10,"bold"),width=20)
        name_entry.grid(row=0,column=3,padx=2,sticky=W,pady=10)
        #Student Division
        lbl_student_div=Label(StudentClass_Frame,text="Division",font=("Arial",10,"bold"),bg="white")
        lbl_student_div.grid(row=1,column=0,padx=2,sticky=W,pady=10)

        div_entry=ttk.Entry(StudentClass_Frame,textvariable=self.var_div,font=("Arial",10,"bold"),width=20)
        div_entry.grid(row=1,column=1,padx=2,sticky=W,pady=10)
        #Student Class Roll No
        lbl_student_roll=Label(StudentClass_Frame,text="Class Roll No.",font=("Arial",10,"bold"),bg="white")
        lbl_student_roll.grid(row=1,column=2,padx=2,sticky=W,pady=10)

        roll_entry=ttk.Entry(StudentClass_Frame,textvariable=self.var_roll,font=("Arial",10,"bold"),width=20)
        roll_entry.grid(row=1,column=3,padx=2,sticky=W,pady=10)
        #Student Gender
        lbl_student_gender=Label(StudentClass_Frame,text="Gender",font=("Arial",10,"bold"),bg="white")
        lbl_student_gender.grid(row=2,column=0,padx=2,sticky=W,pady=10)

        Drop_gender=ttk.Combobox(StudentClass_Frame,textvariable=self.var_gender,font=("Arial ",10,"bold"),width=17,state="readonly")
        Drop_gender["value"]=("Select Gender","Male","Female","Else you don't exist")
        Drop_gender.current(0)
        Drop_gender.grid(row=2,column=1,pady=10)
        #Student Date of Birth
        lbl_student_dob=Label(StudentClass_Frame,text="DOB",font=("Arial",10,"bold"),bg="white")
        lbl_student_dob.grid(row=2,column=2,padx=5,sticky=W,pady=10)

        dob_entry=ttk.Entry(StudentClass_Frame,textvariable=self.var_dob,font=("Arial",10,"bold"),width=20)
        dob_entry.grid(row=2,column=3,padx=2,sticky=W,pady=10)
        #Student Email
        lbl_student_email=Label(StudentClass_Frame,text="Email",font=("Arial",10,"bold"),bg="white")
        lbl_student_email.grid(row=3,column=0,padx=5,sticky=W,pady=10)

        email_entry=ttk.Entry(StudentClass_Frame,textvariable=self.var_email,font=("Arial",10,"bold"),width=20)
        email_entry.grid(row=3,column=1,padx=2,sticky=W,pady=10)
        #Student Phone
        lbl_student_phone=Label(StudentClass_Frame,text="Phone",font=("Arial",10,"bold"),bg="white")
        lbl_student_phone.grid(row=3,column=2,padx=5,sticky=W,pady=10)

        phone_entry=ttk.Entry(StudentClass_Frame,textvariable=self.var_phone,font=("Arial",10,"bold"),width=20)
        phone_entry.grid(row=3,column=3,padx=2,sticky=W,pady=10)
        #Student Address
        lbl_student_add=Label(StudentClass_Frame,text="Address",font=("Arial",10,"bold"),bg="white")
        lbl_student_add.grid(row=4,column=0,padx=5,sticky=W,pady=10)

        add_entry=ttk.Entry(StudentClass_Frame,textvariable=self.var_address,font=("Arial",10,"bold"),width=20)
        add_entry.grid(row=4,column=1,padx=2,sticky=W,pady=10)
        #Teacher
        lbl_student_id=Label(StudentClass_Frame,text="Teacher_ID",font=("Arial",10,"bold"),bg="white")
        lbl_student_id.grid(row=4,column=2,padx=2,sticky=W,pady=10)

        id_entry=ttk.Entry(StudentClass_Frame,textvariable=self.teacher,font=("Arial",10,"bold"),width=20)
        id_entry.grid(row=4,column=3,padx=2,sticky=W,pady=10)

        #Button Frame
        btn_frame=Frame(Left_Data_Frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=3,y=470,width=635,height=40)
        #ADD Button
        add_btn=Button(btn_frame,text="ADD",command=self.add_data,font=("Arial",10,"bold"),width=17,bg="white",fg="black")
        add_btn.grid(row=0,column=0,padx=6)
        #UPDATE Button
        update_btn=Button(btn_frame,text="UPDATE",command=self.update_data,font=("Arial",10,"bold"),width=17,bg="white",fg="black")
        update_btn.grid(row=0,column=1,padx=6)
        #DELETE Button
        delete_btn=Button(btn_frame,text="DELETE",command=self.delete,font=("Arial",10,"bold"),width=17,bg="white",fg="black")
        delete_btn.grid(row=0,column=2,padx=6)
        #RESET Button
        reset_btn=Button(btn_frame,text="RESET",command=self.reset,font=("Arial",10,"bold"),width=17,bg="white",fg="black")
        reset_btn.grid(row=0,column=3,padx=6,pady=4)
        
        ##########################################RIGHT FRAME##########################################################
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

        self.student_tab=ttk.Treeview(table_frame,columns=("Student_ID","Roll_no","Student_name","Dept_name","Course","Year","Sem","Div","Gender","DOB","Email","Phone","Address","Teacher"),xscrollcommand=scroll.set)
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
        self.student_tab.heading("Gender",text="Gender")
        self.student_tab.heading("DOB",text="DOB")
        self.student_tab.heading("Email",text="Email")
        self.student_tab.heading("Phone",text="Phone")
        self.student_tab.heading("Address",text="Address")
        self.student_tab.heading("Teacher",text="Teacher")

        self.student_tab["show"]="headings"

        self.student_tab.column("Student_ID",width=100)
        self.student_tab.column("Roll_no",width=100)
        self.student_tab.column("Student_name",width=150)
        self.student_tab.column("Dept_name",width=150)
        self.student_tab.column("Course",width=100)
        self.student_tab.column("Year",width=100)
        self.student_tab.column("Sem",width=50)
        self.student_tab.column("Div",width=50)
        self.student_tab.column("Gender",width=100)
        self.student_tab.column("DOB",width=100)
        self.student_tab.column("Email",width=200)
        self.student_tab.column("Phone",width=100)
        self.student_tab.column("Address",width=100)
        self.student_tab.column("Teacher",width=100)

        
        self.student_tab.pack(fill=BOTH,expand=0)
        self.student_tab.bind("<ButtonRelease>",self.cursor)
        self.data_fetch()

        #Teacher Frame
        SearchTeacher_Frame=LabelFrame(Right_Data_Frame,bd=4,relief=RIDGE,padx=3,text="Get Teacher Details",font=("Arial Baltic",12,"bold"),fg="red",bg="white")
        SearchTeacher_Frame.place(x=0,y=290,width=760,height=55)

        Showall_btn=Button(SearchTeacher_Frame,text="SHOW ALL",font=("Arial",10,"bold"),width=17,bg="white",fg="black")
        Showall_btn.grid(row=0,column=6,padx=300)

        


    def add_data(self):
        if(self.var_dep.get()=="" or self.var_studid.get()=="" or self.var_email.get()==""):
            messagebox.showerror("Error","All fields required")
        else:
            try:
                connection=mysql.connector.connect(host="localhost",username="root",password="Abhi9shinde@2004",database="student2")
                my_cursor=connection.cursor()
                my_cursor.execute("INSERT INTO stud_det VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_studid.get(),self.var_roll.get(),self.var_name.get(),self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_sem.get(),self.var_div.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.teacher.get()))
                connection.commit()
                self.data_fetch()
                connection.close()
                messagebox.showinfo("Success","Student Added",parent=self.root)
            except Exception as except1:
                messagebox.showerror("Error",f"Reason:{str(except1)}",parent=self.root)


    #Fetch data from database
    def data_fetch(self):
        connection=mysql.connector.connect(host="localhost",username="root",password="Abhi9shinde@2004",database="student2")
        my_cursor=connection.cursor()
        my_cursor.execute("SELECT * FROM stud_det")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.student_tab.delete(*self.student_tab.get_children())
            for i in data:
                self.student_tab.insert("",END,values=i)
            connection.commit()
        connection.close()
    
    def data_fetch_teacher(self):
        connection=mysql.connector.connect(host="localhost",username="root",password="Abhi9shinde@2004",database="student2")
        my_cursor=connection.cursor()
        my_cursor.execute("SELECT * FROM Teacher")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.student_tab.delete(*self.student_tab.get_children())
            for i in data:
                self.student_tab.insert("",END,values=i)
            connection.commit()
        connection.close()

    def cursor(self,event=""):
        cursor_row=self.student_tab.focus()
        content=self.student_tab.item(cursor_row)
        data=content["values"]
        self.var_studid.set(data[0])
        self.var_roll.set(data[1])
        self.var_name.set(data[2])
        self.var_dep.set(data[3])
        self.var_course.set(data[4])
        self.var_div.set(data[7])
        self.var_year.set(data[5])
        self.var_sem.set(data[6])
        self.var_gender.set(data[8])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_dob.set(data[9])   
        self.var_address.set(data[12])
        self.teacher.set(data[13])

    def update_data(self):
        if(self.var_dep.get()=="" or self.var_studid.get()=="" or self.var_email.get()==""):
            messagebox.showerror("Error","All fields required")
        else:
            try:
                update=messagebox.askyesno("Update","Are you sure??",parent=self.root)
                if update>0:
                    connection=mysql.connector.connect(host="localhost",username="root",password="Abhi9shinde@2004",database="student2")
                    my_cursor=connection.cursor()
                    my_cursor.execute("UPDATE stud_det set Roll_No=%s,Student_Name=%s,Dept_Name=%s,Course=%s,Year=%s,Sem=%s,Division=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teach_id=%s WHERE Student_id=%s",(self.var_roll.get(),self.var_name.get(),self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_sem.get(),self.var_div.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.teacher.get(),self.var_studid.get()))
                else:
                    if not update:
                        return
                connection.commit()
                self.data_fetch()
                connection.close()

                messagebox.showinfo("Success","Student Profile Updated successfully",parent=self.root)

            except Exception as except1:
                messagebox.showerror("Error",f"Reason:{str(except1)}",parent=self.root)

    #DELETE RECORD
    def delete(self):
        if self.var_studid.get()=="":
            messagebox.showerror("Error","All fields required")
        else:
            try:
                Del=messagebox.askyesno("Delete","Delete this record??")
                if Del>0:
                    connection=mysql.connector.connect(host="localhost",username="root",password="Abhi9shinde@2004",database="student2")
                    my_cursor=connection.cursor()
                    my_cursor.execute("DELETE FROM stud_det WHERE Student_id=%s",(self.var_studid.get(),))
                else:
                    if not Del:
                        return
                connection.commit()
                self.data_fetch()
                connection.close()

                messagebox.showinfo("Success","Record Deleted",parent=self.root)

            except Exception as except1:
                messagebox.showerror("Error","a",parent=self.root)
    
    def reset(self):
        self.var_studid.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_dep.set("Select Deaprtment")
        self.var_course.set("Select Course")
        self.var_div.set("")
        self.var_year.set("Select Academic Year")
        self.var_sem.set("Select Semester")
        self.var_gender.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_dob.set("")   
        self.var_address.set("")
        self.teacher.set("")



        
        





    
    




















if __name__== "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()