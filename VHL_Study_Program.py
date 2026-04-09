#!/usr/bin/env python
# coding: utf-8

# In[1]:

#  * Copyright (c) 2025 Arian Azarang at UNC Chapel Hill. All rights reserved.
#  *
#  * This source code is intended for internal use only and may not be
#  * reproduced, distributed, or transmitted in any form or by any means,
#  * including photocopying, recording, or other electronic or mechanical
#  * methods, without the prior written permission of the copyright owner,
#  * except in the case of brief quotations embodied in critical reviews
#  * and certain other noncommercial uses permitted by copyright law.
#  *
#  * For permission requests, write to aazarang@unc.edu.



import tkinter
import os, glob
import cv2 as cv
import numpy as np
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import multiprocessing as mltp
from PIL import ImageTk, Image
from tkinter import filedialog

win= Tk()
win.geometry("320x600+10+10")
win.title("Folder Selection Window")
global Series_number, Instance_number
if os.path.exists("FinalScores.csv"):
    pass
else:
    FinalScores = open("FinalScores.csv",'w')
    FinalScores.write('File ID, Any Cysts/Lesions, How Many Cysts/Lesions, Simple Cysts/Lesions, Not Simple Cysts/Lesions, Any Malignant Lesions, Confidence in Malignancy, Quality of Images, Comments\n')
    FinalScores.close()
def select_file():
    global path_to_data
    path_to_data = filedialog.askdirectory(title="Select a Folder")
def select_file_b_mode():
    global updated_path
    updated_path = os.path.join(path_to_data)
    FilesAll = glob.glob(updated_path+'\*')
    Series_number = []
    for i in range(len(FilesAll)):
        Series_number.append(os.path.splitext(os.path.split(FilesAll[i])[1])[0])
    lbox.delete(0, tk.END)
    for ser in np.unique(Series_number):
        lbox.insert(0, ser)
        lbox.config(yscrollcommand = scrollbar.set, height = 5)
    folder_name = os.path.split(path_to_data)[1]
    if folder_name == "AU0":
        lbox.itemconfigure(0+1, bg="#00aa00", fg="#fff") 
    elif folder_name == "WWY":
        lbox.itemconfigure(0+1, bg="#00aa00", fg="#fff")
    else:
        lbox.itemconfigure(0+1, bg="#00aa00", fg="#fff")
        lbox.itemconfigure(int(len(Series_number)/2)+1, bg="#00aa00", fg="#fff") 

def showcontent(event):
    global selected_serie
    x = lbox.curselection()[0]
    selected_serie = lbox.get(x)
    lesion_count.delete(0, END)
    simple_lesion_count.delete(0, END)
    not_simple_lesion_count.delete(0, END)
    malignancy_confidence_scale.delete(0, END)
    image_quality_scale.delete(0, END)
    comments_final.delete(0, END)
    v.set(None)
    v2.set(None)
    v3.set(None)
    v4.set(None)
    v5.set(None)
    v6.set(None)
def show_series_selected():
    selectedFile = os.path.join(updated_path, selected_serie + '.avi')
    cap = cv.VideoCapture(selectedFile)
    win1 = Toplevel()
    win1.geometry("750x550+350+10")
    win1.configure(bg="gray17")
    max_val = cap.get(cv.CAP_PROP_FRAME_COUNT)
    var = DoubleVar()

    class Control():
        def __init__(self):
            self.scale = Scale(win1, from_=0, to=max_val - 1, orient=HORIZONTAL,
                               variable=var,bg="gray17",fg="white", activebackground='#339999')

            self.scale.set(0)
            self.scale.place(x=70, y=450, width=604)
            self.label = Label(win1)
            self.counter = 0
            self.key = True
            mltp.Process(target=self.display())
            self.scale.bind("<ButtonPress-1>", lambda e: self.active_scaler())
            self.scale.bind("<ButtonRelease-1>", lambda e: self.active_auto())

        def to_pil(self, img):
            
            
            img = cv.resize(img, (600, 400))
            img = cv.cvtColor(img, cv.COLOR_BGRA2RGB)
            image = Image.fromarray(img)
            pic = ImageTk.PhotoImage(image)
            self.label.configure(image=pic)
            self.label.image = pic
            self.label.place(x=70, y=50)
            cv.destroyAllWindows()

        def active_auto(self):
            self.key = True

        def active_scaler(self):
            self.key = False

        def display(self):
            if self.key == True:
                self.counter += 1
                if self.counter >= max_val:
                    self.counter = max_val
                    cap.set(cv.CAP_PROP_POS_FRAMES, self.counter - 1)
                self.scale.set(self.counter)
            else:
                val = self.scale.get()
                self.counter = val
                cap.set(cv.CAP_PROP_POS_FRAMES, self.counter)

            _, frame = cap.read()
            self.to_pil(frame)
            win1.after(100, self.display)

    if __name__ == '__main__':
        Control()
        win1.mainloop()
    cap.release()

