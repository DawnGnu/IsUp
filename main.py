import time
from tkinter import *
from tkinter import ttk
import subprocess



#window
root = Tk()
root.geometry("386x274")
root.title("Is up ? ")

#variable
ip = ""
isclick = False
#create fonction
def isclicked():
    global ip
    isclick = True
    ip = ipbox.get()
    print(ip)
    global ping
    ping(ip)

def ping(host):
    global up
    command = ['ping', '-c', '1', host]
    result = (subprocess.call(command))
    if result == 0:
        up.config(text="server is online !")

    else:
       up.config(text="server is offline !")



#create the widget
grn = ttk.Frame(root, padding=100)
grn.grid()
up = Label(grn, text="enter ip adress")
ipbox = Entry(grn)
buttonup = Button(grn, command=isclicked,text="start ping", width=5, height=1)





#pack the widget 
up.pack()
ipbox.pack()
buttonup.pack()

def task():
    
    time.sleep(1)
    ping(ip)
    root.update()

while 1:
    task()
