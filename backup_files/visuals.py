from tkinter import *
from tkinter.ttk import Progressbar
import time
import threading


ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x200')
ws.config(bg='#345')

def start_download():
    time.sleep(5)
    pb.start()   
    
def stop_download():
    pb.stop()

pb = Progressbar(
    ws,
    orient = HORIZONTAL,
    length = 200,
    mode = 'determinate'
    )
pb.pack()

msg = Label(
    ws,
    text='',
    bg='#345',
    fg='red',
    
)

msg.pack()

start = Button(
    ws,
    text='Start Download',
    command=threading.Thread(target=start_download).start()
    #command=start_download
    )

start.pack()

stop = Button(
    ws,
    text='Stop Download',
    command=stop_download
)
stop.pack()

ws.mainloop()