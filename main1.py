from tkinter import *
from tkinter import ttk
import sqlite3

class Student:
    def __init__(self, main):
        self.main = main
        self.t_Frame = Frame(self.main, height=50, width=1200, background="blue", bd=2)
        self.t_Frame.pack()
        self.Title = Label(self.t_Frame, text="student management system", font="arial 20 bold", width=1200, bg="blue")
        self.Title.pack()

        self.Frame_1 = Frame(self.main, height=580, width=400, bd=2, relief=GROOVE, bg='YELLOW')
        self.Frame_1.pack(side=LEFT)
        self.Frame_1.pack_propagate(0)

        Label(self.Frame_1, text='Student Details', background="yellow", font="arial 12 bold").place(x=20, y=20)

        self.Id = Label(self.Frame_1, text="ID", background="black", font="arial 12 bold")
        self.Id.place(x=40, y=60)
        self.Id.Entry = Entry(self.Frame_1, width=40)
        self.Id.Entry.place(x=150, y=60)

        self.Name = Label(self.Frame_1, text="Name", background="black", font="arial 12 bold")
        self.Name.place(x=40, y=100)
        self.Name.Entry = Entry(self.Frame_1, width=40)
        self.Name.Entry.place(x=150, y=100)

        self.Age = Label(self.Frame_1, text="Age", background="black", font="arial 12 bold")
        self.Age.place(x=40, y=140)
        self.Age.Entry = Entry(self.Frame_1, width=40)
        self.Age.Entry.place(x=150, y=140)

        self.DOB = Label(self.Frame_1, text="DOB", background="black", font="arial 12 bold")
        self.DOB.place(x=40, y=180)
        self.DOB.Entry = Entry(self.Frame_1, width=40)
        self.DOB.Entry.place(x=150, y=180)

        self.Gender = Label(self.Frame_1, text="Gender", background="black", font="arial 12 bold")
        self.Gender.place(x=40, y=220)
        self.Gender.Entry = Entry(self.Frame_1, width=40)
        self.Gender.Entry.place(x=150, y=220)

        self.City = Label(self.Frame_1, text="City", background="black", font="arial 12 bold")
        self.City.place(x=40, y=260)
        self.City.Entry = Entry(self.Frame_1, width=40)
        self.City.Entry.place(x=150, y=260)

        # ========================== BUTTONS =============================
        self.Button_Frame = Frame(self.Frame_1, height=250, width=250, relief=GROOVE, bd=2, background='yellow')
        self.Button_Frame.place(x=80, y=300)

        self.Add = Button(self.Button_Frame, text='Add', width=25, font="arial 11 bold", command=self.Add)
        self.Add.pack()

        self.update_button = Button(self.Button_Frame, text='Update', width=25, font="arial 11 bold", command=self.update)
        self.update_button.pack()

        self.delete = Button(self.Button_Frame, text='Delete', width=25, font="arial 11 bold", command=self.delete)
        self.delete.pack()

        self.clear = Button(self.Button_Frame, text='Clear', width=25, font="arial 11 bold", command=self.clear)
        self.clear.pack()

        self.Frame_2 = Frame(self.main, height=580, width=800, bd=2, relief=GROOVE, bg='BLUE')
        self.Frame_2.pack(side=RIGHT)

        self.tree = ttk.Treeview(self.Frame_2, columns=("c1", "c2", "c3", "c4", "c5", "c6"), show="headings", height=26)

        self.tree.column("#1", anchor=CENTER, width=40)
        self.tree.heading("#1", text="ID")

        self.tree.column("#2", anchor=CENTER, width=100)
        self.tree.heading("#2", text="Name")

        self.tree.column("#3", anchor=CENTER, width=115)
        self.tree.heading("#3", text="DOB")

        self.tree.column("#4", anchor=CENTER, width=110)
        self.tree.heading("#4", text="Age")

        self.tree.column("#5", anchor=CENTER, width=110)
        self.tree.heading("#5", text="Gender")

        self.tree.column("#6", anchor=CENTER)
        self.tree.heading("#6", text="City")

        self.tree.insert("", index=0, values=(1, "vijay", 18, "11-02-2002", "male", "chennai"))
        self.tree.pack()

    def Add(self):
        id = self.Id.Entry.get()
        name = self.Name.Entry.get()
        age = self.Age.Entry.get()
        dob = self.DOB.Entry.get()
        gender = self.Gender.Entry.get()
        city = self.City.Entry.get()
        c = sqlite3.connect("students.db")
        curses = c.cursor()
        curses.execute("INSERT INTO Student(ID,NAME,AGE,DOB,GENDER,CITY) VALUES(?,?,?,?,?,?)", (id, name, age, dob, gender, city))
        c.commit()
        c.close()
        print("Values inserted")
        self.tree.insert('', index=0, values=(id, name, age, dob, gender, city))

    def delete(self):
        item = self.tree.selection()[0]
        selected_item = self.tree.item(item)['values'][0]
        print(selected_item)
        c = sqlite3.connect("students.db")
        cursor = c.cursor()
        cursor.execute("DELETE FROM students WHERE ID={}".format(selected_item))
        print("value deleted")
        c.commit()
        c.close()
        self.tree.delete(item)

    def update(self):
        id = self.Id.Entry.get()
        name = self.Name.Entry.get()
        age = self.Age.Entry.get()
        dob = self.DOB.Entry.get()
        gender = self.Gender.Entry.get()
        city = self.City.Entry.get()
        item = self.tree.selection()[0]

        # Get the selected item's ID for updating the correct row
        selected_item = self.tree.item(item)['values'][0]

        c = sqlite3.connect("students.db")
        cursor = c.cursor()
        cursor.execute("UPDATE Student SET ID=?, NAME=?, AGE=?, DOB=?, GENDER=?, CITY=? WHERE ID=?",
                       (id, name, age, dob, gender, city, selected_item))
        c.commit()
        c.close()

        # Update the treeview
        self.tree.item(item, values=(id, name, age, dob, gender, city))

    def clear(self):
        self.Id.Entry.delete(0, END)
        self.Name.Entry.delete(0, END)
        self.Age.Entry.delete(0, END)
        self.DOB.Entry.delete(0, END)
        self.Gender.Entry.delete(0, END)
        self.City.Entry.delete(0, END)


main = Tk()
main.title("Student Management System")
main.resizable(False, False)
main.geometry("1200x600")

Student(main)
main.mainloop()