def save_assess():
    
    with open("FinalScores.csv", mode='a') as Out:
        path = os.path.normpath(updated_path)
        yy = path.split(os.sep)
        fileID = str(yy[-1] + "_" + selected_serie)
        if list(values)[int(v.get())-1] == 'Y':            
            line = ",".join([fileID,
                             list(values)[int(v.get())-1],
                             str(c_count.get()), 
                             str(s_count.get()), 
                             str(ns_count.get()), 
                             list(values2)[int(v2.get())-1],
                             str(m_status.get()), 
                             str(i_q.get()), 
                             str(comment_to_put.get())])
        else:
            line = ",".join([fileID,
                             list(values)[int(v.get())-1],
                             str(v3.get()), 
                             str(v4.get()), 
                             str(v5.get()), 
                             list(values2)[int(v2.get())-1],
                             str(v6.get()), 
                             str(i_q.get()), 
                             str(comment_to_put.get())])
        Out.write(line+"\n")
    tkinter.messagebox.showinfo("Message", "Please select the next video!") 

def lesion_status():  
    print("You selected the option " + str(v.get()))
def malignancy_status():  
    print("You selected the option " + str(v2.get()))

c_count = tk.StringVar()
s_count = tk.StringVar()
ns_count = tk.StringVar()
m_status = tk.StringVar()
i_q = tk.StringVar()
comment_to_put = tk.StringVar()

v = tk.StringVar()
v.set(None)
values = {"Y" : 1,
          "N" : 2}

v2 = tk.IntVar()
v2.set(None)
values2 = {"Y" : 1, 
           "N" : 2, 
           "Not sure": 3, 
           "N/A": 4}

v3 = tk.StringVar()
v3.set(None)
v4 = tk.StringVar()
v4.set(None)
v5 = tk.StringVar()
v5.set(None)
v6 = tk.StringVar()
v6.set(None)
v7 = tk.StringVar()
v7.set(None)

top_frame = tk.Frame(win)
mid_frame = tk.Frame(win)
mid_frame1 = tk.Frame(win)
mid_frame2 = tk.Frame(win)
mid_frame3 = tk.Frame(win)
mid_frame4 = tk.Frame(win)
mid_frame5 = tk.Frame(win)
mid_frame6 = tk.Frame(win)
mid_frame7 = tk.Frame(win)
mid_frame8 = tk.Frame(win)
mid_frame9 = tk.Frame(win)
bottom_frame = tk.Frame(win)

top_frame.pack(side=tk.TOP)
mid_frame.pack(side=tk.TOP)
mid_frame1.pack(side=tk.TOP)
mid_frame2.pack(side=tk.TOP)
mid_frame3.pack(side=tk.TOP)
mid_frame4.pack(side=tk.TOP)
mid_frame5.pack(side=tk.TOP)
mid_frame6.pack(side=tk.TOP)
mid_frame7.pack(side=tk.TOP)
mid_frame8.pack(side=tk.TOP)
mid_frame9.pack(side=tk.TOP)
bottom_frame.pack(side=tk.TOP)

Label(top_frame, text="Click to select a folder", font=('Aerial 10 bold')).pack(pady=10)
button = ttk.Button(top_frame, text="Select a folder", command= select_file)
button1 = ttk.Button(top_frame, text="Show files", command= select_file_b_mode)

lbox = tk.Listbox(mid_frame, height = 20)
lbox.config(height = 5)

scrollbar = Scrollbar(mid_frame, orient = 'vertical', command = lbox.yview)
lbox.bind('<Double-1>', showcontent)

