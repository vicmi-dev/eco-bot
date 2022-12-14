
"""
Created on 12/2/2022


@author: monica


Visualization for the tk inter interface

From my POV, to be done:
- Insert BG - done
- How to dinamically link the image to the folder and not to user dependent folder 
- Insert Logo
- Insert Quit Button - done 
- Rearrange buttons - done 
- Design of buttons - style doesnt work
- Connect functionality
"""

import os
import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
import tkinter.filedialog
from tkcalendar import DateEntry
from datetime import datetime, timezone
from pathlib import Path
from tkinter import messagebox as mb
from tkinter import *

class VisualsScreen:
    def __init__(self):

        # assigns ques to the display_question function to update later.
        self.display_title()    

        self.buttons()

        self.labels()

    def display_title(self):
        # The title to be shown
        title = Label(root, text="Eco-Bot",
        width=55, bg="black",fg="white", font=("ariel", 20, "bold")) 
         
        # place of the title
        title.place(x=0, y=2)

    def buttons(self):
        #Button to choose the directory            
        #chooseDir_button = Button (root, text="Pick the folder you want to clean!",command=intance.save_space, bg= "black",fg = "white", font=('ariel', 11, 'bold')) 
        #chooseDir_button.place(x=70, y = 50)

       
        style = Style()
        style.configure('TButton', font = ('ariel', 20, 'bold'), foreground = 'red')
        style.map('TButton', foreground = [('active', '!disabled', 'green')], background = [('active', 'black')])

        # This is the second button which is used to Quit the GUI
        quit_button = Button(root, text="Quit",  borderwidth = 1, relief = "solid",command=root.destroy, bg= "black",fg = "white", font=('ariel', 11, 'bold'),)       
        # placing the Quit button on the screen
        quit_button.place(x=850,y=50)

    def labels(self):

        description = tk.Label(canvas1, text='The Eco-Bot is a ML&CS FG Python Script that help us clean our folders from files we do not use anymore', 
        borderwidth = 1, relief = "solid",bg = "white", font = ('ariel', 10,'bold'))
        description.place(x = 10, y = 50)

        """ LABEL FOR FILE SIZE """
        #Label for the question
        label2 = tk.Label(canvas1, text='What do you consider as too many bytes?',
        width = 40, borderwidth = 1, relief = "solid",bg = "white")

        label2.config(font=('ariel', 10))
        label2.place(x= 10,y=90) #canvas1.create_window(400, 75, window=label2)

        #Entry for the number of bytes
        entry1 = tk.Entry (canvas1, borderwidth = 1, relief = "solid")
        #Defining default value
        entry1.insert(0, "2000000")
        entry1.place(x = 100, y = 120)#canvas1.create_window(400, 100, window=entry1)

        """ LABEL FOR KEYWORD """
        #Label for the question
        label2 = tk.Label(canvas1, text='Keyword of files you want to resize/delete', 
        width = 40, borderwidth = 1, relief = "solid", bg = "white")
        label2.config(font=('ariel', 10))
        label2.place(x= 10, y = 160) #canvas1.create_window(400, 125, window=label2)

        #Entry for the number of bytes
        entry2 = tk.Entry (canvas1, borderwidth = 1, relief = "solid")
        entry2.insert(0, "") #Defining default value
        entry2.place(x = 100, y =190)#canvas1.create_window(400, 150, window=entry2)

        """ LABEL FOR DATE PICKER"""
        #Label for the question
        label2 = tk.Label(canvas1, text='Select the date you want to check files previous from',
        width = 40,borderwidth = 1, relief = "solid", bg = "white")
        label2.config(font=('ariel', 10))
        label2.place(x= 10, y = 220) #canvas1.create_window(400, 125, window=label2)

        style = ttk.Style()

        style.configure('my.DateEntry',
                fieldbackground='light green',
                background='dark green',
                foreground='dark blue',
                arrowcolor='white')
        dateentry = DateEntry(canvas1, width = 17, style='my.DateEntry')
        dateentry.grid(row=0,column=0,padx=100, pady = 250)

#Initializing tkimport
root = tk.Tk()
# Adjust size 
root.geometry("900x500")
root.title("Eco-Bot")
# Add image file

bg = PhotoImage(file = os.path.abspath("CustomScripting\eco-bot\/bg.png")) 
#Creating the canvas for the complete dashboard  
canvas1 = tk.Canvas(root, width = 900, height = 500)
#Display Image
canvas1.create_image(0,0, image = bg, anchor = "nw")
canvas1.pack(fill = "both", expand = True)



#Create an object of the class VisualScreen
visual = VisualsScreen()

#Starting the tk dashboard 
root.mainloop()










