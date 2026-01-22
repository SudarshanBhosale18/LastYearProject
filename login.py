
import tkinter as tk
from tkinter import ttk, LEFT, END
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re


##############################################+=============================================================
root = tk.Tk()
root.configure(background="white")
root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("590x450")
root.title("Login Form")



username = tk.StringVar()
password = tk.StringVar()
        
# image2 = Image.open('w1.png')
# image2 = image2.resize((700, 700), Image.ANTIALIAS)

# background_image = ImageTk.PhotoImage(image2)

# background_label = tk.Label(root, image=background_image)

# background_label.image = background_image

# background_label.place(x=0, y=0)  # 


#call registration page
def registration():
    from subprocess import call
    call(["python","registration.py"])
    root.destroy()

#login form connected to dbsqlite
def login():
        # Establish Connection

    with sqlite3.connect('evaluation.db') as db:
         c = db.cursor()

        # Find user If there is any take proper action
         db = sqlite3.connect('evaluation.db')
         cursor = db.cursor()
         cursor.execute("CREATE TABLE IF NOT EXISTS registration"
                           "(Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT,Gender TEXT,age TEXT , password TEXT)")
         db.commit()
         find_entry = ('SELECT * FROM registration WHERE username = ? and password = ?')
         c.execute(find_entry, [(username.get()), (password.get())])
         result = c.fetchall()

         if result:
            msg = ""
            print(msg)
            ms.showinfo("messege", "Patient's LogIn sucessfully")
            # ===========================================
            root.destroy()

            from subprocess import call
            call(['python','GUI_Master.py'])

            # ================================================
         else:
           ms.showerror('Oops!', 'Username Or Password Did Not Found/Match.')

#Images on form
img = Image.open('t8.jpeg')
img = img.resize((100,80), Image.LANCZOS)
logo_image = ImageTk.PhotoImage(img)

logo_label = tk.Label(root, image=logo_image)
logo_label.image = logo_image
logo_label.place(x=250, y=10)
        
title=tk.Label(root, text="Login to Access", font=("arial black", 30, "bold"),bd=5,bg="white",fg="blue")
title.place(x=150,y=70,width=350)
        
l4 = tk.Label(root, text="User Name :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l4.place(x=100, y=150)
t3 = tk.Entry(root, textvar=username, width=20, font=('times new roman', 15),bg="#AFEEEE")
t3.place(x=250, y=150)

l9 = tk.Label(root, text="Password :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l9.place(x=100, y=200)
t9 = tk.Entry(root, textvar=password, width=20, font=('times new roman', 15), show="*",bg="#AFEEEE")
t9.place(x=250, y=200)
        
button1 = tk.Button(root, text=" SIGN UP ",command=registration,width=10, height=1, font=('times', 15, ' bold '),bg="#808000",fg="white")
button1.place(x=250, y=350)

button2 = tk.Button(root, text="SUBMIT",command=login,width=10, height=1, font=('times', 15, ' bold '),bg="BLUE",fg="white")
button2.place(x=250, y=250)
        
title=tk.Label(root, text="Not a member Yet??", font=("Algerian", 15, "bold"),bd=5,bg="white",fg="black")
title.place(x=220,y=300)       
    
       
    
    
def window():
    root.destroy()
  
  








root.mainloop()