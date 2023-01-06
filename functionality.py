#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 12:39:03 2022

@author: laura
@author: kasper
@author: monica
@author: petra
@author: manuel

Small GUI created with TKinter which let's user pick a folder, file size and a date,
and it will delete the files in the directory which are older than the selected date and bigger than the selected size.

If you experience issues with tkinter run:
pip install tkinter     

If you experience issues with tkcalendar run:
pip install tkcalendar 


From my POV, to be done:
- Add dialog to let user decide whether they want to resize images or delete files. (Compress some files an option? https://superuser.com/questions/1283070/is-is-good-idea-to-store-long-term-data-in-zip-format)
- Work on improving overall user experience.
- Divide project in different classes.
- Add graph showing storage.
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
import shutil




#Initializing tkimport
root = tk.Tk()
# Adjust size 
root.geometry("900x500")
root.title("Eco-Bot")
# Add image file
bg = PhotoImage(file = os.path.abspath("eco-bot\/resources\/bg.png")) 
#Creating the canvas for the complete dashboard  
canvas1 = tk.Canvas(root, width = 900, height = 500)
#Display Image
canvas1.create_image(0,0, image = bg, anchor = "nw")


#Graph for storage space:
total, used, free = shutil.disk_usage("/")

print("Total: %d GiB" % (total // (2**30)))
print("Used: %d GiB" % (used // (2**30)))
print("Free: %d GiB" % (free // (2**30)))
# the variables below size the bar graph
# experiment with them to fit your needs
# highest y = max_data_value * y_stretch
y_stretch = 15
# gap between lower canvas edge and x axis
y_gap = 20
# stretch enough to get all data items in
x_stretch = 10
x_width = 10

# calculate reactangle coordinates (integers) for each bar
x0 = (used // (2**30))
y0 = (total // (2**30))
x1 = 20
y1 = 100
# draw the bar RED
#canvas1.create_rectangle(y0, x0, y1, x1, fill="red")
canvas1.create_rectangle(650, 150, 650+100*(x0/y0), 200, fill="red")

# put the y value above each bar
canvas1.create_text(y0+2, x0, anchor=tk.SW, text=str(x0)+"/"+str(y0))

# calculate reactangle coordinates (integers) for each bar
#y0 = 15 * y_stretch
# draw the bar BLUE
#canvas1.create_rectangle(y0, x0, y1, x1, fill="blue")
canvas1.create_rectangle(650+100*(x0/y0), 150, 750, 200, fill="blue")
# put the y value above each bar
canvas1.create_text(y0+2, x0, anchor=tk.SW)

canvas1.pack(fill = "both", expand = True)
canvas2 = tk.Canvas(root, width = 900, height = 500)


class deleteFilesInFolder:

    def __init__(self):
        pass


    def choose_directory(self):
        """Function to choose the directory""" 
        rootDirectory = tk.Tk()
        myDir = tkinter.filedialog.askdirectory(parent=rootDirectory, initialdir="/",
                                            title='Please select a directory')
        #Filter protected directories
        rootDirectory.destroy()
        return myDir

    def get_file_access_date(self, file_path):
        """Function to get last access time of""" 
        stat_result = Path(file_path).stat()
        modified_date = datetime.fromtimestamp(stat_result.st_mtime, tz=timezone.utc)
        return modified_date

    def clean_files(self, myDir):
        """Function to get last access time of""" 
        bytesTreshold = int(visual.entry1.get())
        keyWord = visual.entry2.get().lower()
        files_to_clean = []
        print("Number of files in folder is: ", len(os.listdir(myDir)), os.listdir(myDir))
        if len(os.listdir(myDir)) > 0:
            for subdir, dirs, files in os.walk(myDir):
                for file in files:
                    file_path = os.path.join(subdir, file)
                    modified_date = self.get_file_access_date(file_path)
                    print("Last date of access is: ", modified_date, " it should be after: ", visual.dateentry.get_date())
                    fileSize = os.path.getsize(file_path)
                    print("File name in the loop: ", file)
                    print("Dir loop: " , os.path.join(subdir, file))
                    print("Size of file is: " + str(fileSize) + " it should be less than: " + str(bytesTreshold))
                    if modified_date.date() < visual.dateentry.get_date():
                        print("True", modified_date.date(),  visual.dateentry.get_date() )
                    else:
                        print("False", modified_date.date(),  visual.dateentry.get_date() )
                    if fileSize > bytesTreshold:
                        print("True", fileSize, bytesTreshold)
                    else:
                        print("False", fileSize, bytesTreshold)
                    if modified_date.date() < visual.dateentry.get_date() and fileSize > bytesTreshold and keyWord in file.lower():
                        files_to_clean.append(file_path)
                    else:
                        print("False no files matching", fileSize, bytesTreshold, modified_date.date(),  visual.dateentry.get_date())                             
                    print("--------------------------------------")
            if len(files_to_clean) > 0:
                app = tk.Tk()
                app.title('List box')
                files_selected = []

                def clicked():
                    print("clicked")
                    selected = box.curselection()  # returns a tuple
                    for idx in selected:
                        print(box.get(idx))
                        files_selected.append(box.get(idx))
                    app.destroy()
                    if self.delete_verification(files_selected, myDir):
                        #Delete the files
                        for file in files_selected:
                            os.remove(file)
                            print(f"""Following files are deleted {"-- ".join(files_selected)} from folder {myDir}""")
                            for subdir, dirs, files in os.walk(myDir):
                                for file in files:
                                    print(os.path.join(subdir, file))
                        #Delete empty folders
                        self.remove_empty_folders(myDir)
                    else:
                        print("Deletion aborted")

                box = tk.Listbox(app, selectmode=tk.MULTIPLE, height=20, width=100)
                for val in files_to_clean:
                    box.insert(tk.END, val)
                box.pack()

                button = tk.Button(app, text='Delete selected files', width=25, command=clicked)
                button.pack()

                exit_button = tk.Button(app, text='Cancel', width=25, command=app.destroy)
                exit_button.pack()
                print("after the multi selection")

            else:
                mb.showinfo("showinfo", "There are no files with the parameters defined.")
        else:
            mb.showinfo("showinfo", "The selected directory is empty")

    def remove_empty_folders(self, path_abs):
        """Delete empty folders"""
        walk = list(os.walk(path_abs))
        for path, _, _ in walk[::-1]:
            if len(os.listdir(path)) == 0:
                os.rmdir(path)
                print(path, " has been removed")

    def delete_verification(self, files_to_clean, myDir):
        """Verify whether user really wants to delete the files"""
        if mb.askyesno('Verify', f"""Do you want to delete these files?
        {'"-- "'.join(files_to_clean)}"""):
            mb.showwarning('Yes', 'Files deleted successfully')
            return True
        else:
            mb.showinfo('No', 'No problem')
            return False

    def save_space(self):
        """Function to save space on disk""" 
        myDir = self.choose_directory()
        self.clean_files(myDir)


    def clean_files_all(self):
        """Clean all files bigger than 2000000000""" 
        myDir = "/Users/"
        bytesTreshold = 2000000000
        print(visual.entry1.get())
        files_to_clean = []
        print("Number of files in folder is: ", len(os.listdir(myDir)), os.listdir(myDir))
        if len(os.listdir(myDir)) > 0:
            for subdir, dirs, files in os.walk(myDir):
                if not "AppData" in subdir and not "Eclipse" in subdir:
                    for file in files:
                        file_path = os.path.join(subdir, file)
                        fileSize = os.path.getsize(file_path)
                        if fileSize > bytesTreshold:
                            files_to_clean.append(file_path)
            if len(files_to_clean) > 0:
                app = tk.Tk()
                app.title('List box')
                files_selected = []

                def clicked():
                    print("clicked")
                    selected = box.curselection()  # returns a tuple
                    for idx in selected:
                        print(box.get(idx))
                        files_selected.append(box.get(idx))
                    app.destroy()
                    if self.delete_verification(files_selected, myDir):
                        #Delete the files
                        for file in files_selected:
                            os.remove(file)
                            print(f"""Following files are deleted {"-- ".join(files_selected)} from folder {myDir}""")
                            for subdir, dirs, files in os.walk(myDir):
                                for file in files:
                                    print(os.path.join(subdir, file))
                        #Delete empty folders
                        self.remove_empty_folders(myDir)
                    else:
                        print("Deletion aborted")

                box = tk.Listbox(app, selectmode=tk.MULTIPLE, height=20, width=100)
                for val in files_to_clean:
                    box.insert(tk.END, val)
                box.pack()

                button = tk.Button(app, text='Show', width=25, command=clicked)
                button.pack()

                exit_button = tk.Button(app, text='Close', width=25, command=app.destroy)
                exit_button.pack()
                print("after the multi selection")

            else:
                mb.showinfo("showinfo", "There are no files with the parameters defined.")
        else:
            mb.showinfo("showinfo", "The selected directory is empty")



class VisualsScreen:

    # Class variables
    #Entry for the number of bytes
    entry1 = tk.Entry (canvas1, borderwidth = 1, relief = "solid",justify= CENTER)
    #Defining default value
    entry1.insert(0, "200")
    entry1.place(x = 100, y = 123)
  
    #Entry for the keyword
    entry2 = tk.Entry (canvas1, borderwidth = 1, relief = "solid", justify= CENTER)
    entry2.insert(0, "") #Defining default value
    entry2.place(x = 100, y =190)
    
    style = ttk.Style()
    # calendar
    style.configure('my.DateEntry',
            fieldbackground='light green',
            background='dark green',
            foreground='dark blue',
            arrowcolor='white')
    dateentry = DateEntry(canvas1, width = 17, style='my.DateEntry',justify= CENTER)
    dateentry.grid(row=0,column=0,padx=100, pady = 255)


    
    """ Checkbutton1 = IntVar()  
    Checkbutton2 = IntVar()  

    
    Button1 = Checkbutton(root, text = "Resize", 
                        variable = Checkbutton1,
                        onvalue = 1,
                        offvalue = 0,
                        height = 2,
                        width = 10,bg= "white")


    Button2 = Checkbutton(root, text = "Delete", 
                        variable = Checkbutton2,
                        onvalue = 1,
                        offvalue = 0,
                        height = 2,
                        width = 10,bg= "white")

    Button1.place(x = 50, y =215)
    Button2.place(x = 150, y =215) """



    def __init__(self):

        # assigns ques to the display_question function to update later.
        self.display_title()    

        self.buttons()

        self.labels()



    def display_title(self):
        # The title to be shown
        title = Label(root, text="Eco-Bot",
        width=57, bg="black",fg="white", font=("ariel", 20, "bold")) 
         
        # place of the title
        title.place(x=0, y=2)

    def buttons(self):

        #Button to choose the directory            
        chooseDir_button = Button (root, text="Pick the folder you want to clean!",command=instance.save_space, bg= "white",fg = "black", font=('ariel', 11, 'bold')) 
        chooseDir_button.place(x=350, y = 400)
       
        style = Style()
        style.configure('TButton', font = ('ariel', 20, 'bold'), foreground = 'red')
        style.map('TButton', foreground = [('active', '!disabled', 'green')], background = [('active', 'black')])

        # This is the second button which is used to Quit the GUI
        quit_button = Button(root, text="Quit",  borderwidth = 1, relief = "solid",command=root.destroy, bg= "black",fg = "white", font=('ariel', 11, 'bold'),)       
        # placing the Quit button on the screen
        quit_button.place(x=850,y=50)

        
        """README Button"""
        

        
        Fact = """The Eco-Bot is a ML&CS FG Python Script that help us clean 
        our folders from files we do not use anymore
        In order to use the Eco-Bot you can set up some filters. 
        For file cleanup you can specify the size of the files, the date of the files
        and a keyword such as a Client Name to delete all the related files."""


        def onClick():
            tkinter.messagebox.showinfo("Eco-Bot Description", Fact)
        readme_button = Button(root, text = "README", command = onClick, height = 2, width = 7, borderwidth = 1, relief = "solid",bg = "white", font = ('ariel', 10,'bold'))
        readme_button.place(x = 450, y = 50)





    def labels(self):

        """ LABEL FOR FILE SIZE """
        #Label for the question
        label2 = tk.Label(canvas1, text='What do you consider as too many bytes?',
        width = 40, borderwidth = 1, relief = "solid",bg = "white")

        label2.config(font=('ariel', 10))
        label2.place(x= 10,y=93) 





        """ LABEL FOR KEYWORD """
        #Label for the question
        label2 = tk.Label(canvas1, text='Keyword of files you want to resize/delete', 
        width = 40, borderwidth = 1, relief = "solid", bg = "white")
        label2.config(font=('ariel', 10))
        label2.place(x= 10, y = 160) #canvas1.create_window(400, 125, window=label2)




        """ LABEL FOR DATE PICKER"""
        #Label for the question
        label2 = tk.Label(canvas1, text='Select the date you want to check files previous from',
        width = 40,borderwidth = 1, relief = "solid", bg = "white")
        label2.config(font=('ariel', 10))
        label2.place(x= 10, y = 225) #canvas1.create_window(400, 125, window=label2)



class VisualsScreenRight:
    
    style = ttk.Style()

    def __init__(self):
        self.labels()
        # self.buttons()

        



    def labels(self):

        """ LABEL FOR FILE SIZE """
        #Label for the question
        label2 = tk.Label(canvas1, text='Your storage:',
        width = 40, borderwidth = 1, relief = "solid",bg = "white")

        label2.config(font=('ariel', 10))
        label2.place(x= 550,y=93) 

        """ LABEL FOR KEYWORD """
        """         #Label for the question
        label2 = tk.Label(canvas1, text='Free up space:', 
        width = 40, borderwidth = 1, relief = "solid", bg = "white")
        label2.config(font=('ariel', 10))
        label2.place(x=510, y = 190) #canvas1.create_window(400, 125, window=label2) """

    """ def buttons(self):

        #Button to choose the directory            
        free_up_space = Button (root, text="Save up some space now!",command=instance.clean_files_all, bg= "white",fg = "black", font=('ariel', 11, 'bold')) 
        free_up_space.place(x=590, y = 250) """




#Create an object of the functionalities class
instance = deleteFilesInFolder()

#Create an object of the class VisualScreen
visual = VisualsScreen()

visualRight = VisualsScreenRight()

#Starting the tk dashboard 
root.mainloop()
