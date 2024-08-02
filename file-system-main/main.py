from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import time
from datetime import date

dbfilesystem = sqlite3.connect("filesystem.db")


root = Tk()
root.title("PENSION FILE SYSTEM")
root.iconbitmap("")
root.geometry("900x500+50+100")
root.resizable(0, 0)


class main:
    def login(self):
        self.var1 = self.e1.get()
        self.var2 = self.e2.get()
        cursor = dbfilesystem.cursor()
        cursor.execute(
            "SELECT * FROM UserLogin WHERE UserID='"
            + self.var1
            + "' and Password='"
            + self.var2
            + "'"
        )
        dbfilesystem.commit()
        self.ab = cursor.fetchone()

        if self.ab != None:
            self.under_fm = Frame(root, height=500, width=900, bg="#fff")
            self.under_fm.place(x=0, y=0)

            self.fm2 = Frame(root, bg="#012727", height=80, width=900)
            self.fm2.place(x=0, y=0)

            self.lbb = Label(self.fm2, bg="#012727")
            self.lbb.place(x=15, y=5)
            self.ig = PhotoImage(file="bt1.png")
            self.lbb.config(image=self.ig)

            self.lb3 = Label(
                self.fm2,
                text="DASHBOARD",
                fg="White",
                bg="#012727",
                font=("times new roman", 30, "bold"),
            )
            self.lb3.place(x=325, y=17)

            self.name = Label(
                root,
                text="Name : ",
                bg="#fff",
                fg="black",
                font=("Calibri", 12, "bold"),
            )
            self.name.place(x=5, y=83)
            self.name1 = Label(
                root,
                text=self.ab[0],
                fg="black",
                bg="#fff",
                font=("Calibri", 12, "bold"),
            )
            self.name1.place(x=60, y=83)

            self.today = date.today()
            self.dat = Label(
                root,
                text="Date : ",
                bg="#fff",
                fg="black",
                font=("Calibri", 12, "bold"),
            )
            self.dat.place(x=750, y=83)
            self.dat2 = Label(
                root,
                text=self.today,
                bg="#fff",
                fg="black",
                font=("Calibri", 12, "bold"),
            )
            self.dat2.place(x=800, y=83)

            self.cur()
        else:
            messagebox.showerror("File System", "Your ID or Password is invalid!")

    def cur(self):
        self.fm3 = Frame(root, bg="#fff", width=900, height=390)
        self.fm3.place(x=0, y=110)

        def clock():
            h = str(time.strftime("%H"))
            m = str(time.strftime("%M"))
            s = str(time.strftime("%S"))

            if int(h) >= 12 and int(m) >= 0:
                self.lb7_hr.config(text="PM")

            self.lb1_hr.config(text=h)
            self.lb3_hr.config(text=m)
            self.lb5_hr.config(text=s)

            self.lb1_hr.after(200, clock)

        self.lb1_hr = Label(
            self.fm3,
            text="12",
            font=("times new roman", 20, "bold"),
            bg="#581845",
            fg="white",
        )
        self.lb1_hr.place(x=607, y=0, width=60, height=30)

        self.lb3_hr = Label(
            self.fm3,
            text="05",
            font=("times new roman", 20, "bold"),
            bg="#581845",
            fg="white",
        )
        self.lb3_hr.place(x=677, y=0, width=60, height=30)

        self.lb5_hr = Label(
            self.fm3,
            text="37",
            font=("times new roman", 20, "bold"),
            bg="#581845",
            fg="white",
        )
        self.lb5_hr.place(x=747, y=0, width=60, height=30)

        self.lb7_hr = Label(
            self.fm3,
            text="AM",
            font=("times new roman", 17, "bold"),
            bg="#581845",
            fg="white",
        )
        self.lb7_hr.place(x=817, y=0, width=60, height=30)

        clock()
        self.canvas8 = Canvas(self.fm3, bg="black", width=400, height=300)
        self.canvas8.place(x=475, y=40)

        self.photo9 = PhotoImage(file="bt1.png")
        self.canvas8.create_image(0, 0, image=self.photo9, anchor=NW)

        self.develop = Label(
            self.fm3,
            text="Developed By DON",
            bg="#fff",
            fg="#d7837f",
            font=("Candara", 12, "bold"),
        )
        self.develop.place(x=732, y=350)

        self.bt1 = Button(
            self.fm3,
            text="Receive",
            fg="#fff",
            bg="#581845",
            font=("Candara", 15, "bold"),
            width=170,
            height=0,
            bd=7,
            relief="flat",
            command=self.receive,
            cursor="hand2",
            activebackground="black",
            activeforeground="#581845",
        )
        self.bt1.place(x=40, y=40)
        self.logo = PhotoImage(file="bt1.png")
        self.bt1.config(image=self.logo, compound=LEFT)
        self.small_logo = self.logo.subsample(1, 1)
        self.bt1.config(image=self.small_logo)

        self.bt2 = Button(
            self.fm3,
            text="Issue",
            fg="#fff",
            bg="#581845",
            font=("Candara", 15, "bold"),
            width=170,
            height=0,
            bd=7,
            relief="flat",
            command=self.issue,
            cursor="hand2",
            activebackground="black",
            activeforeground="#581845",
        )
        self.bt2.place(x=250, y=40)
        self.log = PhotoImage(file="bt2.png")
        self.bt2.config(image=self.log, compound=LEFT)
        self.small_log = self.log.subsample(1, 1)
        self.bt2.config(image=self.small_log)

        self.bt3 = Button(
            self.fm3,
            text="Dispatch",
            fg="#fff",
            bg="#581845",
            font=("Candara", 15, "bold"),
            width=170,
            height=0,
            bd=7,
            relief="flat",
            cursor="hand2",
            command=self.dispatch,
            activebackground="black",
            activeforeground="#581845",
        )
        self.bt3.place(x=40, y=120)
        self.log3 = PhotoImage(file="bt3.png")
        self.bt3.config(image=self.log3, compound=LEFT)
        self.small_log3 = self.log3.subsample(1, 1)
        self.bt3.config(image=self.small_log3)

        self.bt4 = Button(
            self.fm3,
            text=" Show",
            fg="#fff",
            bg="#581845",
            font=("Candara", 15, "bold"),
            width=170,
            height=0,
            bd=7,
            relief="flat",
            cursor="hand2",
            command=self.show,
            activebackground="black",
            activeforeground="#581845",
        )
        self.bt4.place(x=250, y=120)
        self.log4 = PhotoImage(file="bt4.png")
        self.bt4.config(image=self.log4, compound=LEFT)
        self.small_log4 = self.log4.subsample(1, 1)
        self.bt4.config(image=self.small_log4)

        self.bt5 = Button(
            self.fm3,
            text="Search",
            fg="#fff",
            bg="#581845",
            font=("Candara", 15, "bold"),
            width=170,
            height=0,
            bd=7,
            relief="flat",
            cursor="hand2",
            command=self.search,
            activebackground="black",
            activeforeground="#581845",
        )
        self.bt5.place(x=40, y=200)
        self.log5 = PhotoImage(file="bt5.png")
        self.bt5.config(image=self.log5, compound=LEFT)
        self.small_log5 = self.log5.subsample(1, 1)
        self.bt5.config(image=self.small_log5)

        self.bt6 = Button(
            self.fm3,
            text="Issued",
            fg="#fff",
            bg="#581845",
            font=("Candara", 15, "bold"),
            width=170,
            height=0,
            bd=7,
            relief="flat",
            cursor="hand2",
            command=self.showissued,
            activebackground="black",
            activeforeground="#581845",
        )
        self.bt6.place(x=250, y=200)
        self.log6 = PhotoImage(file="bt6.png")
        self.bt6.config(image=self.log6, compound=LEFT)
        self.small_log6 = self.log6.subsample(1, 1)
        self.bt6.config(image=self.small_log6)

        try:
            self.bt7 = Button(
                self.fm3,
                text="  Log Out",
                fg="#fff",
                bg="#581845",
                font=("Candara", 15, "bold"),
                width=170,
                height=0,
                bd=7,
                relief="flat",
                cursor="hand2",
                command=self.code,
                activebackground="black",
                activeforeground="#581845",
            )
            self.bt7.place(x=40, y=280)
            self.log7 = PhotoImage(file="bt7.png")
            self.bt7.config(image=self.log7, compound=LEFT)
            self.small_log7 = self.log7.subsample(1, 1)
            self.bt7.config(image=self.small_log7)

        except:
            self.bt8 = ttk.Button(
                self.fm3,
                text="Ram",
                bg="#a40000",
                font=("Candara", 15, "bold"),
                width=150,
                height=0,
            )
            self.bt8.place(x=250, y=280)
            self.log8 = PhotoImage(file="bt8.png")
            self.bt8.config(image=self.log8, compound=LEFT)
            self.small_log8 = self.log8.subsample(3, 3)
            self.bt8.config(image=self.small_log8)

    def receive(self):
        class temp(main):
            def file(self):
                self.fm = Frame(root, bg="#ffe8ec", width=900, height=390)
                self.fm.place(x=0, y=110)

                self.fm1 = Frame(
                    self.fm, bg="#ffe8ec", width=500, height=360, bd=5, relief="flat"
                )
                self.fm1.place(x=200, y=15)

                self.backbt = Button(
                    self.fm,
                    width=60,
                    bg="#ffe8ec",
                    bd=0,
                    relief="flat",
                    command=self.cur,
                    activeforeground="black",
                    activebackground="#ffe8ec",
                )
                self.backbt.place(x=2, y=7)
                self.log = PhotoImage(file="bt1.png")
                self.backbt.config(image=self.log, compound=LEFT)
                self.small_log = self.log.subsample(2, 2)
                self.backbt.config(image=self.small_log)

                self.fll = Frame(self.fm1, width=150, height=40, bg="#ff6690")
                self.fll.place(x=150, y=15)
                self.ll = Label(
                    self.fll,
                    text="ADD FILES",
                    fg="#fff",
                    bg="#ff6690",
                    font=("Canara", 12, "bold"),
                    width=15,
                )
                self.ll.config(height=5)
                self.ll.place(x=0, y=8)

                self.lb = Label(
                    self.fm1,
                    text="fileno",
                    fg="black",
                    bg="#ffe8ec",
                    font=("times new roman", 11, "bold"),
                )
                self.lb.place(x=70, y=90)
                self.lb2 = Label(
                    self.fm1,
                    text="Section",
                    fg="black",
                    bg="#ffe8ec",
                    font=("times new roman", 11, "bold"),
                )
                self.lb2.place(x=70, y=130)
                self.lb3 = Label(
                    self.fm1,
                    text="R.From",
                    fg="black",
                    bg="#ffe8ec",
                    font=("times new roman", 11, "bold"),
                )
                self.lb3.place(x=70, y=170)
                self.lb4 = Label(
                    self.fm1,
                    text="R.By",
                    fg="black",
                    bg="#ffe8ec",
                    font=("times new roman", 11, "bold"),
                )
                self.lb4.place(x=70, y=210)
                self.lb5 = Label(
                    self.fm1,
                    text="Digit",
                    fg="black",
                    bg="#ffe8ec",
                    font=("times new roman", 11, "bold"),
                )
                self.lb5.place(x=70, y=250)
                self.lb6 = Label(
                    self.fm1,
                    text="Problem",
                    fg="black",
                    bg="#ffe8ec",
                    font=("times new roman", 11, "bold"),
                )
                self.lb6.place(x=70, y=290)
                self.lb7 = Label(
                    self.fm1,
                    text="Date",
                    fg="black",
                    bg="#ffe8ec",
                    font=("times new roman", 11, "bold"),
                )
                self.lb7.place(x=70, y=330)
                self.lb8 = Label(
                    self.fm1,
                    text="Status",
                    fg="black",
                    bg="#ffe8ec",
                    font=("times new roman", 11, "bold"),
                )
                self.lb8.place(x=70, y=370)

                self.ee1 = Entry(
                    self.fm1,
                    width=25,
                    bd=4,
                    relief="groove",
                    font=("Calibri", 11, "bold"),
                )
                self.ee1.place(x=180, y=88)
                self.ee2 = Entry(
                    self.fm1,
                    width=25,
                    bd=4,
                    relief="groove",
                    font=("Calibri", 11, "bold"),
                )
                self.ee2.place(x=180, y=130)
                self.ee3 = Entry(
                    self.fm1,
                    width=25,
                    bd=4,
                    relief="groove",
                    font=("Calibri", 11, "bold"),
                )
                self.ee3.place(x=180, y=170)
                self.ee4 = Entry(
                    self.fm1,
                    width=25,
                    bd=4,
                    relief="groove",
                    font=("Calibri", 11, "bold"),
                )
                self.ee4.place(x=180, y=210)
                self.ee5 = Entry(
                    self.fm1,
                    width=25,
                    bd=4,
                    relief="groove",
                    font=("Calibri", 11, "bold"),
                )
                self.ee5.place(x=180, y=250)
                self.ee6 = Entry(
                    self.fm1,
                    width=25,
                    bd=4,
                    relief="groove",
                    font=("Calibri", 11, "bold"),
                )
                self.ee6.place(x=180, y=290)
                self.ee7 = Entry(
                    self.fm1,
                    width=25,
                    bd=4,
                    relief="groove",
                    font=("Calibri", 11, "bold"),
                )
                self.ee7.place(x=180, y=330)
                self.ee8 = Entry(
                    self.fm1,
                    width=25,
                    bd=4,
                    relief="groove",
                    font=("Calibri", 11, "bold"),
                )
                self.ee8.place(x=180, y=370)

                self.bt = Button(
                    self.fm1,
                    text="SUBMIT",
                    width=8,
                    fg="white",
                    bg="#ff6690",
                    font=("Canara", 12, "bold"),
                    bd=3,
                    relief="flat",
                    command=self.submit1,
                    activebackground="black",
                    activeforeground="#ff6690",
                )
                self.bt.place(x=5, y=20)

            def submit1(self):
                try:
                    self.fn = self.ee1.get()
                    self.sc = self.ee2.get()
                    self.rf = self.ee3.get()
                    self.rb = self.ee4.get()
                    self.dg = self.ee5.get()
                    self.pr = self.ee6.get()
                    self.dt = self.ee7.get()

                    if (
                        self.fn
                        and self.sc
                        and self.rf
                        and self.rb
                        and self.dg
                        and self.pr
                        and self.dt
                    ):
                        cursor = dbfilesystem.cursor()
                        cursor.execute(
                            "INSERT INTO files(fileno,section,rfrom,rby,digit,problem,date) values(?,?,?,?,?,?,?)",
                            (
                                self.fn,
                                self.sc,
                                self.rf,
                                self.rb,
                                self.dg,
                                self.pr,
                                self.dt,
                            ),
                        )
                        dbfilesystem.commit()
                        messagebox.showinfo(
                            "Success", "file has been added to the library succesfully"
                        )
                        self.clear()
                    else:
                        messagebox.showerror("Error", "Enter Valid Details")
                except Exception as e:
                    messagebox.showerror("Error", "Enter Valid Details")

            def clear(self):
                self.ee1.delete(0, END)
                self.ee2.delete(0, END)
                self.ee3.delete(0, END)
                self.ee4.delete(0, END)
                self.ee5.delete(0, END)
                self.ee6.delete(0, END)
                self.ee7.delete(0, END)

        obj = temp()
        obj.file()

    def issue(self):
        class temp(main):
            def file(self):
                self.fm = Frame(root, bg="#ffe8ec", width=900, height=390)
                self.fm.place(x=0, y=110)

                self.fm1 = Frame(
                    self.fm, bg="#ffe8ec", width=500, height=360, bd=5, relief="flat"
                )
                self.fm1.place(x=200, y=15)

                self.backbt = Button(
                    self.fm,
                    width=60,
                    bg="#ffe8ec",
                    bd=0,
                    relief="flat",
                    command=self.cur,
                    activeforeground="black",
                    activebackground="#ffe8ec",
                )
                self.backbt.place(x=2, y=7)
                self.log = PhotoImage(file="bt1.png")
                self.backbt.config(image=self.log, compound=LEFT)
                self.small_log = self.log.subsample(2, 2)
                self.backbt.config(image=self.small_log)

                self.fll = Frame(self.fm1, width=150, height=40, bg="#ff6690")
                self.fll.place(x=150, y=15)
                self.ll = Label(
                    self.fll,
                    text="ISSUE FILES",
                    fg="#fff",
                    bg="#ff6690",
                    font=("Canara", 12, "bold"),
                    width=15,
                )
                self.ll.config(height=5)
                self.ll.place(x=0, y=8)

                self.lb = Label(
                    self.fm1,
                    text="FILENO",
                    fg="black",
                    bg="#ffe8ec",
                    font=("times new roman", 11, "bold"),
                )
                self.lb.place(x=70, y=90)
                self.lb2 = Label(
                    self.fm1,
                    text="ISSUED TO",
                    fg="black",
                    bg="#ffe8ec",
                    font=("times new roman", 11, "bold"),
                )
                self.lb2.place(x=70, y=130)
                self.lb3 = Label(
                    self.fm1,
                    text="ISSUE DATE",
                    fg="black",
                    bg="#ffe8ec",
                    font=("times new roman", 11, "bold"),
                )
                self.lb3.place(x=70, y=170)

                self.ee1 = Entry(
                    self.fm1,
                    width=25,
                    bd=4,
                    relief="groove",
                    font=("Calibri", 11, "bold"),
                )
                self.ee1.place(x=180, y=88)
                self.ee2 = Entry(
                    self.fm1,
                    width=25,
                    bd=4,
                    relief="groove",
                    font=("Calibri", 11, "bold"),
                )
                self.ee2.place(x=180, y=130)
                self.ee3 = Entry(
                    self.fm1,
                    width=25,
                    bd=4,
                    relief="groove",
                    font=("Calibri", 11, "bold"),
                )
                self.ee3.place(x=180, y=170)

                self.bt = Button(
                    self.fm1,
                    text="SUBMIT",
                    width=8,
                    fg="white",
                    bg="#ff6690",
                    font=("Canara", 12, "bold"),
                    bd=3,
                    relief="flat",
                    command=self.submit1,
                    activebackground="black",
                    activeforeground="#ff6690",
                )
                self.bt.place(x=70, y=300)

            def submit1(self):
                try:
                    self.fn = self.ee1.get()
                    self.ist = self.ee2.get()
                    self.isd = self.ee3.get()

                    if self.fn and self.ist and self.isd:
                        cursor = dbfilesystem.cursor()
                        cursor.execute(
                            "INSERT INTO issued(fileno,issuedto,issuedate) values(?,?,?)",
                            (
                                self.fn,
                                self.ist,
                                self.isd,
                            ),
                        )
                        dbfilesystem.commit()
                        messagebox.showinfo(
                            "Success", "file has been issued succesfully"
                        )
                        self.clear()
                    else:
                        messagebox.showerror("Error", "Enter Valid Details")
                except Exception as e:
                    messagebox.showerror("Error", "Enter Valid Details")

            def clear(self):
                self.ee1.delete(0, END)
                self.ee2.delete(0, END)
                self.ee3.delete(0, END)

        obj = temp()
        obj.file()

    def dispatch(self):
        class temp(main):
            def file(self):
                self.fm = Frame(root, bg="#ffe8ec", width=900, height=390)
                self.fm.place(x=0, y=110)

                self.fm1 = Frame(
                    self.fm, bg="#ffe8ec", width=500, height=360, bd=5, relief="flat"
                )
                self.fm1.place(x=200, y=15)

                self.backbt = Button(
                    self.fm,
                    width=60,
                    bg="#ffe8ec",
                    bd=0,
                    relief="flat",
                    command=self.cur,
                    activeforeground="black",
                    activebackground="#ffe8ec",
                )
                self.backbt.place(x=2, y=7)
                self.log = PhotoImage(file="bt1.png")
                self.backbt.config(image=self.log, compound=LEFT)
                self.small_log = self.log.subsample(2, 2)
                self.backbt.config(image=self.small_log)

                self.fll = Frame(self.fm1, width=150, height=40, bg="#ff6690")
                self.fll.place(x=150, y=15)
                self.ll = Label(
                    self.fll,
                    text="DISPATCH FILES",
                    fg="#fff",
                    bg="#ff6690",
                    font=("Canara", 12, "bold"),
                    width=15,
                )
                self.ll.config(height=5)
                self.ll.place(x=0, y=8)

                self.lb = Label(
                    self.fm1,
                    text="FILENO",
                    fg="black",
                    bg="#ffe8ec",
                    font=("times new roman", 11, "bold"),
                )
                self.lb.place(x=70, y=90)
                self.lb2 = Label(
                    self.fm1,
                    text="RBY",
                    fg="black",
                    bg="#ffe8ec",
                    font=("times new roman", 11, "bold"),
                )
                self.lb2.place(x=70, y=130)
                self.lb3 = Label(
                    self.fm1,
                    text="SECTION",
                    fg="black",
                    bg="#ffe8ec",
                    font=("times new roman", 11, "bold"),
                )
                self.lb3.place(x=70, y=170)
                self.lb4 = Label(
                    self.fm1,
                    text="DIGIT",
                    fg="black",
                    bg="#ffe8ec",
                    font=("times new roman", 11, "bold"),
                )
                self.lb4.place(x=70, y=210)
                self.lb5 = Label(
                    self.fm1,
                    text="DATE",
                    fg="black",
                    bg="#ffe8ec",
                    font=("times new roman", 11, "bold"),
                )
                self.lb5.place(x=70, y=250)

                self.ee1 = Entry(
                    self.fm1,
                    width=25,
                    bd=4,
                    relief="groove",
                    font=("Calibri", 11, "bold"),
                )
                self.ee1.place(x=180, y=90)
                self.ee2 = Entry(
                    self.fm1,
                    width=25,
                    bd=4,
                    relief="groove",
                    font=("Calibri", 11, "bold"),
                )
                self.ee2.place(x=180, y=130)
                self.ee3 = Entry(
                    self.fm1,
                    width=25,
                    bd=4,
                    relief="groove",
                    font=("Calibri", 11, "bold"),
                )
                self.ee3.place(x=180, y=170)
                self.ee4 = Entry(
                    self.fm1,
                    width=25,
                    bd=4,
                    relief="groove",
                    font=("Calibri", 11, "bold"),
                )
                self.ee4.place(x=180, y=210)
                self.ee5 = Entry(
                    self.fm1,
                    width=25,
                    bd=4,
                    relief="groove",
                    font=("Calibri", 11, "bold"),
                )
                self.ee5.place(x=180, y=250)

                self.bt = Button(
                    self.fm1,
                    text="SUBMIT",
                    width=8,
                    fg="white",
                    bg="#ff6690",
                    font=("Canara", 12, "bold"),
                    bd=3,
                    relief="flat",
                    command=self.submit1,
                    activebackground="black",
                    activeforeground="#ff6690",
                )
                self.bt.place(x=70, y=300)

            def submit1(self):
                try:
                    self.fn = self.ee1.get()
                    self.rb = self.ee2.get()
                    self.sc = self.ee3.get()
                    self.dg = self.ee4.get()
                    self.dt = self.ee5.get()

                    if self.fn and self.rb and self.sc and self.dg and self.dt:
                        cursor = dbfilesystem.cursor()
                        cursor.execute(
                            "INSERT INTO outgoing(fileno,rby,section,digit,date) values(?,?,?,?,?)",
                            (
                                self.fn,
                                self.rb,
                                self.sc,
                                self.dg,
                                self.dt,
                            ),
                        )
                        dbfilesystem.commit()
                        messagebox.showinfo(
                            "Success", "file has been dispatched succesfully"
                        )
                        self.clear()
                    else:
                        messagebox.showerror("Error", "Enter Valid Details")
                except Exception as e:
                    messagebox.showerror("Error", "Enter Valid Details")

            def clear(self):
                self.ee1.delete(0, END)
                self.ee2.delete(0, END)
                self.ee3.delete(0, END)
                self.ee4.delete(0, END)
                self.ee5.delete(0, END)

        obj = temp()
        obj.file()

    def search(self):
        class demt(main):
            def delmdata(self):
                self.fc = Frame(root, bg="#ffe8ec", width=900, height=390)
                self.fc.place(x=0, y=110)
                self.fc1 = Frame(
                    self.fc, bg="#ffe8ec", width=500, height=200, bd=5, relief="flat"
                )
                self.fc1.place(x=200, y=15)
                self.edm = Frame(
                    self.fc1, bg="#b76e79", bd=0, relief="flat", width=130, height=35
                )
                self.edm.place(x=140, y=0)
                self.lac = Label(
                    self.edm,
                    text="RECEIVED",
                    bg="#b76e79",
                    fg="#fff",
                    font=("Calibri", 12, "bold"),
                )
                self.lac.place(x=8, y=5)
                self.label8 = Label(
                    self.fc1,
                    text="Fileno",
                    bg="#ffe8ec",
                    fg="black",
                    font=("Times New Roman", 11, "bold"),
                )
                self.label8.place(x=85, y=65)
                self.entryl = Entry(
                    self.fc1,
                    width=25,
                    bd=4,
                    relief="groove",
                    font=("Calibri", 8, "bold"),
                )
                self.entryl.place(x=130, y=65)
                self.butto = Button(
                    self.fc1,
                    text="SEARCH",
                    bg="#b76e79",
                    fg="#fff",
                    width=8,
                    font=("Calibri", 12, "bold"),
                    command=self.srch,
                    relief="flat",
                    activebackground="black",
                    activeforeground="#b76e79",
                )
                self.butto.place(x=291, y=65)

                self.lac = Label(
                    self.edm,
                    text="ISSUED",
                    bg="#b76e79",
                    fg="#fff",
                    font=("Calibri", 12, "bold"),
                )
                self.lac.place(x=8, y=75)
                self.label9 = Label(
                    self.fc1,
                    text="Fileno",
                    bg="#ffe8ec",
                    fg="black",
                    font=("Times New Roman", 11, "bold"),
                )
                self.label9.place(x=85, y=105)
                self.entry2 = Entry(
                    self.fc1,
                    width=25,
                    bd=4,
                    relief="groove",
                    font=("Calibri", 8, "bold"),
                )
                self.entry2.place(x=130, y=105)
                self.butto = Button(
                    self.fc1,
                    text="SEARCH",
                    bg="#b76e79",
                    fg="#fff",
                    width=8,
                    font=("Calibri", 12, "bold"),
                    command=self.srch,
                    relief="flat",
                    activebackground="black",
                    activeforeground="#b76e79",
                )
                self.butto.place(x=291, y=105)

                self.lac = Label(
                    self.edm,
                    text="",
                    bg="#b76e79",
                    fg="#fff",
                    font=("Calibri", 12, "bold"),
                )
                self.lac.place(x=8, y=105)
                self.label10 = Label(
                    self.fc1,
                    text="Fileno",
                    bg="#ffe8ec",
                    fg="black",
                    font=("Times New Roman", 11, "bold"),
                )
                self.label10.place(x=85, y=140)
                self.entry3 = Entry(
                    self.fc1,
                    width=25,
                    bd=4,
                    relief="groove",
                    font=("Calibri", 8, "bold"),
                )
                self.entry3.place(x=130, y=140)
                self.butto = Button(
                    self.fc1,
                    text="SEARCH",
                    bg="#b76e79",
                    fg="#fff",
                    width=8,
                    font=("Calibri", 12, "bold"),
                    command=self.srch,
                    relief="flat",
                    activebackground="black",
                    activeforeground="#b76e79",
                )
                self.butto.place(x=291, y=140)

                self.backbt = Button(
                    self.fc,
                    width=60,
                    bg="#ffe8ec",
                    activebackground="#ffe8ec",
                    bd=0,
                    relief="flat",
                    command=self.cur,
                )
                self.backbt.place(x=0, y=0)
                self.log = PhotoImage(file="bt1.png")
                self.backbt.config(image=self.log, compound=LEFT)
                self.small_log = self.log.subsample(2, 2)
                self.backbt.config(image=self.small_log)

            def srch(self):
                self.emp = self.entryl.get()
                cursor = dbfilesystem.cursor()
                cursor.execute("SELECT * FROM files WHERE fileno='" + self.emp + "'")
                dbfilesystem.commit()
                self.srval = cursor.fetchone()
                if self.srval != None:
                    self.top = Tk()
                    self.top.title("File System")

                    self.top.geometry("700x400+395+300")
                    self.top.resizable(0, 0)
                    self.top.configure(bg="#ffe8ec")

                    self.frm = Frame(self.top, bg="#b76e79", width=300, height=65)
                    self.frm.place(x=100, y=10)

                    self.mnlb = Label(
                        self.frm,
                        bg="#b76e79",
                        fg="#fff",
                        text="AVAILABLE",
                        font=("Calibri", 12, "bold"),
                    )
                    self.mnlb.place(x=9, y=5)

                    self.lb1 = Label(
                        self.top,
                        text="SECTION: ",
                        bg="#ffe8ec",
                        fg="black",
                        font=("Calibri", 12, "bold"),
                    )
                    self.lb1.place(x=85, y=70)
                    self.lb2 = Label(
                        self.top,
                        text=self.srval[1],
                        bg="#ffe8ec",
                        fg="black",
                        font=("Calibri", 12, "bold"),
                    )
                    self.lb2.place(x=165, y=70)

                    self.lb3 = Label(
                        self.top,
                        text="RFROM: ",
                        bg="#ffe8ec",
                        fg="black",
                        font=("Calibri", 12, "bold"),
                    )
                    self.lb3.place(x=85, y=110)
                    self.lb4 = Label(
                        self.top,
                        text=self.srval[2],
                        bg="#ffe8ec",
                        fg="black",
                        font=("Calibri", 12, "bold"),
                    )
                    self.lb4.place(x=165, y=110)

                    self.lb5 = Label(
                        self.top,
                        text="Rby: ",
                        bg="#ffe8ec",
                        fg="black",
                        font=("Calibri", 12, "bold"),
                    )
                    self.lb5.place(x=85, y=150)
                    self.lb6 = Label(
                        self.top,
                        text=self.srval[3],
                        bg="#ffe8ec",
                        fg="black",
                        font=("Calibri", 12, "bold"),
                    )
                    self.lb6.place(x=165, y=150)
                    self.lb7 = Label(
                        self.top,
                        text="DIGIT: ",
                        bg="#ffe8ec",
                        fg="black",
                        font=("Calibri", 12, "bold"),
                    )
                    self.lb7.place(x=85, y=190)
                    self.lb8 = Label(
                        self.top,
                        text=self.srval[4],
                        bg="#ffe8ec",
                        fg="black",
                        font=("Calibri", 12, "bold"),
                    )
                    self.lb8.place(x=165, y=190)
                    self.lb9 = Label(
                        self.top,
                        text="PROBLEM: ",
                        bg="#ffe8ec",
                        fg="black",
                        font=("Calibri", 12, "bold"),
                    )
                    self.lb9.place(x=85, y=230)
                    self.lb10 = Label(
                        self.top,
                        text=self.srval[5],
                        bg="#ffe8ec",
                        fg="black",
                        font=("Calibri", 12, "bold"),
                    )
                    self.lb10.place(x=165, y=230)
                    self.lb11 = Label(
                        self.top,
                        text="DATE: ",
                        bg="#ffe8ec",
                        fg="black",
                        font=("Calibri", 12, "bold"),
                    )
                    self.lb11.place(x=85, y=270)
                    self.lb12 = Label(
                        self.top,
                        text=self.srval[6],
                        bg="#ffe8ec",
                        fg="black",
                        font=("Calibri", 12, "bold"),
                    )
                    self.lb12.place(x=165, y=270)
                    self.entryl.delete(0, END)

                else:
                    messagebox.showwarning("Invalid Data", "This file does not exists!")
                    self.entryl.delete(0, END)

                self.emp = self.entry2.get()
                cursor = dbfilesystem.cursor()
                cursor.execute("SELECT * FROM issued WHERE fileno='" + self.emp + "'")
                dbfilesystem.commit()
                self.srval = cursor.fetchone()
                if self.srval != None:
                    self.top = Tk()
                    self.top.title("File System")

                    self.top.geometry("700x400+395+300")
                    self.top.resizable(0, 0)
                    self.top.configure(bg="#ffe8ec")

                    self.frm = Frame(self.top, bg="#b76e79", width=300, height=65)
                    self.frm.place(x=100, y=10)

                    self.mnlb = Label(
                        self.frm,
                        bg="#b76e79",
                        fg="#fff",
                        text="AVAILABLE",
                        font=("Calibri", 12, "bold"),
                    )
                    self.mnlb.place(x=9, y=5)

                    self.lb1 = Label(
                        self.top,
                        text="ISSUED TO: ",
                        bg="#ffe8ec",
                        fg="black",
                        font=("Calibri", 12, "bold"),
                    )
                    self.lb1.place(x=85, y=70)
                    self.lb2 = Label(
                        self.top,
                        text=self.srval[1],
                        bg="#ffe8ec",
                        fg="black",
                        font=("Calibri", 12, "bold"),
                    )
                    self.lb2.place(x=165, y=70)

                    self.lb3 = Label(
                        self.top,
                        text="ISSUE DATE: ",
                        bg="#ffe8ec",
                        fg="black",
                        font=("Calibri", 12, "bold"),
                    )
                    self.lb3.place(x=85, y=110)
                    self.lb4 = Label(
                        self.top,
                        text=self.srval[2],
                        bg="#ffe8ec",
                        fg="black",
                        font=("Calibri", 12, "bold"),
                    )
                    self.lb4.place(x=165, y=110)
                    self.entry2.delete(0, END)

                else:
                    messagebox.showwarning("Invalid Data", "This file does not exists!")
                    self.entry2.delete(0, END)

                self.emp = self.entry3.get()
                cursor = dbfilesystem.cursor()
                cursor.execute("SELECT * FROM outgoing WHERE fileno='" + self.emp + "'")
                dbfilesystem.commit()
                self.srval = cursor.fetchone()
                if self.srval != None:
                    self.top = Tk()
                    self.top.title("File System")

                    self.top.geometry("700x400+395+300")
                    self.top.resizable(0, 0)
                    self.top.configure(bg="#ffe8ec")

                    self.frm = Frame(self.top, bg="#b76e79", width=300, height=65)
                    self.frm.place(x=100, y=10)

                    self.mnlb = Label(
                        self.frm,
                        bg="#b76e79",
                        fg="#fff",
                        text="AVAILABLE",
                        font=("Calibri", 12, "bold"),
                    )
                    self.mnlb.place(x=9, y=5)

                    self.lb1 = Label(
                        self.top,
                        text="RBY: ",
                        bg="#ffe8ec",
                        fg="black",
                        font=("Calibri", 12, "bold"),
                    )
                    self.lb1.place(x=85, y=70)
                    self.lb2 = Label(
                        self.top,
                        text=self.srval[1],
                        bg="#ffe8ec",
                        fg="black",
                        font=("Calibri", 12, "bold"),
                    )
                    self.lb2.place(x=165, y=70)

                    self.lb3 = Label(
                        self.top,
                        text="SECTION: ",
                        bg="#ffe8ec",
                        fg="black",
                        font=("Calibri", 12, "bold"),
                    )
                    self.lb3.place(x=85, y=110)
                    self.lb4 = Label(
                        self.top,
                        text=self.srval[2],
                        bg="#ffe8ec",
                        fg="black",
                        font=("Calibri", 12, "bold"),
                    )
                    self.lb4.place(x=165, y=110)

                    self.lb5 = Label(
                        self.top,
                        text="DIGIT: ",
                        bg="#ffe8ec",
                        fg="black",
                        font=("Calibri", 12, "bold"),
                    )
                    self.lb5.place(x=85, y=150)
                    self.lb6 = Label(
                        self.top,
                        text=self.srval[3],
                        bg="#ffe8ec",
                        fg="black",
                        font=("Calibri", 12, "bold"),
                    )
                    self.lb6.place(x=165, y=150)
                    self.lb7 = Label(
                        self.top,
                        text="DATE: ",
                        bg="#ffe8ec",
                        fg="black",
                        font=("Calibri", 12, "bold"),
                    )
                    self.lb7.place(x=85, y=190)
                    self.lb8 = Label(
                        self.top,
                        text=self.srval[4],
                        bg="#ffe8ec",
                        fg="black",
                        font=("Calibri", 12, "bold"),
                    )
                    self.lb8.place(x=165, y=190)

                    self.entry3.delete(0, END)

                else:
                    messagebox.showwarning("Invalid Data", "This file does not exists!")
                    self.entry3.delete(0, END)

        _object = demt()
        _object.delmdata()

    def show(self):
        class test(main):
            def __init__(self):
                self.fc = Frame(root, bg="#ffe8ec", width=900, height=390)
                self.fc.place(x=0, y=110)
                self.popframe = Frame(self.fc, width=180, height=30, bg="#edb40d")
                self.popframe.place(x=360, y=0)
                self.lbn = Label(
                    self.popframe,
                    bg="#edb40d",
                    text="FILE INFORMATION",
                    fg="#fff",
                    font=("Calibri", 12, "bold"),
                )

                self.lbn.place(x=8, y=4)

                self.backbt = Button(
                    self.fc,
                    width=30,
                    bg="#ffe8ec",
                    activebackground="#ffe8ec",
                    bd=0,
                    relief="flat",
                    command=self.cur,
                )
                self.backbt.place(x=0, y=0)
                self.log = PhotoImage(file="bt1.png")
                self.backbt.config(image=self.log, compound=LEFT)
                self.small_log = self.log.subsample(3, 3)
                self.backbt.config(image=self.small_log)

                self.table_frame = Frame(self.fc, bg="#ffe8ec", bd=1, relief="flat")
                self.table_frame.place(x=0, y=30, width=900, height=360)

                self.scroll_x = Scrollbar(self.table_frame, orient=HORIZONTAL)
                self.scroll_y = Scrollbar(self.table_frame, orient=VERTICAL)
                self.book_table = ttk.Treeview(
                    self.table_frame,
                    columns=("fileno", "section", "rfrom", "rby", "location"),
                    xscrollcommand=self.scroll_x.set,
                    yscrollcommand=self.scroll_y.set,
                )
                self.scroll_x.pack(side=BOTTOM, fill=X)
                self.scroll_y.pack(side=RIGHT, fill=Y)
                self.scroll_x.config(command=self.book_table.xview)
                self.scroll_y.config(command=self.book_table.yview)

                self.book_table.heading("fileno", text="fileno")
                self.book_table.heading("section", text="section")
                self.book_table.heading("rfrom", text="rfrom")
                self.book_table.heading("rby", text="rby")
                self.book_table.heading("location", text="location")
                self.book_table["show"] = "headings"
                self.book_table.column("fileno", width=200)
                self.book_table.column("section", width=200)
                self.book_table.column("rfrom", width=200)
                self.book_table.column("rby", width=120)
                self.book_table.column("location", width=110)
                self.book_table.pack(fill=BOTH, expand=1)
                self.fetch_data()

            def fetch_data(self):
                cursor = dbfilesystem.cursor()
                cursor.execute("SELECT * FROM files")
                self.rows = cursor.fetchall()
                if len(self.rows) != 0:
                    for self.row in self.rows:
                        self.book_table.insert("", END, values=self.row)
                dbfilesystem.commit()

        oc = test()

    def showissued(self):
        class test(main):
            def __init__(self):
                self.fc = Frame(root, bg="#ffe8ec", width=900, height=390)
                self.fc.place(x=0, y=110)
                self.popframe = Frame(self.fc, width=180, height=30, bg="#edb40d")
                self.popframe.place(x=360, y=0)
                self.lbn = Label(
                    self.popframe,
                    bg="#edb40d",
                    text="FILE INFORMATION",
                    fg="#fff",
                    font=("Calibri", 12, "bold"),
                )

                self.lbn.place(x=8, y=4)

                self.backbt = Button(
                    self.fc,
                    width=30,
                    bg="#ffe8ec",
                    activebackground="#ffe8ec",
                    bd=0,
                    relief="flat",
                    command=self.cur,
                )
                self.backbt.place(x=0, y=0)
                self.log = PhotoImage(file="bt1.png")
                self.backbt.config(image=self.log, compound=LEFT)
                self.small_log = self.log.subsample(3, 3)
                self.backbt.config(image=self.small_log)

                self.table_frame = Frame(self.fc, bg="#ffe8ec", bd=1, relief="flat")
                self.table_frame.place(x=0, y=30, width=900, height=360)

                self.scroll_x = Scrollbar(self.table_frame, orient=HORIZONTAL)
                self.scroll_y = Scrollbar(self.table_frame, orient=VERTICAL)
                self.book_table = ttk.Treeview(
                    self.table_frame,
                    columns=("fileno", "issuedto", "issuedate"),
                    xscrollcommand=self.scroll_x.set,
                    yscrollcommand=self.scroll_y.set,
                )
                self.scroll_x.pack(side=BOTTOM, fill=X)
                self.scroll_y.pack(side=RIGHT, fill=Y)
                self.scroll_x.config(command=self.book_table.xview)
                self.scroll_y.config(command=self.book_table.yview)

                self.book_table.heading("fileno", text="fileno")
                self.book_table.heading("issuedto", text="issuedto")
                self.book_table.heading("issuedate", text="issuedate")
                self.book_table["show"] = "headings"
                self.book_table.column("fileno", width=200)
                self.book_table.column("issuedto", width=200)
                self.book_table.column("issuedate", width=200)
                self.book_table.pack(fill=BOTH, expand=1)
                self.fetch_data()

            def fetch_data(self):
                cursor = dbfilesystem.cursor()
                cursor.execute("SELECT * FROM issued")
                self.rows = cursor.fetchall()

                if len(self.rows) != 0:
                    for self.row in self.rows:
                        self.book_table.insert("", END, values=self.row)

            dbfilesystem.commit()

        oc = test()

    def mainclear(self):
        self.e1.delete(0, END)
        self.e2.delete(0, END)

    def code(self):
        self.fm = Frame(root, height=500, width=900, bg="white")
        self.fm.place(x=0, y=0)

        self.canvas = Canvas(self.fm, height=500, width=900, bg="#000000")
        self.canvas.place(x=0, y=0)

        self.photo = PhotoImage(file="bt1.png")
        self.canvas.create_image(0, 0, image=self.photo, anchor=NW)

        self.fm1 = Frame(
            self.canvas, height=260, width=300, bg="#000000", bd=3, relief="sunken"
        )
        self.fm1.place(x=300, y=120)

        self.b1 = Label(
            self.fm1, text="User ID", bg="black", font=("Arial", 10, "bold"), fg="white"
        )
        self.b1.place(x=20, y=42)

        self.e1 = Entry(
            self.fm1, width=22, font=("arial", 9, "bold"), bd=4, relief="groove"
        )
        self.e1.place(x=100, y=40)

        self.lb2 = Label(
            self.fm1,
            text="Password",
            bg="black",
            font=("Arial", 10, "bold"),
            fg="white",
        )
        self.lb2.place(x=20, y=102)

        self.e2 = Entry(
            self.fm1,
            width=22,
            show="*",
            font=("arial", 9, "bold"),
            bd=4,
            relief="groove",
        )
        self.e2.place(x=100, y=100)

        self.btn1 = Button(
            self.fm1,
            text="  Login",
            fg="black",
            bg="yellow",
            width=100,
            font=("Arial", 11, "bold"),
            activebackground="black",
            activeforeground="yellow",
            command=self.login,
            bd=3,
            relief="flat",
            cursor="hand2",
        )
        self.btn1.place(x=25, y=160)
        self.logo = PhotoImage(file="bt1.png")
        self.btn1.config(image=self.logo, compound=LEFT)
        self.small_logo = self.logo.subsample(1, 1)
        self.btn1.config(image=self.small_logo)

        self.btn2 = Button(
            self.fm1,
            text="  Clear",
            fg="black",
            bg="yellow",
            width=100,
            font=("Arial", 11, "bold"),
            activebackground="black",
            activeforeground="yellow",
            bd=3,
            relief="flat",
            cursor="hand2",
            command=self.mainclear,
        )
        self.btn2.place(x=155, y=160)
        self.log = PhotoImage(file="bt1.png")
        self.btn2.config(image=self.log, compound=LEFT)
        self.small_log = self.log.subsample(1, 1)
        self.btn2.config(image=self.small_log)

        self.forgot = Label(
            self.fm1,
            text="Forgot Password?",
            fg="White",
            bg="#000000",
            activeforeground="black",
            font=("cursive", 9, "bold"),
        )
        self.forgot.place(x=80, y=220)
        self.forgot.bind("<Button>", self.mouseClick)

        root.mainloop()

    def mouseClick(self, event):
        self.rog = Tk()
        self.rog.title("Change password")
        self.rog.geometry("400x300+300+210")
        self.rog.iconbitmap("filename.ico")
        self.rog.resizable(0, 0)
        self.rog.configure(bg="#000")

        self.framerog = Frame(self.rog, width=160, height=30, bg="#d6ed17")
        self.framerog.place(x=95, y=15)

        self.label = Label(
            self.framerog,
            text="SET NEW PASSWORD",
            bg="#d6ed17",
            fg="#606060",
            font=("Calibri", 12, "bold"),
        )
        self.label.place(x=5, y=4)

        self.user = Label(
            self.rog,
            text="User ID",
            bg="#000",
            fg="white",
            font=("Times New Roman", 11, "bold"),
        )
        self.user.place(x=40, y=95)

        self.user = Label(
            self.rog,
            text="New Password",
            bg="#000",
            fg="white",
            font=("Times New Roman", 11, "bold"),
        )
        self.user.place(x=40, y=170)

        self.ef1 = Entry(
            self.rog, width=24, font=("Calibri", 8, "bold"), bd=4, relief="groove"
        )
        self.ef1.place(x=170, y=95)

        self.ef2 = Entry(
            self.rog, width=24, font=("Calibri", 8, "bold"), bd=4, relief="groove"
        )
        self.ef2.place(x=170, y=170)

        self.btn1 = Button(
            self.rog,
            text="SUBMIT",
            fg="#606060",
            bg="#d6ed17",
            width=8,
            font=("Calibri", 12, "bold"),
            activebackground="black",
            activeforeground="#d6ed17",
            bd=3,
            relief="flat",
            cursor="hand2",
            command=self.chan_pas,
        )
        self.btn1.place(x=40, y=240)

    def chan_pas(self):
        self.a = self.ef1.get()
        self.b = self.ef2.get()
        import sqlite3

        conn = sqlite3.connect("admin.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM UserLogin WHERE UserID='" + self.a + "'")
        conn.commit()
        self.data = cursor.fetchone()

        if self.data != None:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE UserLogin SET Password='"
                + self.b
                + "' WHERE UserID='"
                + self.a
                + "'"
            )
            conn.commit()
            messagebox.showinfo("SUCCESSFUL", "Your Password is changed")
            self.rog.destroy()
        else:
            messagebox.showerror("ERROR", "UserID doesn't exist")
            self.rog.destroy()

        self.rog.mainloop()


