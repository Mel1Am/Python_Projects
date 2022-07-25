from itertools import count
import tkinter as tk

path2_w = 'C:\\Users\\1033685\\OneDrive - Blue Yonder\\Documents\\GitHub\\Python_Projects\\FAST\\Checklist.txt'
path2_m = '/Users/lamc/Documents/GitHub/Python_Projects/FAST/Checklist.txt'

window = tk.Tk()
window.title("FAST")
window.geometry("1000x500")


greeting = tk.Label(text="Hello, Welcome to the automated process for FAST")
greeting.pack()

Lb = tk.Listbox(window)
Lb.config(width=100, height=100)



checklist = open(path2_w,'r')
lines = checklist.readlines()
count = 0
for line in lines:
    Lb.insert(11, line)
    Lb.pack()
    print(line)
    
checklist.close()

window.mainloop()


