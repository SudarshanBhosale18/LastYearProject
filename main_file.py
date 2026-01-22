import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image , ImageTk 
from tkinter.filedialog import askopenfilename
import cv2
import numpy as np
import time
import sqlite3
from tkinter import *
from PIL import Image
#import tfModel_test as tf_test
global fn
fn=""
##############################################+=============================================================

root = tk.Tk()
root.configure(background="#7DF9FF")
#root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Teeth Detection")


#430
#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 =Image.open('w6.jpg')
image2 =image2.resize((650,700), Image.LANCZOS)

background_image=ImageTk.PhotoImage(image2)
background_label = tk.Label(root, image=background_image,bd=5)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)
#


#frame_display = tk.LabelFrame(root, text=" --Display-- ", width=900, height=250, bd=5, font=('times', 14, ' bold '),bg="lightblue4")
#frame_display.grid(row=0, column=0, sticky='nw')
#frame_display.place(x=300, y=100)

#frame_display1 = tk.LabelFrame(root, text=" --Result-- ", width=900, height=200, bd=5, font=('times', 14, ' bold '),bg="lightblue4")
#frame_display1.grid(row=0, column=0, sticky='nw')
#frame_display1.place(x=300, y=430)

#frame_display2 = tk.LabelFrame(root, text=" --Calaries-- ", width=900, height=50, bd=5, font=('times', 14, ' bold '),bg="lightblue4")
#frame_display2.grid(row=0, column=0, sticky='nw')
#frame_display2.place(x=300, y=380)

frame_alpr = tk.LabelFrame(root, text="  ", width=650, height=700, bd=5, font=('times', 14, ' bold '),bg="#7DF9FF")
frame_alpr.grid(row=0, column=0)
frame_alpr.place(x=700, y=0)

lbl = tk.Label(root, text=".Welcome to Teeth Detection System.", font=('times new roman',30,' bold '),bg="white",fg="#00CED1",width= 65)
lbl.place(x=0, y=10)

lbl = tk.Label(frame_alpr, text="'Dont Wait Until You", font=('Lucida Calligraphy', 18,' bold '),bg="#7DF9FF",fg="black")
lbl.place(x=120, y=100)

lbl = tk.Label(frame_alpr, text="Lose One To Realise ", font=('Lucida Calligraphy', 18,' bold '),bg="#7DF9FF",fg="black")
lbl.place(x=220, y=140)

lbl = tk.Label(frame_alpr, text="How Percious Your ", font=('Lucida Calligraphy', 18,' bold '),bg="#7DF9FF",fg="black")
lbl.place(x=120, y=180)

lbl = tk.Label(frame_alpr, text="Pearly Whites Are'", font=('Lucida Calligraphy', 18,' bold '),bg="#7DF9FF",fg="black")
lbl.place(x=220, y=220)



def login():

    from subprocess import call
    call(["python", "login.py"])  

def register():

    from subprocess import call
    call(["python", "registration.py"])  
   
def window():
    root.destroy()

button1 = tk.Button(frame_alpr, text=" REGISTER ",command=register,width=15, height=1, font=('times', 15, ' bold '),bg="BLUE",fg="white")
button1.place(x=130, y=350)

button2 = tk.Button(frame_alpr, text="LOGIN",command=login,width=15, height=1, font=('times', 15, ' bold '),bg="GREEN",fg="white")
button2.place(x=350, y=350)




root.mainloop()