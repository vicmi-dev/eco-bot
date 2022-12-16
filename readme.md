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