obj = main()
obj.code()


from tkinter import *
from tkinter import ttk

# main window
root = Tk()
root.title("Library Management System")
root.iconbitmap("")
root.geometry("900x500+50+100")
root.resizable(0, 0)


class main:
    def code(self):
        self.fm = Frame(root, height=500, width=900, bg="white")
        self.fm.place(x=0, y=0)

        self.canvas = Canvas(self.fm, height=500, width=900, bg="#000000")
        self.canvas.place(x=0, y=0)

        self.photo = PhotoImage(file="bt1.png")
        self.canvas.create_image(0, 0, image=self.photo, anchor=NW)

        self.fm1 = Frame(
            self.canvas, height=260, width=300, bg="#000000", bd=3, relief="sunken"
        )
        self.fm1.place(x=300, y=120)

        # UserID Label
        self.b1 = Label(
            self.fm1, text="User ID", bg="black", font=("Arial", 10, "bold"), fg="white"
        )
        self.b1.place(x=20, y=42)

        self.e1 = Entry(
            self.fm1, width=22, font=("arial", 9, "bold"), bd=4, relief="groove"
        )
        self.e1.place(x=100, y=40)

        # Password Label
        self.lb2 = Label(
            self.fm1,
            text="Password",
            bg="black",
            font=("Arial", 10, "bold"),
            fg="white",
        )
        self.lb2.place(x=20, y=102)

        self.e2 = Entry(
            self.fm1,
            width=22,
            show="*",
            font=("arial", 9, "bold"),
            bd=4,
            relief="groove",
        )
        self.e2.place(x=100, y=100)

        # Login Button
        self.btn1 = Button(
            self.fm1,
            text="  Login",
            fg="black",
            bg="yellow",
            width=100,
            font=("Arial", 11, "bold"),
            activebackground="black",
            activeforeground="yellow",
            command=self.login,
            bd=3,
            relief="flat",
            cursor="hand2",
        )
        self.btn1.place(x=25, y=160)
        self.logo = PhotoImage(file="bt1.png")
        self.btn1.config(image=self.logo, compound=LEFT)
        self.small_logo = self.logo.subsample(1, 1)
        self.btn1.config(image=self.small_logo)

        # Clear Button
        self.btn2 = Button(
            self.fm1,
            text="  Clear",
            fg="black",
            bg="yellow",
            width=100,
            font=("Arial", 11, "bold"),
            activebackground="black",
            activeforeground="yellow",
            bd=3,
            relief="flat",
            cursor="hand2",
            command=self.mainclear,
        )
        self.btn2.place(x=155, y=160)
        self.log = PhotoImage(file="bt1.png")
        self.btn2.config(image=self.log, compound=LEFT)
        self.small_log = self.log.subsample(1, 1)
        self.btn2.config(image=self.small_log)

        # Forgot Password Clickable Label
        self.forgot = Label(
            self.fm1,
            text="Forgot Password?",
            fg="White",
            bg="#000000",
            activeforeground="black",
            font=("cursive", 9, "bold"),
        )
        self.forgot.place(x=80, y=220)
        self.forgot.bind("<Button>", self.mouseClick)

        root.mainloop()

    def login(self):
        pass

    def mainclear(self):
        pass

    def mouseClick(self):
        pass


