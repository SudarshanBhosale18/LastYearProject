import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image , ImageTk 
from tkinter.filedialog import askopenfilename
import cv2
import numpy as np
import time
import CNNModel 
import sqlite3
import pandas as pd
import os

#import tfModel_test as 
# import gtts
# from gtts import gTTS
# import requests

global fn
fn=""
##############################################+=============================================================
root = tk.Tk()
root.configure(background="brown")
root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Teeth detection ")

# msg="Cavity Detected..Plz Book your appointment"
# def sms_send():
#     url="https://www.fast2sms.com/dev/bulk"
#     params={
  
#         "authorization":"jmIw5r8SpconV1gXsB4JqTNkfYOP37dRHC2QDWxAibMZKtElaFPdJYpjLumUxDKfNE6Z12rTlRX9SOHo",
#         "sender_id":"SMSINI",
#         "message":msg,
#         "language":"english",
#         "route":"p",
#         "numbers":"7887865466"
#     }
#     rs=requests.get(url,params=params)
#430
#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image

image2 =Image.open('t1.jpeg')
image2 =image2.resize((1700,800))

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)

# image2 =Image.open('T2.jpeg')
# image2 =image2.resize((760,750))

# background_image=ImageTk.PhotoImage(image2)

# background_label = tk.Label(root, image=background_image)

# background_label.image = background_image

# background_label.place(x=800, y=70) #, relwidth=1, relheight=1)
#
lbl = tk.Label(root, text="Let's Start The Detection Process", font=('times', 35,' bold italic'), width=60,height=1,bg="white",fg="blue")
lbl.place(x=5, y=0)

#frame_display = tk.LabelFrame(root, text=" --Display-- ", width=900, height=250, bd=5, font=('times', 14, ' bold '),bg="lightblue4")
#frame_display.grid(row=0, column=0, sticky='nw')
#frame_display.place(x=300, y=100)

#frame_display1 = tk.LabelFrame(root, text=" --Result-- ", width=900, height=200, bd=5, font=('times', 14, ' bold '),bg="lightblue4")
#frame_display1.grid(row=0, column=0, sticky='nw')
#frame_display1.place(x=300, y=430)

#frame_display2 = tk.LabelFrame(root, text=" --Calaries-- ", width=900, height=50, bd=5, font=('times', 14, ' bold '),bg="lightblue4")
#frame_display2.grid(row=0, column=0, sticky='nw')
#frame_display2.place(x=300, y=380)

# frame_alpr = tk.LabelFrame(root, text=" --Process-- ", width=220, height=350, bd=5, font=('times', 14, ' bold '),bg="black",fg="white")
# frame_alpr.grid(row=0, column=0, sticky='nw')
# frame_alpr.place(x=15, y=170)



def update_label1(str_T):
    #clear_img()
    result_label = tk.Label(root, text=str_T, width=40, font=("bold", 25), bg='white', fg='black')
    result_label.place(x=300, y=650)
    
    
    
################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
def update_cal(str_T):
    #clear_img()
    result_label = tk.Label(root, text=str_T, width=40, font=("bold", 20), bg='white', fg='black')
    result_label.place(x=350, y=350)
    
    
    
###########################################################################
def train_model():
 
    update_label("Model Training Start...............")
    
    start = time.time()

    X= CNNModel.main()
    print(X)
    
    end = time.time()
        
    ET="Execution Time: {0:.4} seconds \n".format(end-start)
    
    msg="Model Training Completed.."+'\n'+ X + '\n'+ ET

    update_label(msg)

import functools
import operator


def convert_str_to_tuple(tup):
    s = functools.reduce(operator.add, (tup))
    return s

def test_model_proc(fn):
    from keras.models import load_model


#    global fn
    
    IMAGE_SIZE = 64
    LEARN_RATE = 1.0e-4
    CH=3
    print(fn)
    if fn!="":
        # Model Architecture and Compilation
       
        model = load_model('Teeth_modelnew.h5',compile=False)
            
        # adam = Adam(lr=LEARN_RATE, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0)
        # model.compile(optimizer=adam, loss='categorical_crossentropy', metrics=['accuracy'])
        
        img = Image.open(fn)
        img = img.resize((IMAGE_SIZE,IMAGE_SIZE))
        img = np.array(img)
        
        img = img.reshape(1,IMAGE_SIZE,IMAGE_SIZE,3)
        
        img = img.astype('float32')
        img = img / 255.0
        print('img shape:',img)
        prediction = model.predict(img)
        print(np.argmax(prediction))
        yoga=np.argmax(prediction)
        print(yoga)
        
        
        
        if yoga == 0:
            Cd="Bright, White Enamel\n Healthy teeth boast a bright, white enamel free from stains."
        elif yoga == 1:
            Cd="Cavity Detected \n Precautions :\n 1]A Fluoride Treatment Will Mitigate the Cavity's Progression \n 2]Salt water can also help destroy bacteria that cause cavities. "
            
            print('Cavity Detected')
            
            # sms_send()
        
        elif yoga == 2:
            Cd="No Alzhimer Detected"
        elif yoga == 3:
            Cd="Very Mild Alzheimer Detected"
            
        A=Cd
        return A

