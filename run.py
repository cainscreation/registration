import sqlite3
from tkinter import *
from tkinter import messagebox


class DB:
    def __init__(self):
        self.conn = sqlite3.connect("register.db")
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, name TEXT, batch TEXT, sap INTEGER)")
        self.conn.commit()

    def __del__(self):
        self.conn.close()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return rows

    def insert(self, name, batch, sap):
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?)", (name, batch, sap))
        self.conn.commit()
        self.view()

    def update(self, id, name, batch, sap):
        self.cur.execute("UPDATE book SET name=?, batch=?, sap=? WHERE id=?", (name, batch, sap, id))
        self.view()

    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id=?", (id,))
        self.conn.commit()
        self.view()

    def search(self, name="", batch="", sap=""):
        self.cur.execute("SELECT * FROM book WHERE name=? OR batch=? OR sap=?", (name, batch, sap))
        rows = self.cur.fetchall()
        return rows


db = DB()


def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    e1.delete(0, END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END, selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END, selected_tuple[3])


def view_command():
    list1.delete(0, END)
    for row in db.view():
        list1.insert(END, row)


def search_command():
    list1.delete(0, END)
    for row in db.search(name_text.get(), batch_text.get(), sap_text.get()):
        list1.insert(END, row)


def add_command():
    db.insert(name_text.get(), batch_text.get(), sap_text.get())
    list1.delete(0, END)
    list1.insert(END, (name_text.get(), batch_text.get(), sap_text.get()))


def delete_command():
    db.delete(selected_tuple[0])


def update_command():
    db.update(selected_tuple[0], name_text.get(), batch_text.get(), sap_text.get())


window = Tk()

window.title("Registration Page")


def on_closing():
    dd = db
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()
        del dd


window.protocol("WM_DELETE_WINDOW", on_closing)  # handle window closing

l1 = Label(window, text="name")
l1.grid(row=0, column=0)

l2 = Label(window, text="batch")
l2.grid(row=0, column=2)

l3 = Label(window, text="sap")
l3.grid(row=1, column=0)

name_text = StringVar()
e1 = Entry(window, textvariable=name_text)
e1.grid(row=0, column=1)

batch_text = StringVar()
e2 = Entry(window, textvariable=batch_text)
e2.grid(row=0, column=3)

sap_text = StringVar()
e3 = Entry(window, textvariable=sap_text)
e3.grid(row=1, column=1)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text="View all", width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search entry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add entry", width=12, command=add_command)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update selected", width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete selected", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()