# object for calling the function
obj = main()
obj.code()


class main:
    def mainclear(self):
        self.e1.delete(0, END)
        self.e2.delete(0, END)


class main:
    def mouseClick(self, event):
        self.rog = Tk()
        self.rog.title("Change password")
        self.rog.geometry("400x300+300+210")
        self.rog.iconbitmap("")
        self.rog.resizable(0, 0)
        self.rog.configure(bg="#000")

        self.framerog = Frame(self.rog, width=160, height=30, bg="#d6ed17")
        self.framerog.place(x=95, y=15)

        self.label = Label(
            self.framerog,
            text="SET NEW PASSWORD",
            bg="#d6ed17",
            fg="#606060",
            font=("Calibri", 12, "bold"),
        )
        self.label.place(x=5, y=4)

        # User ID
        self.user = Label(
            self.rog,
            text="User ID",
            bg="#000",
            fg="white",
            font=("Times New Roman", 11, "bold"),
        )
        self.user.place(x=40, y=95)

        # New Password
        self.user = Label(
            self.rog,
            text="New Password",
            bg="#000",
            fg="white",
            font=("Times New Roman", 11, "bold"),
        )
        self.user.place(x=40, y=170)

        self.ef1 = Entry(
            self.rog, width=24, font=("Calibri", 8, "bold"), bd=4, relief="groove"
        )
        self.ef1.place(x=170, y=95)

        self.ef2 = Entry(
            self.rog, width=24, font=("Calibri", 8, "bold"), bd=4, relief="groove"
        )
        self.ef2.place(x=170, y=170)

        # Submit Button
        self.btn1 = Button(
            self.rog,
            text="SUBMIT",
            fg="#606060",
            bg="#d6ed17",
            width=8,
            font=("Calibri", 12, "bold"),
            activebackground="black",
            activeforeground="#d6ed17",
            bd=3,
            relief="flat",
            cursor="hand2",
            command=self.chan_pas,
        )
        self.btn1.place(x=40, y=240)

    def chan_pas(self):
        self.a = self.ef1.get()
        self.b = self.ef2.get()

        import sqlite3

        conn = sqlite3.connect("admin.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM UserLogin WHERE UserID='" + self.a + "'")
        conn.commit()
        self.data = cursor.fetchone()

        if self.data != None:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE UserLogin SET Password='"
                + self.b
                + "' WHERE UserID='"
                + self.a
                + "'"
            )
            conn.commit()
            messagebox.showinfo("SUCCESSFUL", "Your Password is changed")
            self.rog.destroy()
        else:
            messagebox.showerror("ERROR", "UserID doesn't exist")
            self.rog.destroy()

        self.rog.mainloop()


