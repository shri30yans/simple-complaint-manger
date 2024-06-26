from database import databaseClass
import tkinter as tk
from tkinter import ttk

databaseObj = databaseClass()
databaseObj.intialize()

root = tk.Tk()
root.title("Complaint Manager")
menu = tk.Menu(root)
root.config(menu = menu)

# GUI

class LoginFrame:
    def __init__(self,root,databaseObj):
        self.databaseObj = databaseObj
            
        self.frame = tk.Frame(root,width = 800,height = 600)
        self.main = tk.Label(self.frame ,text = "Login", font='Helvetica 12 bold')
        
        self.username = tk.Label(self.frame ,text = "Username")
        self.password = tk.Label(self.frame ,text = "Password")

        self.username_textbox = tk.Text(self.frame,height=1,width=30)
        self.password_textbox = tk.Text(self.frame,height=1,width=30)

        self.loginbtn = ttk.Button(self.frame ,text="Login",command = self.clicked,width=30)
        self.registerbtn = ttk.Button(self.frame ,text="Register",command = self.clicked,width=30)

    def SetFrame(self):
        self.hide_all_frames()
        self.frame.grid(row = 0,column = 0)
        self.main.grid(row=0,column=1,padx=(5,70),pady=(10,20))
        
        self.username.grid(row=1,column=1)
        self.password.grid(row=2,column=1)

        self.username_textbox.grid(row=1,column=2,padx=(10,40),pady=(5,5))
        self.password_textbox.grid(row=2,column=2,padx=(10,40),pady=(5,15))

        
        self.loginbtn.grid(row=3,column=2,padx=(10,20),pady=(5,15)) 
        self.registerbtn.grid(row=4,column=2,padx=(10,20),pady=(5,10)) 

    
    def hide_all_frames(self):
        CreateComplaintFrameObj.frame.grid_forget()
        ShowComplaintsFrameObj.frame.grid_forget()


    def clicked(self):
        username = self.desc_textbox.get(1.0, "end-1c")
        enteredpassword = self.desc_textbox.get(1.0, "end-1c")

        password = databaseObj.get_password(username)
        if password is None:
            print(self.databaseObj.get_all_issues())


class RegisterFrame:
    def __init__(self,root,databaseObj):
        self.databaseObj = databaseObj
            
        self.frame = tk.Frame(root,width = 800,height = 600)
        self.main = tk.Label(self.frame ,text = "Create a complaint.", font='Helvetica 12 bold')
        
        self.username = tk.Label(self.frame ,text = "Create a user name")
        self.register = tk.Label(self.frame ,text = "Enter a password")

        self.username_textbox = tk.Text(self.frame,height=2,width=50)
        self.password_textbox = tk.Text(self.frame,height=1,width=50)

        self.loginbtn = ttk.Button(self.frame ,text="Login",command = self.clicked,width=40)
        self.registerbtn = ttk.Button(self.frame ,text="Register",command = self.clicked,width=40)


class CreateComplaintFrame:
    def __init__(self,root,databaseObj):
        self.databaseObj = databaseObj
        
        self.frame = tk.Frame(root,width = 800,height = 600)
        self.main = tk.Label(self.frame ,text = "Create a complaint.", font='Helvetica 12 bold')
        
        self.desc = tk.Label(self.frame ,text = "Issue Description")
        self.house_no = tk.Label(self.frame ,text = "House Number")
        self.category = tk.Label(self.frame ,text = "Category")

        self.desc_textbox = tk.Text(self.frame,height=2,width=50)
        self.house_no_textbox = tk.Text(self.frame,height=1,width=50)
        self.category_textbox = tk.Text(self.frame,height=1,width=50)

        self.loginbtn = ttk.Button(self.frame ,text="Submit",command = self.clicked,width=40)
        


    def SetFrame(self):
        self.hide_all_frames()
        self.frame.grid(row = 0,column = 0)
        self.main.grid(row=0,column=1,padx=(5,70),pady=(10,20))
        for index,x in enumerate([self.desc,self.house_no,self.category]):
            x.grid(row=index+1,column=0, padx=(60, 10),pady=(10,0))
        for index,x in enumerate([self.desc_textbox,self.house_no_textbox,self.category_textbox]):
            x.grid(row=index+1,column=1,padx=(5,60),pady=(10,0))

        self.btn.grid(row=5,column=1,padx=(5,70),pady=(20,10)) 
    
    def hide_all_frames(self):
        CreateComplaintFrameObj.frame.grid_forget()
        ShowComplaintsFrameObj.frame.grid_forget()


    def clicked(self):
        desc_text = self.desc_textbox.get(1.0, "end-1c")
        house_no_text = self.house_no_textbox.get(1.0, "end-1c")
        category_text = self.category_textbox.get(1.0, "end-1c")
        
        self.databaseObj.add_issue(description=desc_text,house_no=house_no_text,category=category_text,status="Incomplete")
        print(self.databaseObj.get_all_issues())


class ShowComplaintsFrame:
    def __init__(self,root,databaseObj):
        self.databaseObj = databaseObj
        self.frame = tk.Frame(root,width = 800,height = 600)

    def SetFrame(self):
        self.hide_all_frames()
        self.frame.grid(row = 0,column = 0)
        for index,x in enumerate(["Complaint ID","Description","House Number","Category","Status"]):
            e = tk.Entry(self.frame, width=20,font = "Calibri 10 bold",justify="center")
            e.grid(row=1,column=index)
            e.insert(tk.END,x)
        
        data = self.databaseObj.get_all_issues()
        row_number = 1
        for complaint in data:
            for index,cell_data in enumerate(complaint):
                e = tk.Entry(self.frame, width=20,font = "Calibri 10") 
                e.grid(row=row_number, column=index) 
                e.insert(tk.END,cell_data)
            row_number+=1

    def hide_all_frames(self):
        CreateComplaintFrameObj.frame.grid_forget()
        ShowComplaintsFrameObj.frame.grid_forget()

CreateComplaintFrameObj = CreateComplaintFrame(root= root,databaseObj =databaseObj)
ShowComplaintsFrameObj = ShowComplaintsFrame(root= root,databaseObj =databaseObj)
LoginFrameObj = LoginFrame(root= root,databaseObj =databaseObj)
LoginFrameObj.SetFrame()

# Create a menu item
file_menu = tk.Menu(menu)
# Creating a sub menu by associating it with our parent menu
menu.add_cascade(label="Menu",menu = file_menu)
file_menu.add_command(label = "Create Complaint",command=CreateComplaintFrameObj.SetFrame)
file_menu.add_command(label = "View all your complaints",command=ShowComplaintsFrameObj.SetFrame)

# file_menu.add_command(label = "Decrypt",command = DecryptFrameObj.SetFrame)


#

root.mainloop()