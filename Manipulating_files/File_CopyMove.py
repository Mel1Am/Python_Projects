import os
import glob
import shutil
import fileinput

filecount = 0

for name in glob.glob1(dirr,'Rpt*.txt'):
    src = dirr + '\\' + name
    dst = dest + '\\' + name
    shutil.copy(src,dst)
    filecount=filecount+1

#Replace string inside the file post movement
    with fileinput.FileInput(dst,inplace=True,backup='.bak') as file:
        for line in file:
            print(line.replace('502','700'),end='')

    file.close()

print(filecount)