scrollbar.pack(side = "right", fill = 'y')
show_series = ttk.Button(mid_frame1, text="Show series", command = show_series_selected)

any_lesion_button = Label(mid_frame2, text='Are there any cysts/lesions? (Y/N)')
for (text, value) in values.items():
    Radiobutton(mid_frame2, text = text, variable = v, 
                value = value, command=lesion_status).pack(side = RIGHT, ipady = 5)

how_many_lesion_button = Label(mid_frame3, text='How many cysts/lesions?')
lesion_count = Entry(mid_frame3, textvariable=c_count, width=3)
lesion_count_na = Radiobutton(mid_frame3, text = "N/A", value="N/A", variable = v3).pack(side = RIGHT, ipady = 7)

simple_lesion_button = Label(mid_frame4, text='How many cysts are simple?')
simple_lesion_count = Entry(mid_frame4, textvariable=s_count, width=3)
simple_lesion_count_na = Radiobutton(mid_frame4, text = "N/A", value="N/A", variable = v4).pack(side = RIGHT, ipady = 7)

not_simple_lesion_button = Label(mid_frame5, text='How many cysts/lesions are not simple?', wraplength=200)
not_simple_lesion_count = Entry(mid_frame5, textvariable=ns_count, width=3)
not_simple_lesion_count_na = Radiobutton(mid_frame5, text = "N/A", value="N/A", variable = v5).pack(side = RIGHT, ipady = 7)

malignant_lesion_button = Label(mid_frame6, text='Any malignant/potentially malignant lesions?', wraplength=120)

for (text2, value2) in values2.items():
    Radiobutton(mid_frame6, text = text2, variable = v2, 
                value = value2, command=malignancy_status).pack(side = RIGHT, ipady = 5)

malignancy_confidence_button = Label(mid_frame7, 
                                     text='Confidence in malignancy designation: scale 1-5 (1: least confident, 5: most confident)', 
                                     wraplength=200)
malignancy_confidence_scale = Entry(mid_frame7, textvariable=m_status, width=3)
malignancy_confidence_scale_na = Radiobutton(mid_frame7, text = "N/A", value="N/A", variable = v6).pack(side = RIGHT, ipady = 7)

image_quality_button = Label(mid_frame8, 
                             text='Quality of images: scale 1-5 (1: lowest quality, 5: highest quality)', wraplength=200)
image_quality_scale = Entry(mid_frame8, textvariable=i_q, width=5)

comments_final_label = Label(mid_frame9, text='Comments')
comments_final = Entry(bottom_frame, textvariable=comment_to_put, width=20)

save_results = ttk.Button(bottom_frame, text="Save assessment", command= save_assess)
close = ttk.Button(bottom_frame, text="Close", command= win.destroy)
lbox.pack(side = tk.LEFT, padx = 5, pady = 3)
button.pack(ipadx=5, pady=5, side = 'left')
button1.pack(ipadx=5, pady=5, side = 'left')

show_series.pack(ipadx=20, pady=3, side = 'top')
any_lesion_button.pack(ipadx=20, pady=3, side = 'top')

how_many_lesion_button.pack(ipadx=20, pady=3, side = 'left')
lesion_count.pack(ipadx=10, pady=3, side = 'right')

simple_lesion_button.pack(ipadx=20, pady=3, side = 'left')
simple_lesion_count.pack(ipadx=10, pady=3, side = 'right')

not_simple_lesion_button.pack(ipadx=20, pady=3, side = 'left')
not_simple_lesion_count.pack(ipadx=10, pady=3, side = 'right')

malignant_lesion_button.pack(ipadx=20, pady=3, side = 'top')
malignancy_confidence_button.pack(ipadx=20, pady=3, side = 'left')
malignancy_confidence_scale.pack(ipadx=10, pady=3, side = 'right')

image_quality_button.pack(ipadx=20, pady=3, side = 'left')
image_quality_scale.pack(ipadx=10, pady=3, side = 'right')

comments_final_label.pack(ipadx=20, pady=3, side = 'top')
comments_final.pack(ipadx=20, pady=3, side = 'top')
save_results.pack(ipadx=10, pady=5, side = 'left')
close.pack(ipadx=10, pady=5, side = 'right')
win.mainloop()


# In[ ]:




