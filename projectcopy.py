from tkinter import *
from tkinter.ttk import Button,Entry

class Main():
    def __init__(self,parent):
        self.parent=parent
        self.parent.title("Login")
        
        self.page=StringVar() 
        self.loginName=StringVar()
        self.loginPass=StringVar()
        self.signinName=StringVar()
        self.signinPass=StringVar()
        
        
        self.createWidgets()
        
        
        
    def createWidgets(self):
        Label(self.parent,textvariable=self.page,font=("",20))
        frame1=Frame(self.parent)
        Label(frame1,text="Name").grid(sticky=W)
        Entry(frame1,textvariable=self.loginName).grid(row=0,column=1,padx=10,pady=10)
        Label(frame1,text="Password").grid(sticky=W)
        Entry(frame1,textvariable=self.loginPass,show="$").grid(row=1,column=1)
        Button(frame1,text="Login",command=self.login).grid(pady=10)
        Button(frame1,text="Sign Up",command=self.signin).grid(row =2,column=1,pady=10)
        frame1.pack(padx=10,pady=10)
        
        
        
        frame2=Frame(self.parent)
        Label(frame2,text="Name").grid(sticky=W)
        Entry(frame2,textvariable=self.signinName).grid(row=0,column=1,padx=10,pady=10)
        Label(frame2,text="Password").grid(sticky=W)
        Entry(frame2,textvariable=self.signinPass,show="$").grid(row=1,column=1)
        self.loginFrame=frame1
        self.signinFrame=frame2
        
    def login(self):
        return None
    def signin(self):
        self.loginFrame.pack_forget()
        self.signinFrame.pack()
if __name__=="__main__":
    root=Tk()
    Main(root)
    root.mainloop()