# def clear_img():
    
#     img11 = tk.Label(frame_display, background='lightblue4',width=160,height=120)
#     img11.place(x=0, y=0)

def update_label(str_T):
    #clear_img()
    result_label = tk.Label(root, text=str_T, width=50, font=("bold", 20), bg='bisque2', fg='black')
    result_label.place(x=310, y=530)
# def train_model():
    
#     update_label("Model Training Start...............")
    
#     start = time.time()

#     X=Model_frm.main()
    
#     end = time.time()
        
#     ET="Execution Time: {0:.4} seconds \n".format(end-start)
    
#     msg="Model Training Completed.."+'\n'+ X + '\n'+ ET

#     update_label(msg)

def test_model():
    global fn
    if fn!="":
        update_label("Model Testing Start...............")
        
        start = time.time()
    
        X=test_model_proc(fn)
        
        X1="Browsed Image is {0}".format(X)
        
        end = time.time()
            
        ET="Execution Time: {0:.4} seconds \n".format(end-start)
        
        msg="Image Testing Completed.."+'\n'+ X1 + '\n'+ ET
        fn=""
    else:
        msg="Please Select Image For Prediction...."
        
    update_label(msg)
    
    
def openimage():
   
    global fn
    fileName = askopenfilename(initialdir='D:/project code/Updated 100 % code of Teeth detection/Updated 100 % code of Teeth detection/testing_set', title='Select image for Aanalysis ',
                               filetypes=[("all files", "*.*")])
    IMAGE_SIZE=200
    imgpath = fileName
    fn = fileName


#        img = Image.open(imgpath).convert("L")
    img = Image.open(imgpath)
    
    img = img.resize((IMAGE_SIZE,200))
    img = np.array(img)
#        img = img / 255.0
#        img = img.reshape(1,IMAGE_SIZE,IMAGE_SIZE,3)


    x1 = int(img.shape[0])
    y1 = int(img.shape[1])


#
#        gs = cv2.cvtColor(cv2.imread(imgpath, 1), cv2.COLOR_RGB2GRAY)
#
#        gs = cv2.resize(gs, (x1, y1))
#
#        retval, threshold = cv2.threshold(gs, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    im = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(im)
    img = tk.Label(root,text='Original',font=('times new roman', 20 ,'bold'), image=imgtk,compound='bottom', height=250, width=250)
    
    #result_label1 = tk.Label(root, image=imgtk, width=250,height=250)
    #result_label1.place(x=300, y=100)
    img.image = imgtk
    img.place(x=300, y=200)
   # out_label.config(text=imgpath)

def convert_grey():
    global fn    
    IMAGE_SIZE=200
    
    img = Image.open(fn)
    img = img.resize((IMAGE_SIZE,200))
    img = np.array(img)
    
    x1 = int(img.shape[0])
    y1 = int(img.shape[1])

    gs = cv2.cvtColor(cv2.imread(fn, 1), cv2.COLOR_RGB2GRAY)

    gs = cv2.resize(gs, (x1, y1))

    retval, threshold = cv2.threshold(gs, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    print(threshold)

    im = Image.fromarray(gs)
    imgtk = ImageTk.PhotoImage(image=im)
    
    #result_label1 = tk.Label(root, image=imgtk, width=250, font=("bold", 25), bg='bisque2', fg='black',height=250)
    #result_label1.place(x=300, y=400)
    img2 = tk.Label(root,text='Gray',font=('times new roman', 20 ,'bold'), image=imgtk,compound='bottom', height=250, width=250,bg='white')
    img2.image = imgtk
    img2.place(x=580, y=200)
    #label_l1 = tk.Label(root, text='Gray' ,compound='bottom', width=4, height=1)
    #label_l1.place(x=690, y=110)

    im = Image.fromarray(threshold)
    imgtk = ImageTk.PhotoImage(image=im)

    img3 = tk.Label(root,text='Binary',font=('times new roman', 20 ,'bold'), image=imgtk,compound='bottom', height=250, width=250)
    img3.image = imgtk
    img3.place(x=880, y=200)
    #result_label1 = tk.Label(root, image=imgtk, width=250,height=250, font=("bold", 25), bg='bisque2', fg='black')
    #result_label1.place(x=300, y=400)


#################################################################################################################
def window():
    root.destroy()




button1 = tk.Button(text=" Browse Image", command=openimage,width=15, height=1, font=('times', 15, ' bold '),bg="white",fg="darkblue")
button1.place(x=500, y=60)

button2 = tk.Button(text="Preprocessing", command=convert_grey, width=15, height=1, font=('times', 15, ' bold '),bg="white",fg="darkblue")
button2.place(x=700, y=60)



button4 = tk.Button(text="Detection", command=test_model,width=15, height=1,bg="white",fg="darkblue", font=('times', 15, ' bold '))
button4.place(x=900, y=60)


button5 = tk.Button(text="train", command=train_model,width=8, height=1, font=('times', 15, ' bold '),bg="yellow4",fg="white")
button5.place(x=1100, y=60)


exit = tk.Button(text="Exit", command=window, width=15, height=1, font=('times', 15, ' bold '),bg="red",fg="white")
exit.place(x=1300, y=60)


root.mainloop()