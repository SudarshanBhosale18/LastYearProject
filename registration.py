import tkinter as tk
# from tkinter import *
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re
import random
import os



window = tk.Tk()
window.geometry("700x700+200+50")
window.title("REGISTRATION FORM")
window.configure(background="#7DF9FF")

Fullname = tk.StringVar()
address = tk.StringVar()
username = tk.StringVar()
Email = tk.StringVar()
Phoneno = tk.IntVar()
var = tk.IntVar()
age = tk.IntVar()
password = tk.StringVar()
password1 = tk.StringVar()

value = random.randint(1, 1000)
print(value)

# database code
db = sqlite3.connect('evaluation.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS registration"
               "(Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT,Gender TEXT,age TEXT , password TEXT)")
db.commit()



def password_check(passwd): 
	
	SpecialSym =['$', '@', '#', '%'] 
	val = True
	
	if len(passwd) < 6: 
		print('length should be at least 6') 
		val = False
		
	if len(passwd) > 20: 
		print('length should be not be greater than 8') 
		val = False
		
	if not any(char.isdigit() for char in passwd): 
		print('Password should have at least one numeral') 
		val = False
		
	if not any(char.isupper() for char in passwd): 
		print('Password should have at least one uppercase letter') 
		val = False
		
	if not any(char.islower() for char in passwd): 
		print('Password should have at least one lowercase letter') 
		val = False
		
	if not any(char in SpecialSym for char in passwd): 
		print('Password should have at least one of the symbols $@#') 
		val = False
	if val: 
		return val 

def insert():
    fname = Fullname.get()
    addr = address.get()
    un = username.get()
    email = Email.get()
    mobile = Phoneno.get()
    gender = var.get()
    time = age.get()
    pwd = password.get()
    cnpwd = password1.get()

    with sqlite3.connect('evaluation.db') as db:
        c = db.cursor()

    # Find Existing username if any take proper action
    find_user = ('SELECT * FROM registration WHERE username = ?')
    c.execute(find_user, [(username.get())])

    # else:
    #   ms.showinfo('Success!', 'Account Created Successfully !')

    # to check mail
    #regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    regex='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (re.search(regex, email)):
        a = True
    else:
        a = False
    # validation
    if (fname.isdigit() or (fname == "")):
        ms.showinfo("Message", "please enter valid name")
    elif (addr == ""):
        ms.showinfo("Message", "Please Enter Address")
    elif (email == "") or (a == False):
        ms.showinfo("Message", "Please Enter valid email")
    elif((len(str(mobile)))<10 or len(str((mobile)))>10):
        ms.showinfo("Message", "Please Enter 10 digit mobile number")
    elif ((time > 100) or (time == 0)):
        ms.showinfo("Message", "Please Enter valid age")
    elif (c.fetchall()):
        ms.showerror('Error!', 'Username Taken Try a Diffrent One.')
    elif (pwd == ""):
        ms.showinfo("Message", "Please Enter valid password")
    elif (var == False):
        ms.showinfo("Message", "Please Enter gender")
    elif(pwd=="")or(password_check(pwd))!=True:
        ms.showinfo("Message", "password must contain atleast 1 Uppercase letter,1 symbol,1 number")
    elif (pwd != cnpwd):
        ms.showinfo("Message", "Password Confirm password must be same")
    else:
        conn = sqlite3.connect('evaluation.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO registration(Fullname, address, username, Email, Phoneno, Gender, age , password) VALUES(?,?,?,?,?,?,?,?)',
                (fname, addr, un, email, mobile, gender, time, pwd))

            conn.commit()
            db.close()
            ms.showinfo('Success!', 'Account Created Successfully !')
            # window.destroy()
            window.destroy()
            from subprocess import call
            call(["python", "Login.py"])

#####################################################################################################################################################




l1 = tk.Label(window, text="Patient's Information", font=("Times new roman", 30, "bold"), bg="#7DF9FF", fg="black")
l1.place(x=150, y=20)

#logo1
img = Image.open('a4.jpg')
img = img.resize((100,80), Image.LANCZOS)
logo_image = ImageTk.PhotoImage(img)

logo_label = tk.Label(window, image=logo_image)
logo_label.image = logo_image
logo_label.place(x=30, y=0)

#logo2
img = Image.open('a4.jpg')
img = img.resize((100,80), Image.LANCZOS)
logo_image = ImageTk.PhotoImage(img)

logo_label = tk.Label(window, image=logo_image)
logo_label.image = logo_image
logo_label.place(x=550, y=0)
# that is for label1 registration

l2 = tk.Label(window, text="Full Name :", width=12, font=("Times new roman", 18, "bold"), bg="#7DF9FF")
l2.place(x=130, y=100)
t1 = tk.Entry(window, textvar=Fullname, width=20, font=('', 15))
t1.place(x=330, y=100)
# that is for label 2 (full name)


l3 = tk.Label(window, text="Address :", width=12, font=("Times new roman", 18, "bold"), bg="#7DF9FF")
l3.place(x=130, y=150)
t2 = tk.Entry(window, textvar=address, width=20, font=('', 15))
t2.place(x=330, y=150)
# that is for label 3(address)


l5 = tk.Label(window, text="E-mail :", width=12, font=("Times new roman", 18, "bold"), bg="#7DF9FF")
l5.place(x=130, y=200)
t4 = tk.Entry(window, textvar=Email, width=20, font=('', 15))
t4.place(x=330, y=200)
# that is for email address

l6 = tk.Label(window, text="Phone number :", width=12, font=("Times new roman", 18, "bold"), bg="#7DF9FF")
l6.place(x=130, y=250)
t5 = tk.Entry(window, textvar=Phoneno, width=20, font=('', 15))
t5.place(x=330, y=250)
# phone number
l7 = tk.Label(window, text="Gender :", width=12, font=("Times new roman", 18, "bold"),bg="#7DF9FF")
l7.place(x=130, y=300)
# gender
tk.Radiobutton(window, text="Male", padx=5, width=5, bg="#7DF9FF", font=("bold", 15), variable=var, value=1).place(x=330,
                                                                                                                y=300)
tk.Radiobutton(window, text="Female", padx=20, width=4, bg="#7DF9FF", font=("bold", 15), variable=var, value=2).place(
    x=440, y=300)


l8 = tk.Label(window, text="Age :", width=12, font=("Times new roman", 18, "bold"), bg="#7DF9FF")
l8.place(x=130, y=350)
t6 = tk.Entry(window, textvar=age, width=20, font=('', 15))
t6.place(x=330, y=350)
#age
l4 = tk.Label(window, text="User Name :", width=12, font=("Times new roman", 18, "bold"), bg="#7DF9FF")
l4.place(x=130, y=400)
t3 = tk.Entry(window, textvar=username, width=20, font=('', 15))
t3.place(x=330, y=400)
#username
l9 = tk.Label(window, text="Password :", width=12, font=("Times new roman", 18, "bold"), bg="#7DF9FF")
l9.place(x=130, y=450)
t9 = tk.Entry(window, textvar=password, width=20, font=('', 15), show="*")
t9.place(x=330, y=450)
#password
l10 = tk.Label(window, text="Confirm Password:", width=15, font=("Times new roman", 18, "bold"), bg="#7DF9FF")
l10.place(x=100, y=500)

t10 = tk.Entry(window, textvar=password1, width=20, font=('', 15), show="*")
t10.place(x=330, y=500)

btn = tk.Button(window, text="SIGN-UP", bg="green",font=("",20),fg="white", width=9, height=1, command=insert)
btn.place(x=260, y=550)

window.mainloop()