class main:
    def login(self):
        self.var1 = self.e1.get()
        self.var2 = self.e2.get()

        cursor = dbfilesystem.cursor()
        cursor.execute(
            "SELECT * FROM UserLogin WHERE UserID='"
            + self.var1
            + "' and Password='"
            + self.var2
            + "'"
        )
        dbfilesystem.commit()
        self.ab = cursor.fetchone()

        if self.ab != None:
            self.under_fm = Frame(root, height=500, width=900, bg="#fff")
            self.under_fm.place(x=0, y=0)

            self.fm2 = Frame(root, bg="#012727", height=80, width=900)
            self.fm2.place(x=0, y=0)

            self.lbb = Label(self.fm2, bg="#012727")
            self.lbb.place(x=15, y=5)
            self.ig = PhotoImage(file="bt1.png")
            self.lbb.config(image=self.ig)

            self.lb3 = Label(
                self.fm2,
                text="DASHBOARD",
                fg="White",
                bg="#012727",
                font=("times new roman", 30, "bold"),
            )
            self.lb3.place(x=325, y=17)

            # Name of the logged in admin
            self.name = Label(
                root,
                text="Name : ",
                bg="#fff",
                fg="black",
                font=("Calibri", 12, "bold"),
            )
            self.name.place(x=5, y=83)
            self.name1 = Label(
                root,
                text=self.ab[0],
                fg="black",
                bg="#fff",
                font=("Calibri", 12, "bold"),
            )
            self.name1.place(x=60, y=83)

            # Display Date
            self.today = date.today()
            self.dat = Label(
                root,
                text="Date : ",
                bg="#fff",
                fg="black",
                font=("Calibri", 12, "bold"),
            )
            self.dat.place(x=750, y=83)
            self.dat2 = Label(
                root,
                text=self.today,
                bg="#fff",
                fg="black",
                font=("Calibri", 12, "bold"),
            )
            self.dat2.place(x=800, y=83)

            # For Head part
            self.cur()

        else:
            messagebox.showerror("Library System", "Your ID or Password is invalid!")


