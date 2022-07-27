


Client_name = input("Cambiar 'Hola' a: ")
file_a = 'C:\\Users\\1033685\\OneDrive - Blue Yonder\\Documents\\GitHub\\Python_Projects\\FAST\\Qt_Designer\\prueba.txt'


try:
    my_file = open(file_a,'r')
    my_file2 = open('C:\\Users\\1033685\\OneDrive - Blue Yonder\\Documents\\GitHub\\Python_Projects\\FAST\\Qt_Designer\\out.txt','r')
    print("File Exists")
except IOError:
    my_file = open(file_a,'w+')
    my_file2 = open('C:\\Users\\1033685\\OneDrive - Blue Yonder\\Documents\\GitHub\\Python_Projects\\FAST\\Qt_Designer\\out.txt', 'wt')
    print("File is Created")

#my_file = open(path,'a+')
#my_file.write("Prueba de escritura dentro del file\n")
#print(my_file)
#my_file.close()

#input file
fin = open(file_a, "rt")
#output file to write the result to
fout = open('C:\\Users\\1033685\\OneDrive - Blue Yonder\\Documents\\GitHub\\Python_Projects\\FAST\\Qt_Designer\\out.txt', "w+")
#for each line in the input file
for line in fin:
    #read replace the string and write to output file
    fout.write(line.replace("Hola", Client_name))
#close input and output files
fin.close()
fout.close()