from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import pymysql
import sys
import os




#import mysql.connector

#---------------------------------------------------------------Login Function --------------------------------------
def clear():
	userentry.delete(0,END)
	passentry.delete(0,END)

def close():
	win.destroy()
	os.system('python ObjCamTk.py')




def login():
	if user_name.get()=="" or password.get()=="":
		messagebox.showerror("Error", "Enter User Name And Password", parent=win)
	else:
		try:
			con = pymysql.connect(host="localhost", user="root", password="root", database="facedetectiondb")

			cur = con.cursor()

			cur.execute("select * from admin where uname=%s and pword = %s",(user_name.get(),password.get()))
			row = cur.fetchone()

			if row==None:
				messagebox.showerror("Error" , "Invalid User Name And Password", parent = win)

			else:
				messagebox.showinfo("Success", "Successfully Login", parent=win)
				close()




			con.close()
		except Exception as es:
			messagebox.showerror("Error", f"Error Due to : {str(es)}", parent = win)


# ------------------------------------------------------------ Login Window -----------------------------------------

win = Tk()

# app title
win.title("Login Page")

# window size
win.maxsize(width=1500, height=1500)
win.minsize(width=1500, height=1500)
bg = PhotoImage(file = "log2.png")
label1 = Label( win, image = bg)
label1.place(x = 0, y = 0)

# heading label
heading = Label(win, text="Login", font='Verdana 25 bold')
heading.place(x=80, y=150)

username = Label(win, text="User Name :", font='Verdana 10 bold')
username.place(x=80, y=220)

userpass = Label(win, text="Password :", font='Verdana 10 bold')
userpass.place(x=80, y=260)

# Entry Box
user_name = StringVar()
password = StringVar()

userentry = Entry(win, width=40, textvariable=user_name)
userentry.focus()
userentry.place(x=200, y=223)

passentry = Entry(win, width=40, show="*", textvariable=password)
passentry.place(x=200, y=260)

# button login and clear

btn_login = Button(win, text="Login", font='Verdana 10 bold', command=login)
btn_login.place(x=200, y=293)

btn_login = Button(win, text="Clear", font='Verdana 10 bold', command=clear)
btn_login.place(x=260, y=293)

win.mainloop()