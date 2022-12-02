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

From my POV, to be done:
- Adjust position of time picker.
- Add dialog to let user decide whether they want to resize images or delete files. (Compress some files an option? https://superuser.com/questions/1283070/is-is-good-idea-to-store-long-term-data-in-zip-format)
- Work on improving overall user experience.
- Publish repository to Accenture github. https://github.com/vicmi-dev/eco-bot.git
- Divide project in different classes.
- Group datepicker and filesize in one column (Left size?)
- Resize images on the right. (Right column?)
- Search files by keywords
"""

import os
import tkinter
import tkinter as tk
from tkinter import ttk
import tkinter.filedialog
from tkcalendar import DateEntry
from datetime import datetime, timezone
from pathlib import Path
from tkinter import messagebox as mb

#How to change scope of variable root so it is accessible within the definition
#global root 

    
#Initializing tkimport
root = tk.Tk()

#Creating the canvas for the complete dashboard  
canvas1 = tk.Canvas(root, width = 800, height = 30)
canvas1.pack()

style = ttk.Style()

style.configure('my.DateEntry',
                fieldbackground='light green',
                background='dark green',
                foreground='dark blue',
                arrowcolor='white')

dateentry = DateEntry(style='my.DateEntry')
dateentry.pack()

#Creating the canvas for the complete dashboard  
canvas2 = tk.Canvas(root, width = 800, height = 300)
canvas2.pack()

#Label for the title
label1 = tk.Label(root, text='Eco-bot')
label1.config(font=('Arial', 20))
canvas2.create_window(400, 30, window=label1)

#Label for the question
label2 = tk.Label(root, text='What do you consider as too many bytes?')
label2.config(font=('Arial', 10))
canvas2.create_window(400, 75, window=label2)

#Entry for the number of bytes
entry1 = tk.Entry (root)
#Defining default value
entry1.insert(0, "2000000")
canvas2.create_window(400, 100, window=entry1)

#Label for the question
label2 = tk.Label(root, text='Keyword of files you want to delete')
label2.config(font=('Arial', 10))
canvas2.create_window(400, 125, window=label2)

#Entry for the number of bytes
entry2 = tk.Entry (root)
#Defining default value
entry2.insert(0, "")
canvas2.create_window(400, 150, window=entry2)

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
        bytesTreshold = int(entry1.get())
        keyWord = entry2.get().lower()
        files_to_clean = []
        print("Number of files in folder is: ", len(os.listdir(myDir)), os.listdir(myDir))
        if len(os.listdir(myDir)) > 0:
            for subdir, dirs, files in os.walk(myDir):
                for file in files:
                    file_path = os.path.join(subdir, file)
                    modified_date = self.get_file_access_date(file_path)
                    print("Last date of access is: ", modified_date, " it should be after: ", dateentry.get_date())
                    fileSize = os.path.getsize(file_path)
                    print("File name in the loop: ", file)
                    print("Dir loop: " , os.path.join(subdir, file))
                    print("Size of file is: " + str(fileSize) + " it should be less than: " + str(bytesTreshold))
                    if modified_date.date() < dateentry.get_date():
                        print("True", modified_date.date(),  dateentry.get_date() )
                    else:
                        print("False", modified_date.date(),  dateentry.get_date() )
                    if fileSize > bytesTreshold:
                        print("True", fileSize, bytesTreshold)
                    else:
                        print("False", fileSize, bytesTreshold)
                    if modified_date.date() < dateentry.get_date() and fileSize > bytesTreshold and keyWord in file.lower():
                        files_to_clean.append(file_path)
                    else:
                        print("False no files matching", fileSize, bytesTreshold, modified_date.date(),  dateentry.get_date())                             
                    print("--------------------------------------")
            if len(files_to_clean) > 0:
                if self.delete_verification(files_to_clean, myDir):
                    #Delete the files
                    for file in files_to_clean:
                        os.remove(file)
                        print(f"""Following files are deleted {"-- ".join(files_to_clean)} from folder {myDir}""")
                        for subdir, dirs, files in os.walk(myDir):
                            for file in files:
                                print(os.path.join(subdir, file))
                    #Delete empty folders
                    self.remove_empty_folders(myDir)
                else:
                    print("Deletion aborted")
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

intance = deleteFilesInFolder()

#Button to choose the directory            
button1 = tk.Button (root, text="Let's save some space",command=intance.save_space, bg='palegreen2', font=('Arial', 11, 'bold')) 
canvas2.create_window(400, 200, window=button1)

#Button to exit the app
button3 = tk.Button (root, text='Exit Application', command=root.destroy, bg='lightsteelblue2', font=('Arial', 11, 'bold'))
canvas2.create_window(400, 260, window=button3)

#Starting the tk dashboard 
root.mainloop()