class main:
    def cur(self):
        self.fm3 = Frame(root, bg="#fff", width=900, height=390)
        self.fm3.place(x=0, y=110)

        def clock():
            h = str(time.strftime("%H"))
            m = str(time.strftime("%M"))
            s = str(time.strftime("%S"))

            if int(h) >= 12 and int(m) >= 0:
                self.lb7_hr.config(text="PM")

            # if int(h) > 12:
            # h = str(int(h) // 12)

            self.lb1_hr.config(text=h)
            self.lb3_hr.config(text=m)
            self.lb5_hr.config(text=s)

            self.lb1_hr.after(200, clock)

        self.lb1_hr = Label(
            self.fm3,
            text="12",
            font=("times new roman", 20, "bold"),
            bg="#581845",
            fg="white",
        )
        self.lb1_hr.place(x=607, y=0, width=60, height=30)

        self.lb3_hr = Label(
            self.fm3,
            text="05",
            font=("times new roman", 20, "bold"),
            bg="#581845",
            fg="white",
        )
        self.lb3_hr.place(x=677, y=0, width=60, height=30)

        self.lb5_hr = Label(
            self.fm3,
            text="37",
            font=("times new roman", 20, "bold"),
            bg="#581845",
            fg="white",
        )
        self.lb5_hr.place(x=747, y=0, width=60, height=30)

        self.lb7_hr = Label(
            self.fm3,
            text="AM",
            font=("times new roman", 17, "bold"),
            bg="#581845",
            fg="white",
        )
        self.lb7_hr.place(x=817, y=0, width=60, height=30)

        clock()

        # right side image
        self.canvas8 = Canvas(self.fm3, bg="black", width=400, height=300)
        self.canvas8.place(x=475, y=40)
        self.photo9 = PhotoImage(file="bt1.png")
        self.canvas8.create_image(0, 0, image=self.photo9, anchor=NW)

        self.develop = Label(
            self.fm3,
            text="Developed By - <YourName>",
            bg="#fff",
            fg="#d7837f",
            font=("Candara", 12, "bold"),
        )
        self.develop.place(x=732, y=350)

        # AddButton

        self.bt1 = Button(
            self.fm3,
            text="  Add files",
            fg="#fff",
            bg="#581845",
            font=("Candara", 15, "bold"),
            width=170,
            height=0,
            bd=7,
            relief="flat",
            command=self.addbook,
            cursor="hand2",
            activebackground="black",
            activeforeground="#581845",
        )
        self.bt1.place(x=40, y=40)
        self.logo = PhotoImage(file="bt1.png")
        self.bt1.config(image=self.logo, compound=LEFT)
        self.small_logo = self.logo.subsample(1, 1)
        self.bt1.config(image=self.small_logo)

        # IssueButton

        self.bt2 = Button(
            self.fm3,
            text="  Issue files",
            fg="#fff",
            bg="#581845",
            font=("Candara", 15, "bold"),
            width=170,
            height=0,
            bd=7,
            relief="flat",
            command=self.issue,
            cursor="hand2",
            activebackground="black",
            activeforeground="#581845",
        )
        self.bt2.place(x=250, y=40)
        self.log = PhotoImage(file="bt2.png")
        self.bt2.config(image=self.log, compound=LEFT)
        self.small_log = self.log.subsample(1, 1)
        self.bt2.config(image=self.small_log)

        # DeleteButton

        self.bt5 = Button(
            self.fm3,
            text=" Delete files",
            fg="#fff",
            bg="#581845",
            font=("Candara", 15, "bold"),
            width=170,
            height=0,
            bd=7,
            relief="flat",
            cursor="hand2",
            command=self.delete,
            activebackground="black",
            activeforeground="#581845",
        )
        self.bt5.place(x=40, y=200)
        self.log5 = PhotoImage(file="bt5.png")
        self.bt5.config(image=self.log5, compound=LEFT)
        self.small_log5 = self.log5.subsample(1, 1)
        self.bt5.config(image=self.small_log5)

        # ShowButton

        self.bt6 = Button(
            self.fm3,
            text=" Show files",
            fg="#fff",
            bg="#581845",
            font=("Candara", 15, "bold"),
            width=170,
            height=0,
            bd=7,
            relief="flat",
            cursor="hand2",
            command=self.show,
            activebackground="black",
            activeforeground="#581845",
        )
        self.bt6.place(x=40, y=280)
        self.log6 = PhotoImage(file="bt6.png")
        self.bt6.config(image=self.log6, compound=LEFT)
        self.small_log6 = self.log6.subsample(1, 1)
        self.bt6.config(image=self.small_log6)

        # SearchButton

        self.bt7 = Button(
            self.fm3,
            text="  Search files",
            fg="#fff",
            bg="#581845",
            font=("Candara", 15, "bold"),
            width=170,
            height=0,
            bd=7,
            relief="flat",
            cursor="hand2",
            command=self.search,
            activebackground="black",
            activeforeground="#581845",
        )
        self.bt7.place(x=250, y=200)
        self.log7 = PhotoImage(file="bt7.png")
        self.bt7.config(image=self.log7, compound=LEFT)
        self.small_log7 = self.log7.subsample(1, 1)
        self.bt7.config(image=self.small_log7)

        # ExitButton
        try:
            self.bt8 = Button(
                self.fm3,
                text="  Log Out",
                fg="#fff",
                bg="#581845",
                font=("Candara", 15, "bold"),
                width=170,
                height=0,
                bd=7,
                relief="flat",
                cursor="hand2",
                command=self.code,
                activebackground="black",
                activeforeground="#581845",
            )
            self.bt8.place(x=250, y=280)
            self.log8 = PhotoImage(file="bt8.png")
            self.bt8.config(image=self.log8, compound=LEFT)
            self.small_log8 = self.log8.subsample(1, 1)
            self.bt8.config(image=self.small_log8)

        except:
            self.bt9 = ttk.Button(
                self.fm3,
                text="Name",
                bg="#a40000",
                font=("Candara", 15, "bold"),
                width=150,
                height=0,
            )
            self.bt9.place(x=40, y=350)
            self.log9 = PhotoImage(file="bt8.png")
            self.bt9.config(image=self.log9, compound=LEFT)
            self.small_log9 = self.log9.subsample(3, 3)
            self.bt9.config(image=self.small_log9)

    def receive(self):
        pass

    def issue(self):
        pass

    def dispatch(self):
        pass

    def show(self):
        pass

    def search(self):
        pass

    def showissued(self):
        pass


