def data_fetch_teacher(self):
    #     connection=mysql.connector.connect(host="localhost",username="root",password="Abhi9shinde@2004",database="student2")
    #     my_cursor=connection.cursor()
    #     my_cursor.execute("SELECT * FROM Teacher")
    #     data=my_cursor.fetchall()
    #     if len(data)!=0:
    #         self.teacher_tab.delete(*self.teacher_tab.get_children())
    #         for i in data:
    #             self.teacher_tab.insert("",END,values=i)
    #         connection.commit()
    #     connection.close()