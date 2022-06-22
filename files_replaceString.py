import os
import fileinput

Dir = input("Source directory: ")
os.chdir(Dir)

Filelist = os.listdir()
print('File list: ', Filelist)

FileName = input("Enter file name: ")

ExistingTxt = input("Enter Text to search n replace: ")

NewTxt = input("Enter New text: ")

with fileinput.FileInput(FileName, inplace=True,backup='.bak') as file:
    for line in file:
        print(line.replace(ExistingTxt, NewTxt), end='')

file.close()
