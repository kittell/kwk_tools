import os
from tkinter import *
from tkinter.filedialog import askdirectory

root = Tk()
root.withdraw()

dir_start = askdirectory(title='Select starting folder')
if dir_start:
    files = os.listdir(dir_start)
    for file in files:
        print(file)
