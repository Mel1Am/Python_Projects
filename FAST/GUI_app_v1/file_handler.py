# This file is used to open and write on files
# Most likely will be turned into a function
#


from tabnanny import check


path = 'C:\\Users\\1033685\\OneDrive - Blue Yonder\\Documents\\GitHub\\Python_Projects\\FAST\\prueba.txt'
path2 = 'C:\\Users\\1033685\\OneDrive - Blue Yonder\\Documents\\GitHub\\Python_Projects\\FAST\\Checklist.txt'
try:
    my_file = open(path,'r')
    print("File Exists")
except IOError:
    my_file = open(path,'w+')
    print("File is Created")

my_file = open(path,'a+')
my_file.write("Prueba de escritura dentro del file\n")
print(my_file)
my_file.close()

checklist = open(path2,'r')
lines = checklist.readlines()
for line in lines:
    print(line)
    
checklist.close()




'''
from genericpath import exists
from importlib.resources import path
from pathlib import Path


file = path('C:\\Users\\1033685\\OneDrive - Blue Yonder\\Documents\\GitHub\\Python_Projects\\FAST\\prueba.txt')
file.touch(exist_ok=True)
f = open(file)
f.write("Esto es una prueba de escritura")
f.close(file)

print(file)
'''
