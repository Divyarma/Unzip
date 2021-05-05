from zipfile import ZipFile
import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
from functools import partial

filen=[]
win=tk.Tk()
win.title("Lets unzip !!")

def op():
    f=filedialog.askopenfilename()
    filen.append(f)
    tk.Label(win,text=f).pack()

def unzip():
    dirr=filedialog.askdirectory()
    print (dirr)
    print(filen[0])
    with ZipFile(filen[0],'r') as obj:
        obj.extractall(dirr)
    
    
fn=tkFont.Font(family="Lucida Grande",size=15)
t=tk.Label(win,text="Welcome to the unzipper",width=20,font=fn)
t.pack()
b1=tk.Button(win,text="Open file",height=2,width=8,relief="raised",command=op)
b1.pack()
b2=tk.Button(win,text="Unzip it !! ",height=2,width=8,relief="raised",command=unzip)
b2.pack()
win.mainloop()