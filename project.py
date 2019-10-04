from tkinter import *
import tkinter as tkr
import sqlite3
import datetime

with sqlite3.connect("quit.db") as db:
    cursur=db.cursur()
cursur.execute("CREATE TABLE IF NOT EXISTS user(username TEXT NOT NULL, password TEXT NOT NULL);")
cursur.execute("SELECT * FROM user")
db.commit()
db.close()

app = tkr.Tk()
C = tkr.Canvas(app, bg="black")
app.title("Project")

img = PhotoImage(file="logo.png")      
C.create_image(500,500, anchor=CENTER, image=img)   

label1 = Label(C,text="Username")
label2 = Label(C,text="password")

entry1=Entry(C)
entry2=Entry(C,show='#')

label1.grid(row=0,column=0,padx=20, pady=20)
label2.grid(row=1,column=0,padx=20, pady=20)

entry1.grid(row=0,column=1,padx=20, pady=20)
entry2.grid(row=1,column=1,padx=20, pady=20)

app.geometry("1000x1000")
app.wm_attributes("-alpha",0.9)
C.pack(fill='both', expand=True)

def callback():
    tkMessageBox.showinfo( "Hello Python", "Hello World")

b = tkr.Button(app, text="OK", command=callback)
b.pack()
app.mainloop()