class main:
    def receive(self):
        class temp(main):
            def book(self):
                self.fm = Frame(root, bg="#ffe8ec", width=900, height=390)
                self.fm.place(x=0, y=110)

                self.fm1 = Frame(
                    self.fm, bg="#ffe8ec", width=500, height=360, bd=5, relief="flat"
                )
                self.fm1.place(x=200, y=15)

                # Back Button (clickable image)
                self.backbt = Button(
                    self.fm,
                    width=60,
                    bg="#ffe8ec",
                    bd=0,
                    relief="flat",
                    command=self.cur,
                    activeforeground="black",
                    activebackground="#ffe8ec",
                )
                self.backbt.place(x=2, y=7)
                self.log = PhotoImage(file="bt1.png")
                self.backbt.config(image=self.log, compound=LEFT)
                self.small_log = self.log.subsample(2, 2)
                self.backbt.config(image=self.small_log)

                self.fll = Frame(self.fm1, width=150, height=40, bg="#ff6690")
                self.fll.place(x=150, y=15)
                self.ll = Label(
                    self.fll,
                    text="receive",
                    fg="#fff",
                    bg="#ff6690",
                    font=("Canara", 12, "bold"),
                    width=15,
                )
                self.ll.place(x=0, y=8)

                # ID
                self.lb = Label(
                    self.fm1,
                    text="fileno",
                    fg="black",
                    bg="#ffe8ec",
                    font=("times new roman", 11, "bold"),
                )
                self.lb.place(x=70, y=90)

                # section
                self.lb2 = Label(
                    self.fm1,
                    text="section",
                    fg="black",
                    bg="#ffe8ec",
                    font=("times new roman", 11, "bold"),
                )
                self.lb2.place(x=70, y=130)

                # rfrom
                self.lb3 = Label(
                    self.fm1,
                    text="rfrom",
                    fg="black",
                    bg="#ffe8ec",
                    font=("times new roman", 11, "bold"),
                )
                self.lb3.place(x=70, y=170)

                # rby
                self.lb4 = Label(
                    self.fm1,
                    text="rby",
                    fg="black",
                    bg="#ffe8ec",
                    font=("times new roman", 11, "bold"),
                )
                self.lb4.place(x=70, y=210)

                # Entries
                self.ee1 = Entry(
                    self.fm1,
                    width=25,
                    bd=4,
                    relief="groove",
                    font=("Calibri", 11, "bold"),
                )
                self.ee1.place(x=180, y=88)

                self.ee2 = Entry(
                    self.fm1,
                    width=25,
                    bd=4,
                    relief="groove",
                    font=("Calibri", 11, "bold"),
                )
                self.ee2.place(x=180, y=130)

                self.ee3 = Entry(
                    self.fm1,
                    width=25,
                    bd=4,
                    relief="groove",
                    font=("Calibri", 11, "bold"),
                )
                self.ee3.place(x=180, y=170)

                self.ee4 = Entry(
                    self.fm1,
                    width=25,
                    bd=4,
                    relief="groove",
                    font=("Calibri", 11, "bold"),
                )
                self.ee4.place(x=180, y=210)

                self.ee5 = Entry(
                    self.fm1,
                    width=25,
                    bd=4,
                    relief="groove",
                    font=("Calibri", 11, "bold"),
                )
                self.ee5.place(x=180, y=250)

                # Submit Button
                self.bt = Button(
                    self.fm1,
                    text="SUBMIT",
                    width=8,
                    fg="white",
                    bg="#ff6690",
                    font=("Canara", 12, "bold"),
                    bd=3,
                    relief="flat",
                    command=self.submit1,
                    activebackground="black",
                    activeforeground="#ff6690",
                )
                self.bt.place(x=70, y=300)

            # Submit Button function
            def submit1(self):
                try:
                    self.fn = self.ee1.get()
                    self.sc = self.ee2.get()
                    self.rf = self.ee3.get()
                    self.rb = self.ee4.get()
                    self.loc = self.ee5.get()

                    if self.fn and self.sc and self.rf and self.rb and self.loc != None:
                        cursor = dbfilesystem.cursor()
                        cursor.execute(
                            "INSERT INTO files(fileno,section,rfrom,rby, location) values(?,?,?,?,?)",
                            (self.fn, self.sc, self.rf, self.rb, self.loc),
                        )
                        dbfilesystem.commit()

                        messagebox.showinfo(
                            "Success", "file has been added to the library succesfully"
                        )

                        # clear the entries after succesful operation
                        self.clear()
                    else:
                        messagebox.showerror("Error", "Enter Valid Details")

                except Exception as e:
                    messagebox.showerror("Error", "Enter Valid Details")

            def clear(self):
                self.ee1.delete(0, END)
                self.ee2.delete(0, END)
                self.ee3.delete(0, END)
                self.ee4.delete(0, END)
                self.ee5.delete(0, END)

        # create object to invoke function
        obj = temp()
        obj.book()


def issue(self):
    class temp(main):
        def file(self):
            self.fm = Frame(root, bg="#ffe8ec", width=900, height=390)
            self.fm.place(x=0, y=110)

            self.fm1 = Frame(
                self.fm, bg="#ffe8ec", width=500, height=360, bd=5, relief="flat"
            )
            self.fm1.place(x=200, y=15)

            self.backbt = Button(
                self.fm,
                width=60,
                bg="#ffe8ec",
                bd=0,
                relief="flat",
                command=self.cur,
                activeforeground="black",
                activebackground="#ffe8ec",
            )
            self.backbt.place(x=2, y=7)
            self.log = PhotoImage(file="bt1.png")
            self.backbt.config(image=self.log, compound=LEFT)
            self.small_log = self.log.subsample(2, 2)
            self.backbt.config(image=self.small_log)

            self.fll = Frame(self.fm1, width=150, height=40, bg="#ff6690")
            self.fll.place(x=150, y=15)
            self.ll = Label(
                self.fll,
                text="ISSUE FILES",
                fg="#fff",
                bg="#ff6690",
                font=("Canara", 12, "bold"),
                width=15,
            )
            # self.ll.config(height=5)
            self.ll.place(x=0, y=8)

            self.lb = Label(
                self.fm1,
                text="FILENO",
                fg="black",
                bg="#ffe8ec",
                font=("times new roman", 11, "bold"),
            )
            self.lb.place(x=70, y=90)
            self.lb2 = Label(
                self.fm1,
                text="ISSUED TO",
                fg="black",
                bg="#ffe8ec",
                font=("times new roman", 11, "bold"),
            )
            self.lb2.place(x=70, y=130)
            self.lb3 = Label(
                self.fm1,
                text="ISSUE DATE",
                fg="black",
                bg="#ffe8ec",
                font=("times new roman", 11, "bold"),
            )
            self.lb3.place(x=70, y=170)

            self.ee1 = Entry(
                self.fm1,
                width=25,
                bd=4,
                relief="groove",
                font=("Calibri", 11, "bold"),
            )
            self.ee1.place(x=180, y=88)
            self.ee2 = Entry(
                self.fm1,
                width=25,
                bd=4,
                relief="groove",
                font=("Calibri", 11, "bold"),
            )
            self.ee2.place(x=180, y=130)
            self.ee3 = Entry(
                self.fm1,
                width=25,
                bd=4,
                relief="groove",
                font=("Calibri", 11, "bold"),
            )
            self.ee3.place(x=180, y=170)

            self.bt = Button(
                self.fm1,
                text="SUBMIT",
                width=8,
                fg="white",
                bg="#ff6690",
                font=("Canara", 12, "bold"),
                bd=3,
                relief="flat",
                command=self.submit1,
                activebackground="black",
                activeforeground="#ff6690",
            )
            self.bt.place(x=70, y=300)

        def submit1(self):
            try:
                self.fn = self.ee1.get()
                self.ist = self.ee2.get()
                self.isd = self.ee3.get()

                if self.fn and self.ist and self.isd:
                    cursor = dbfilesystem.cursor()
                    cursor.execute(
                        "INSERT INTO issued(fileno,issuedto,issuedate) values(?,?,?)",
                        (
                            self.fn,
                            self.ist,
                            self.isd,
                        ),
                    )
                    dbfilesystem.commit()
                    messagebox.showinfo("Success", "file has been issued succesfully")
                    self.clear()
                else:
                    messagebox.showerror("Error", "Enter Valid Details")
            except Exception as e:
                messagebox.showerror("Error", "Enter Valid Details")

        def clear(self):
            self.ee1.delete(0, END)
            self.ee2.delete(0, END)
            self.ee3.delete(0, END)

    obj = temp()
    obj.file()


def showissued(self):
    class test(main):
        def __init__(self):
            self.fc = Frame(root, bg="#ffe8ec", width=900, height=390)
            self.fc.place(x=0, y=110)
            self.popframe = Frame(self.fc, width=180, height=30, bg="#edb40d")
            self.popframe.place(x=360, y=0)
            self.lbn = Label(
                self.popframe,
                bg="#edb40d",
                text="FILE INFORMATION",
                fg="#fff",
                font=("Calibri", 12, "bold"),
            )

            self.lbn.place(x=8, y=4)

            self.backbt = Button(
                self.fc,
                width=30,
                bg="#ffe8ec",
                activebackground="#ffe8ec",
                bd=0,
                relief="flat",
                command=self.cur,
            )
            self.backbt.place(x=0, y=0)
            self.log = PhotoImage(file="bt1.png")
            self.backbt.config(image=self.log, compound=LEFT)
            self.small_log = self.log.subsample(3, 3)
            self.backbt.config(image=self.small_log)

            self.table_frame = Frame(self.fc, bg="#ffe8ec", bd=1, relief="flat")
            self.table_frame.place(x=0, y=30, width=900, height=360)

            self.scroll_x = Scrollbar(self.table_frame, orient=HORIZONTAL)
            self.scroll_y = Scrollbar(self.table_frame, orient=VERTICAL)
            self.book_table = ttk.Treeview(
                self.table_frame,
                columns=("fileno", "issuedto", "issuedate"),
                xscrollcommand=self.scroll_x.set,
                yscrollcommand=self.scroll_y.set,
            )
            self.scroll_x.pack(side=BOTTOM, fill=X)
            self.scroll_y.pack(side=RIGHT, fill=Y)
            self.scroll_x.config(command=self.book_table.xview)
            self.scroll_y.config(command=self.book_table.yview)

            self.book_table.heading("fileno", text="fileno")
            self.book_table.heading("issuedto", text="issuedto")
            self.book_table.heading("issuedate", text="issuedate")
            self.book_table["show"] = "headings"
            self.book_table.column("fileno", width=200)
            self.book_table.column("issuedto", width=200)
            self.book_table.column("issuedate", width=200)
            self.book_table.pack(fill=BOTH, expand=1)
            self.fetch_data()

        def fetch_data(self):
            cursor = dbfilesystem.cursor()
            cursor.execute("SELECT * FROM issued")
            self.rows = cursor.fetchall()
            if len(self.rows) != 0:
                for self.row in self.rows:
                    self.book_table.insert("", END, values=self.row)
            dbfilesystem.commit()

    oc = test()

    def mainclear(self):
        self.e1.delete(0, END)
        self.e2.delete(0, END)

    def code(self):
        self.fm = Frame(root, height=500, width=900, bg="white")
        self.fm.place(x=0, y=0)

    self.canvas = Canvas(self.fm, height=500, width=900, bg="#000000")
    self.canvas.place(x=0, y=0)

    self.photo = PhotoImage(file="bt1.png")

    self.canvas.create_image(0, 0, image=self.photo, anchor=NW)

    self.fm1 = Frame(
        self.canvas, height=260, width=300, bg="#000000", bd=3, relief="sunken"
    )
    self.fm1.place(x=300, y=120)

    self.b1 = Label(
        self.fm1, text="User ID", bg="black", font=("Arial", 10, "bold"), fg="white"
    )
    self.b1.place(x=20, y=42)

    self.e1 = Entry(
        self.fm1, width=22, font=("arial", 9, "bold"), bd=4, relief="groove"
    )
    self.e1.place(x=100, y=40)

    self.lb2 = Label(
        self.fm1,
        text="Password",
        bg="black",
        font=("Arial", 10, "bold"),
        fg="white",
    )
    self.lb2.place(x=20, y=102)

    self.e2 = Entry(
        self.fm1,
        width=22,
        show="*",
        font=("arial", 9, "bold"),
        bd=4,
        relief="groove",
    )
    self.e2.place(x=100, y=100)

    self.btn1 = Button(
        self.fm1,
        text="  Login",
        fg="black",
        bg="yellow",
        width=100,
        font=("Arial", 11, "bold"),
        activebackground="black",
        activeforeground="yellow",
        command=self.login,
        bd=3,
        relief="flat",
        cursor="hand2",
    )
    self.btn1.place(x=25, y=160)
    self.logo = PhotoImage(file="bt1.png")

    self.btn1.config(image=self.logo, compound=LEFT)
    self.small_logo = self.logo.subsample(1, 1)
    self.btn1.config(image=self.small_logo)

    self.btn2 = Button(
        self.fm1,
        text="  Clear",
        fg="black",
        bg="yellow",
        width=100,
        font=("Arial", 11, "bold"),
        activebackground="black",
        activeforeground="yellow",
        bd=3,
        relief="flat",
        cursor="hand2",
        command=self.mainclear,
    )
    self.btn2.place(x=155, y=160)
    self.log = PhotoImage(file="bt1.png")

    self.btn2.config(image=self.log, compound=LEFT)
    self.small_log = self.log.subsample(1, 1)
    self.btn2.config(image=self.small_log)

    self.forgot = Label(
        self.fm1,
        text="Forgot Password?",
        fg="White",
        bg="#000000",
        activeforeground="black",
        font=("cursive", 9, "bold"),
    )
    self.forgot.place(x=80, y=220)
    self.forgot.bind("<Button>", self.mouseClick)

    root.mainloop()

    def mouseClick(self, event):
        self.rog = Tk()

    self.rog.title("Change password")
    self.rog.geometry("400x300+300+210")
    self.rog.iconbitmap("")
    self.rog.resizable(0, 0)
    self.rog.configure(bg="#000")

    self.framerog = Frame(self.rog, width=160, height=30, bg="#d6ed17")
    self.framerog.place(x=95, y=15)

    self.label = Label(
        self.framerog,
        text="SET NEW PASSWORD",
        bg="#d6ed17",
        fg="#606060",
        font=("Calibri", 12, "bold"),
    )
    self.label.place(x=5, y=4)

    self.user = Label(
        self.rog,
        text="User ID",
        bg="#000",
        fg="white",
        font=("Times New Roman", 11, "bold"),
    )
    self.user.place(x=40, y=95)

    self.user = Label(
        self.rog,
        text="New Password",
        bg="#000",
        fg="white",
        font=("Times New Roman", 11, "bold"),
    )
    self.user.place(x=40, y=170)

    self.ef1 = Entry(
        self.rog, width=24, font=("Calibri", 8, "bold"), bd=4, relief="groove"
    )
    self.ef1.place(x=170, y=95)

    self.ef2 = Entry(
        self.rog, width=24, font=("Calibri", 8, "bold"), bd=4, relief="groove"
    )
    self.ef2.place(x=170, y=170)

    self.btn1 = Button(
        self.rog,
        text="SUBMIT",
        fg="#606060",
        bg="#d6ed17",
        width=8,
        font=("Calibri", 12, "bold"),
        activebackground="black",
        activeforeground="#d6ed17",
        bd=3,
        relief="flat",
        cursor="hand2",
        command=self.chan_pas,
    )
    self.btn1.place(x=40, y=240)

    def chan_pas(self):
        self.a = self.ef1.get()

    self.b = self.ef2.get()
    import sqlite3

    conn = sqlite3.connect("admin.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM UserLogin WHERE UserID='" + self.a + "'")
    conn.commit()
    self.data = cursor.fetchone()

    if self.data != None:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE UserLogin SET Password='"
            + self.b
            + "' WHERE UserID='"
            + self.a
            + "'"
        )
        conn.commit()
        messagebox.showinfo("SUCCESSFUL", "Your Password is changed")
        self.rog.destroy()
    else:
        messagebox.showerror("ERROR", "UserID doesn't exist")
        self.rog.destroy()

    self.rog.mainloop()


