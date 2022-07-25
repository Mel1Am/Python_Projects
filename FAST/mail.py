from itertools import count
import string
import tkinter as tk

path2_w = 'C:\\Users\\1033685\\OneDrive - Blue Yonder\\Documents\\GitHub\\Python_Projects\\FAST\\Checklist.txt'
path2_m = '/Users/lamc/Documents/GitHub/Python_Projects/FAST/Checklist.txt'

#OppOwn = input("What's the Opportunity Owner's name?")
#f = open('out.txt','r')
#print(f.read())
#f.close()


window = tk.Tk()
window.title("FAST")
window.geometry("1000x500")

entry1 = tk.Entry(window)
OppOwn = string(entry1)

with open("LIAM_email_Template.txt", "rt") as fin:
    with open("out.txt", "wt") as fout:
        for line in fin:
            fout.write(line.replace('OppOwn', OppOwn))

greeting = tk.Label(text="Hello, Welcome to the automated process for FAST")
greeting.pack()

window.mainloop()



