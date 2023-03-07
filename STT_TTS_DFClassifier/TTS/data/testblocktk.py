from tkinter import *
import tkinter.messagebox
import tkinter
import subprocess, os
from pathlib import Path

root = Tk()


def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

DR = "DR1C" 
input_path = os.path.join("data","combined_wavs", DR)

def set_DR(DR_):
   DR=DR_
   DR_path = os.path.join(os.path.dirname(input_path), DR)
   
   return(DR, DR_path)
DR, DR_path = set_DR("DR1C")

Lb1 = Listbox(root, width=80, height=20)
def createlb1(DR, DR_path):
    Lb1.delete(0,END)
    idx=0
    
    for filename in os.listdir( DR_path):
        
        
        speaker_name = filename
        idx+=idx
        Lb1.insert(idx, F"Region: {DR}, speaker_name: {speaker_name}")
    Lb1.pack()
    return Lb1

def set_dr_and_list(DR):
    DR, DR_path =set_DR(DR)
    Lb1 = createlb1(DR,DR_path)
    return Lb1
 

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
speakermenu = Menu(menubar, tearoff=0)
filemenu.add_cascade(label = "DR1", menu = speakermenu)
filemenu.add_command(label="DR1", command=tkinter._setit(Lb1, set_dr_and_list(DR = "DR1C")))
filemenu.add_command(label="DR2", command=tkinter._setit(Lb1, set_dr_and_list(DR = "DR2C")))
filemenu.add_command(label="DR3", command=tkinter._setit(Lb1, set_dr_and_list(DR = "DR3C")))
filemenu.add_command(label="DR4", command=tkinter._setit(Lb1, set_dr_and_list(DR = "DR4C")))
filemenu.add_command(label="DR5", command=tkinter._setit(Lb1, set_dr_and_list(DR = "DR5C")))
filemenu.add_command(label="DR6", command=tkinter._setit(Lb1, set_dr_and_list(DR = "DR6C")))
filemenu.add_command(label="DR7", command=tkinter._setit(Lb1, set_dr_and_list(DR = "DR7C")))
filemenu.add_command(label="DR8", command=tkinter._setit(Lb1, set_dr_and_list(DR = "DR8C")))
filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Dialect Region", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)


editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

os.getcwd()



root.config(menu=menubar)
root.mainloop()