obj = main()
obj.login()


class main:
    def edit(self):
        class editing(main):
            def edfiles(self):
                self.ffm = Frame(root, bg="#ffe8ec", width=900, height=390)
                self.ffm.place(x=0, y=110)

                self.fm1 = Frame(
                    self.ffm, bg="#ffe8ec", width=500, height=200, bd=5, relief="flat"
                )
                self.fm1.place(x=150, y=30)

                self.ed = Frame(
                    self.fm1, bg="#1c1c1b", bd=0, relief="flat", width=160, height=35
                )
                self.ed.place(x=170, y=0)

                self.lab = Label(
                    self.ed,
                    text="EDIT FILE DETAILS",
                    bg="#1c1c1b",
                    fg="#ce4a7e",
                    font=("Calibri", 12, "bold"),
                )
                self.lab.place(x=9, y=5)

                # fileno
                self.label3 = Label(
                    self.fm1,
                    text="fileno",
                    bg="#ffe8ec",
                    fg="black",
                    font=("Times New Roman", 11, "bold"),
                )
                self.label3.place(x=85, y=65)
                self.entry = Entry(
                    self.fm1,
                    width=30,
                    bd=4,
                    relief="groove",
                    font=("Calibri", 8, "bold"),
                )
                self.entry.place(x=188, y=65)

                # Search Button
                self.button7 = Button(
                    self.fm1,
                    text="SEARCH",
                    bg="#1c1c1b",
                    fg="#ce4a7e",
                    width=8,
                    font=("Calibri", 12, "bold"),
                    command=self.searchedit,
                    relief="flat",
                    activebackground="#ce4a7e",
                    activeforeground="#1c1c1b",
                )
                self.button7.place(x=85, y=125)

                # Back Button (clickable image)
                self.backbt = Button(
                    self.ffm,
                    width=60,
                    bg="#ffe8ec",
                    activebackground="#ffe8ec",
                    bd=0,
                    relief="flat",
                    command=self.cur,
                )
                self.backbt.place(x=0, y=0)
                self.log = PhotoImage(file="bt1.png")
                self.backbt.config(image=self.log, compound=LEFT)
                self.small_log = self.log.subsample(2, 2)
                self.backbt.config(image=self.small_log)

            def searchedit(self):
                self.datas = self.entry.get()
                cursor = dbfilesystem.cursor()
                cursor.execute(
                    "SELECT * FROM files WHERE fileno = '" + self.datas + "'"
                )
                dbfilesystem.commit()
                self.val = cursor.fetchone()
                if self.val != None:
                    self.edcat = Tk()
                    self.edcat.title("Library System")
                    self.edcat.geometry("300x360+600+230")
                    self.edcat.configure(bg="#ffe8ec")
                    self.edcat.iconbitmap("")

                    self.fc = Frame(self.edcat, bg="#1c1c1b", width=90, height=30)
                    self.fc.place(x=80, y=10)

                    self.lab = Label(
                        self.fc,
                        bg="#1c1c1b",
                        fg="#ce4a7e",
                        text="EDIT BOOK",
                        font=("Calibri", 12, "bold"),
                    )
                    self.lab.place(x=3, y=3)

                    # fileno
                    self.labid = Label(
                        self.edcat,
                        bg="#ffe8ec",
                        fg="black",
                        text="fileno:",
                        font=("Calibri", 12, "bold"),
                    )
                    self.labid.place(x=30, y=60)

                    # section
                    self.labti = Label(
                        self.edcat,
                        bg="#ffe8ec",
                        fg="black",
                        text="section:",
                        font=("Calibri", 12, "bold"),
                    )
                    self.labti.place(x=30, y=100)

                    # rfrom
                    self.labaut = Label(
                        self.edcat,
                        bg="#ffe8ec",
                        fg="black",
                        text="rfrom:",
                        font=("Calibri", 12, "bold"),
                    )
                    self.labaut.place(x=30, y=140)

                    # rby
                    self.labed = Label(
                        self.edcat,
                        bg="#ffe8ec",
                        fg="black",
                        text="rby:",
                        font=("Calibri", 12, "bold"),
                    )
                    self.labed.place(x=30, y=180)

                    self.en1 = Entry(
                        self.edcat,
                        width=20,
                        bd=4,
                        relief="groove",
                        font=("Times New Roman", 9, "bold"),
                    )
                    self.en1.place(x=110, y=60)

                    self.en2 = Entry(
                        self.edcat,
                        width=20,
                        bd=4,
                        relief="groove",
                        font=("Times New Roman", 9, "bold"),
                    )
                    self.en2.place(x=110, y=100)

                    self.en3 = Entry(
                        self.edcat,
                        width=20,
                        bd=4,
                        relief="groove",
                        font=("Times New Roman", 9, "bold"),
                    )
                    self.en3.place(x=110, y=140)

                    self.en4 = Entry(
                        self.edcat,
                        width=20,
                        bd=4,
                        relief="groove",
                        font=("Times New Roman", 9, "bold"),
                    )
                    self.en4.place(x=110, y=180)

                    self.en5 = Entry(
                        self.edcat,
                        width=20,
                        bd=4,
                        relief="groove",
                        font=("Times New Roman", 9, "bold"),
                    )
                    self.en5.place(x=110, y=220)

                    # Submit Button for updating changes
                    self.butt = Button(
                        self.edcat,
                        text="SUBMIT",
                        bg="#1c1c1b",
                        fg="#ce4a7e",
                        width=8,
                        font=("Calibri", 12, "bold"),
                        command=self.savedit,
                        relief="flat",
                    )
                    self.butt.place(x=30, y=273)

                    self.en1.insert(0, self.val[0])
                    self.en2.insert(0, self.val[1])
                    self.en3.insert(0, self.val[2])
                    self.en4.insert(0, self.val[3])
                    self.en5.insert(0, self.val[4])

                    self.edcat.mainloop()

                else:
                    messagebox.showerror("Invalid Entry", "This Book doesn't exists!")
                    self.entry.delete(0, END)

            def savedit(self):
                self.fn = self.en1.get()
                self.sc = self.en2.get()
                self.rf = self.en3.get()
                self.rb = self.en4.get()
                self.loc = self.en5.get()

                if self.fn and self.sc and self.rf and self.rb and self.loc:
                    cursor = dbfilesystem.cursor()
                    cursor.execute(
                        "UPDATE files SET fileno='"
                        + self.fn
                        + "', section='"
                        + self.sc
                        + "',rfrom='"
                        + self.rf
                        + "',rby='"
                        + self.rb
                        + "',location='"
                        + self.loc
                        + "' WHERE fileno='"
                        + self.filess
                        + "'"
                    )
                    dbfilesystem.commit()
                    messagebox.showinfo(
                        "Changes Saved", "files has been updated successfully!"
                    )
                    self.edcat.destroy()
                    self.entry.delete(0, END)
                else:
                    messagebox.showerror("Error", "Enter Valfn Details")
                    self.entry.delete(0, END)

        obj = editing()
        obj.eddata()


class main:
    def delete(self):
        class dele(main):
            def deletefiles(self):
                self.ff = Frame(root, bg="#ffe8ec", width=900, height=390)
                self.ff.place(x=0, y=110)

                self.f1 = Frame(
                    self.ff, bg="#ffe8ec", width=500, height=200, bd=5, relief="flat"
                )
                self.f1.place(x=200, y=15)

                self.ed = Frame(
                    self.f1, bg="#7ea310", bd=0, relief="flat", width=120, height=30
                )
                self.ed.place(x=150, y=0)

                self.lac = Label(
                    self.ed,
                    text="DELETE files ",
                    bg="#7ea310",
                    fg="#213502",
                    font=("Calibri", 12, "bold"),
                )
                self.lac.place(x=7, y=3)

                # Book fileno
                self.label8 = Label(
                    self.f1,
                    text="Book fileno",
                    bg="#ffe8ec",
                    fg="black",
                    font=("times new roman", 11, "bold"),
                )
                self.label8.place(x=85, y=65)
                self.entry4 = Entry(
                    self.f1,
                    width=30,
                    bd=4,
                    relief="groove",
                    font=("Calibri", 8, "bold"),
                )
                self.entry4.place(x=188, y=65)

                # Delete files Button
                self.button9 = Button(
                    self.f1,
                    text="DELETE",
                    bg="#7ea310",
                    fg="#213502",
                    width=8,
                    font=("Calibri", 12, "bold"),
                    command=self.delfiles,
                    relief="flat",
                    activebackground="black",
                    activeforeground="#7ea310",
                )
                self.button9.place(x=85, y=120)

                # Back Button (Clickable Image)
                self.backbt = Button(
                    self.ff,
                    width=60,
                    bg="#ffe8ec",
                    activebackground="#ffe8ec",
                    bd=0,
                    relief="flat",
                    command=self.cur,
                )
                self.backbt.place(x=0, y=0)
                self.log = PhotoImage(file="bt1.png")
                self.backbt.config(image=self.log, compound=LEFT)
                self.small_log = self.log.subsample(2, 2)
                self.backbt.config(image=self.small_log)

            def deldata(self):
                self.a = self.entry4.get()

                cursor = dbfilesystem.cursor()
                cursorv = dbfilesystem.cursor()
                cursorv.execute("SELECT * FROM files WHERE fileno='" + self.a + "'")
                dbfilesystem.commit()
                self.validation = cursorv.fetchone()

                if self.validation != None:
                    cursor.execute("DELETE FROM files WHERE fileno='" + self.a + "'")
                    dbfilesystem.commit()
                    messagebox.showinfo(
                        "Succesful", "The book is successfully removed from the store!"
                    )
                    self.entry4.delete(0, END)
                else:
                    messagebox.showerror(
                        "Invalid Operation", "This book does not exist!"
                    )
                    self.entry4.delete(0, END)

        occ = dele()
        occ.deletefiles()


