from tkinter import *
import tkinter as tk
from tkinter import ttk, LEFT, END
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk


from PIL import Image ,ImageTk

from tkinter.ttk import *
#from pymsgbox import *


root=tk.Tk()

root.title("Welcome to Teeth Detection System")
w = tk.Label(root, text="Welcome to Teeth Detection System",background="skyblue",width=45,height=2,font=("Times new roman",19,"bold"))
w.pack(padx=0, side= TOP, anchor="w")



w,h = root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
root.configure(background="skyblue")
bg = Image.open("T2.jpeg")

# Resize the image (replace 0,0 with the desired width and height)
bg_resized = bg.resize((1400,900))

# Convert the resized image to a Tkinter PhotoImage
bg_img = ImageTk.PhotoImage(bg_resized)

# Create a Label widget and display the image
bg_lbl = tk.Label(root, image=bg_img)
bg_lbl.pack()  

from tkinter import messagebox as ms


def log():
    #ms.showinfo('Welcome to Teeth Detection System')
    from subprocess import call
    call(["python","login.py"])

def reg():
    #ms.showinfo('Detective System', 'Cavity Model.')
    from subprocess import call
    call(["python","registration.py"])



# image2 =Image.open('T6.jpg')
# image2 =image2.resize((500,500))
# #background_image=Image.PhotoImage(image2)
# background_label = TK.Label(root, image=background_image)
# backgriund_label.image = background_image
# background_label.place(x=0,y=0)
# bg = Image.open("T6.jpg")
# bg.resize((0,0))
# print(w,h)
# bg_img = ImageTk.PhotoImage(bg)
# bg_lbl = tk.Label(root,image=bg_img)
# bg_lbl.place(x=90,y=93)
#wlcm=tk.Label(root,text=" Disease Detection System Using Machine Learning",width=85,height=2,background="#151B54",foreground="white",font=("Times new roman",22,"bold"))
#wlcm.place(x=0,y=0)

#choose = "_________________________________Choose Options From Below_________________________________"
#co=tk.Label(root,text=choose,width=95,height=2,background="cyan2",foreground="black",font=("Tempus Sans ITC",19,"bold"))
#co.place(x=0,y=50)

wlcm=tk.Label(root,text="......Welcome to Teeth Detection System......",width=95,bd=0,height=2,background="skyblue",foreground="black",font=("Times new roman",22,"bold"))
wlcm.place(x=0,y=620)

Disease1=tk.Button(root,text="Login",command=log,width=16,bd=0,height=2,background="skyblue",foreground="black",font=("times new roman",14,"bold"))
Disease1.place(x=1070,y=7)


Disease2=tk.Button(root,text="Registration",command=reg,width=12,bd=0,height=2,background="skyblue",foreground="black",font=("times new roman",14,"bold"))
Disease2.place(x=1250,y=7)





root.mainloop()
