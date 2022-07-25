#This code imports the os library
# It creates a class with a function
# It calls the function from the class and prints the value

import os 
os.system('clear')


class myFirstClass:
    def suma(a, b):
        suma = a + b
        print(suma)
    pass

myFirstClass.suma(2,2)
