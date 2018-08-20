#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 14:03:56 2018

@author: rishav
"""

from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from PIL import Image
from subprocess import call
import time
import prediction_script
import os 
# Root Window and Button Action is defined 
top = Tk()
top.title("deepView Sandbox Demo")
res= StringVar()
res.set("Result")
proc= StringVar()
proc.set("Upload Jpeg File")
def clicked():
    source=filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    if(source):
        proc.set("File Loaded")
        top.update_idletasks()
        im1=Image.open(source)
        ## USe thumbnail to preserve aspect ratio
        #size=640,480
        #im1.thumbnail(size)
        im2 = im1.resize((640, 480), Image.ANTIALIAS)
        im2.save("TestO/result.jpg")
        src="TestR/result.png"
        im3=""
        call(["bin\\OpenPoseDemo.exe","--image_dir","TestO\\","--write_images","TestR\\","--write_json","TestR\\"])
        while(True):
            try:
              im3=Image.open(src)
            except:
                proc.set("Generating Skeleton...")
                top.update_idletasks()
            if(im3):
                break
        img=PhotoImage(file=src)
        canvas.create_image(0,0,image=img,anchor=NW)
        #top.update_tasks()
        proc.set("Skeleton Generated...")
        os.remove("TestO/result.jpg")
        top.update_idletasks()
        result=prediction_script.predict()
        time.sleep(3)
        if(result==1.0):
            res.set("Predicted:-\nViolent")
            lab.config(fg="red")
        else:
            res.set("Predicted:-\nNon-Violent")
            lab.config(fg="green")
        proc.set("Update")
        top.update_tasks()
######## Creating new paned window     
m = PanedWindow(width=800,height=450,orient=HORIZONTAL)
m.pack(fill=BOTH, expand=1)
## We need to add a new panedWindow to m and then in one pane add the button and the other 
# Add a canvas 
m2=PanedWindow(width=600,height=450,orient=VERTICAL,relief=SUNKEN)
btn = Button(m2, text="Upload", command=clicked,bd=5) 
btn.grid(column=0, row=1,ipadx=100,ipady=50)
canvas = Canvas(m2,width=360,height=350)
canvas.grid(column=0,row=0)
m2.add(canvas)
m2.add(btn,padx=150,pady=20)
m.add(m2)
## We need to add a new paned Window to m and then in one pane add the output label and the 
# other add the activities label 
m3=PanedWindow(width=200,height=450,orient=VERTICAL)
lab = Label(m3,textvariable=res,font=("Helvetica",15),fg="red",padx=20,pady=100)
lab.grid(column=0,row=0)
lab2=Label(m3,textvariable=proc)
lab2.grid(column=0,row=1)
m3.add(lab)
m3.add(lab2)
m.add(m3)
top.resizable(False,False)
mainloop()