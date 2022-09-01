import os

def name_directory(dia):
    mes = "Sept"
    nombre = dia + "_" + mes + "_" + "2022"
    return nombre

def fill_lista():
    lista = []
    for i in range (1,32):
        dia = str(i)
        dir= str(name_directory(dia))
        lista.append(dir)
        #print(dir)
        #print (lista)
    #print(lista)
    return lista

lista = fill_lista()

def create_all_dates():
    for i in range (0,31):
        print(lista[i])

print(create_all_dates())