class main:
    def search(self):
        class demt(main):
            def delmdata(self):
                self.fc = Frame(root, bg="#ffe8ec", width=900, height=390)
                self.fc.place(x=0, y=110)

                self.fc1 = Frame(
                    self.fc, bg="#ffe8ec", width=500, height=200, bd=5, relief="flat"
                )
                self.fc1.place(x=200, y=15)

                self.edm = Frame(
                    self.fc1, bg="#b76e79", bd=0, relief="flat", width=130, height=35
                )
                self.edm.place(x=140, y=0)

                self.lac = Label(
                    self.edm,
                    text="SEARCH files ",
                    bg="#b76e79",
                    fg="#fff",
                    font=("Calibri", 12, "bold"),
                )
                self.lac.place(x=8, y=5)

                # fileno
                self.label8 = Label(
                    self.fc1,
                    text="fileno",
                    bg="#ffe8ec",
                    fg="black",
                    font=("Times New Roman", 11, "bold"),
                )
                self.label8.place(x=85, y=65)
                self.entryl = Entry(
                    self.fc1,
                    width=30,
                    bd=4,
                    relief="groove",
                    font=("Calibri", 8, "bold"),
                )
                self.entryl.place(x=188, y=65)

                # Search Button
                self.butto = Button(
                    self.fc1,
                    text="SEARCH",
                    bg="#0E0E0E",
                    fg="#fff",
                    width=8,
                    font=("Calibri", 12, "bold"),
                    command=self.search,
                    relief="flat",
                    activebackground="black",
                    activeforeground="#b76e79",
                )
                self.butto.place(x=85, y=120)

                # Back Button (Clickable Image)
                self.backbt = Button(
                    self.fc,
                    width=60,
                    bg="#ffe8ec",
                    activebackground="#ffe8ec",
                    bd=0,
                    relief="flat",
                    command=self.search,
                )
                self.backbt.place(x=1, y=1)
                self.log = PhotoImage(file="bt1.png")
                self.backbt.config(image=self.log, compound=LEFT)
                self.small_log = self.log.subsample(2, 2)
                self.backbt.config(image=self.small_log)

            def search(self):
                self.emp = self.entryl.get()

                cursor = dbfilesystem.cursor()
                cursor.execute("SELECT * FROM files WHERE fileno='" + self.emp + "'")
                dbfilesystem.commit()
                self.srval = cursor.fetchone()

                if self.srval != None:
                    self.top = Tk()
                    self.top.title("Library System")
                    self.top.iconbitmap("")

                    self.top.geometry("400x200+335+250")
                    self.top.resizable(0, 0)
                    self.top.configure(bg="#ffe8ec")

                    self.frm = Frame(self.top, bg="#b76e79", width=100, height=35)
                    self.frm.place(x=100, y=10)

                    self.mnlb = Label(
                        self.frm,
                        bg="#b76e79",
                        fg="#fff",
                        text="AVAILABLE",
                        font=("Calibri", 12, "bold"),
                    )
                    self.mnlb.place(x=9, y=5)

                    self.lb1 = Label(
                        self.top,
                        text="section: ",
                        bg="#ffe8ec",
                        fg="black",
                        font=("Calibri", 12, "bold"),
                    )
                    self.lb1.place(x=85, y=70)
                    self.lb2 = Label(
                        self.top,
                        text=self.srval[1],
                        bg="#ffe8ec",
                        fg="black",
                        font=("Calibri", 12, "bold"),
                    )
                    self.lb2.place(x=165, y=70)

                    self.lb3 = Label(
                        self.top,
                        text="rfrom: ",
                        bg="#ffe8ec",
                        fg="black",
                        font=("Calibri", 12, "bold"),
                    )
                    self.lb3.place(x=85, y=110)
                    self.lb4 = Label(
                        self.top,
                        text=self.srval[2],
                        bg="#ffe8ec",
                        fg="black",
                        font=("Calibri", 12, "bold"),
                    )
                    self.lb4.place(x=165, y=110)

                    self.lb5 = Label(
                        self.top,
                        text="rby: ",
                        bg="#ffe8ec",
                        fg="black",
                        font=("Calibri", 12, "bold"),
                    )
                    self.lb5.place(x=85, y=150)
                    self.lb6 = Label(
                        self.top,
                        text=self.srval[3],
                        bg="#ffe8ec",
                        fg="black",
                        font=("Calibri", 12, "bold"),
                    )
                    self.lb6.place(x=165, y=150)
                    self.entryl.delete(0, END)

                else:
                    messagebox.showwarning(
                        "Invalid files", "This book does not exists!"
                    )
                    self.entryl.delete(0, END)

        _object = demt()
        _object.delmdata()

    def show(self):
        class test(main):
            def __init__(self):
                self.fc = Frame(root, bg="#ffe8ec", width=900, height=390)
                self.fc.place(x=0, y=110)
                self.popframe = Frame(self.fc, width=180, height=30, bg="#edb40d")
                self.popframe.place(x=360, y=0)
                self.lbn = Label(
                    self.popframe,
                    bg="#edb40d",
                    text="BOOKS INFORMATION",
                    fg="#fff",
                    font=("Calibri", 12, "bold"),
                )

                self.lbn.place(x=8, y=4)

                self.backbt = Button(
                    self.fc,
                    width=30,
                    bg="#ffe8ec",
                    activebackground="#ffe8ec",
                    bd=0,
                    relief="flat",
                    command=self.cur,
                )
                self.backbt.place(x=0, y=0)
                self.log = PhotoImage(file="bt1.png")
                self.backbt.config(image=self.log, compound=LEFT)
                self.small_log = self.log.subsample(3, 3)
                self.backbt.config(image=self.small_log)

                self.table_frame = Frame(self.fc, bg="#ffe8ec", bd=1, relief="flat")
                self.table_frame.place(x=0, y=30, width=900, height=360)

                self.scroll_x = Scrollbar(self.table_frame, orient=HORIZONTAL)
                self.scroll_y = Scrollbar(self.table_frame, orient=VERTICAL)
                self.book_table = ttk.Treeview(
                    self.table_frame,
                    columns=("Book ID", "Title", "Author", "Edition", "Price"),
                    xscrollcommand=self.scroll_x.set,
                    yscrollcommand=self.scroll_y.set,
                )
                self.scroll_x.pack(side=BOTTOM, fill=X)
                self.scroll_y.pack(side=RIGHT, fill=Y)
                self.scroll_x.config(command=self.book_table.xview)
                self.scroll_y.config(command=self.book_table.yview)

                self.book_table.heading("Book ID", text="Book ID")
                self.book_table.heading("Title", text="Title")
                self.book_table.heading("Author", text="Author")
                self.book_table.heading("Edition", text="Edition")
                self.book_table.heading("Price", text="Price")
                self.book_table["show"] = "headings"
                self.book_table.column("Book ID", width=200)
                self.book_table.column("Title", width=200)
                self.book_table.column("Author", width=200)
                self.book_table.column("Edition", width=120)
                self.book_table.column("Price", width=110)
                self.book_table.pack(fill=BOTH, expand=1)
                self.fetch_data()

            def fetch_data(self):
                cursor = dbfilesystem.cursor()
                cursor.execute("SELECT * FROM Books")
                self.rows = cursor.fetchall()
                if len(self.rows) != 0:
                    for self.row in self.rows:
                        self.book_table.insert("", END, values=self.row)
                dbfilesystem.commit()

        oc = test()

    def mainclear(self):
        self.e1.delete(0, END)
        self.e2.delete(0, END)

    def code(self):
        self.fm = Frame(root, height=500, width=900, bg="white")
        self.fm.place(x=0, y=0)

        self.canvas = Canvas(self.fm, height=500, width=900, bg="#000000")
        self.canvas.place(x=0, y=0)

        self.photo = PhotoImage(file=r"pathtoimage\filename.png")
        self.canvas.create_image(0, 0, image=self.photo, anchor=NW)

        self.fm1 = Frame(
            self.canvas, height=260, width=300, bg="#000000", bd=3, relief="sunken"
        )
        self.fm1.place(x=300, y=120)

        self.b1 = Label(
            self.fm1, text="User ID", bg="black", font=("Arial", 10, "bold"), fg="white"
        )
        self.b1.place(x=20, y=42)

        self.e1 = Entry(
            self.fm1, width=22, font=("arial", 9, "bold"), bd=4, relief="groove"
        )
        self.e1.place(x=100, y=40)

        self.lb2 = Label(
            self.fm1,
            text="Password",
            bg="black",
            font=("Arial", 10, "bold"),
            fg="white",
        )
        self.lb2.place(x=20, y=102)

        self.e2 = Entry(
            self.fm1,
            width=22,
            show="*",
            font=("arial", 9, "bold"),
            bd=4,
            relief="groove",
        )
        self.e2.place(x=100, y=100)

        self.btn1 = Button(
            self.fm1,
            text="  Login",
            fg="black",
            bg="yellow",
            width=100,
            font=("Arial", 11, "bold"),
            activebackground="black",
            activeforeground="yellow",
            command=self.login,
            bd=3,
            relief="flat",
            cursor="hand2",
        )
        self.btn1.place(x=25, y=160)
        self.logo = PhotoImage(file=r"pathtoimage.png")
        self.btn1.config(image=self.logo, compound=LEFT)
        self.small_logo = self.logo.subsample(1, 1)
        self.btn1.config(image=self.small_logo)

        self.btn2 = Button(
            self.fm1,
            text="  Clear",
            fg="black",
            bg="yellow",
            width=100,
            font=("Arial", 11, "bold"),
            activebackground="black",
            activeforeground="yellow",
            bd=3,
            relief="flat",
            cursor="hand2",
            command=self.mainclear,
        )
        self.btn2.place(x=155, y=160)
        self.log = PhotoImage(file=r"pathtoimage.png")
        self.btn2.config(image=self.log, compound=LEFT)
        self.small_log = self.log.subsample(1, 1)
        self.btn2.config(image=self.small_log)

        self.forgot = Label(
            self.fm1,
            text="Forgot Password?",
            fg="White",
            bg="#000000",
            activeforeground="black",
            font=("cursive", 9, "bold"),
        )
        self.forgot.place(x=80, y=220)
        self.forgot.bind("<Button>", self.mouseClick)

        root.mainloop()

    def mouseClick(self, event):
        self.rog = Tk()
        self.rog.title("Change password")
        self.rog.geometry("400x300+300+210")
        self.rog.iconbitmap("filename.ico")
        self.rog.resizable(0, 0)
        self.rog.configure(bg="#000")

        self.framerog = Frame(self.rog, width=160, height=30, bg="#d6ed17")
        self.framerog.place(x=95, y=15)

        self.label = Label(
            self.framerog,
            text="SET NEW PASSWORD",
            bg="#d6ed17",
            fg="#606060",
            font=("Calibri", 12, "bold"),
        )
        self.label.place(x=5, y=4)

        self.user = Label(
            self.rog,
            text="User ID",
            bg="#000",
            fg="white",
            font=("Times New Roman", 11, "bold"),
        )
        self.user.place(x=40, y=95)

        self.user = Label(
            self.rog,
            text="New Password",
            bg="#000",
            fg="white",
            font=("Times New Roman", 11, "bold"),
        )
        self.user.place(x=40, y=170)

        self.ef1 = Entry(
            self.rog, width=24, font=("Calibri", 8, "bold"), bd=4, relief="groove"
        )
        self.ef1.place(x=170, y=95)

        self.ef2 = Entry(
            self.rog, width=24, font=("Calibri", 8, "bold"), bd=4, relief="groove"
        )
        self.ef2.place(x=170, y=170)

        self.btn1 = Button(
            self.rog,
            text="SUBMIT",
            fg="#606060",
            bg="#d6ed17",
            width=8,
            font=("Calibri", 12, "bold"),
            activebackground="black",
            activeforeground="#d6ed17",
            bd=3,
            relief="flat",
            cursor="hand2",
            command=self.chan_pas,
        )
        self.btn1.place(x=40, y=240)

    def chan_pas(self):
        self.a = self.ef1.get()
        self.b = self.ef2.get()
        import sqlite3

        conn = sqlite3.connect("admin.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM UserLogin WHERE UserID='" + self.a + "'")
        conn.commit()
        self.data = cursor.fetchone()

        if self.data != None:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE UserLogin SET Password='"
                + self.b
                + "' WHERE UserID='"
                + self.a
                + "'"
            )
            conn.commit()
            messagebox.showinfo("SUCCESSFUL", "Your Password is changed")
            self.rog.destroy()
        else:
            messagebox.showerror("ERROR", "UserID doesn't exist")
            self.rog.destroy()

        self.rog.mainloop()


obj = main()
obj.code
