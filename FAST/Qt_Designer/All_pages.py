from PyQt5 import QtWidgets, uic

#iniciar la aplicacion

app = QtWidgets.QApplication([])

# Cargar archivos .ui, files, etc

LIAM_q = 'C:\\Users\\1033685\\OneDrive - Blue Yonder\\Documents\\GitHub\\Python_Projects\\FAST\\GUI_app_v1\\LIAM_email_Template.txt'
Home = uic.loadUi("C:\\Users\\1033685\\OneDrive - Blue Yonder\\Documents\\GitHub\\Python_Projects\\FAST\\Qt_Designer\\Home_Page.ui")
NewProject = uic.loadUi("C:\\Users\\1033685\\OneDrive - Blue Yonder\\Documents\\GitHub\\Python_Projects\\FAST\\Qt_Designer\\NewProject_page.ui")
Email = uic.loadUi("C:\\Users\\1033685\\OneDrive - Blue Yonder\\Documents\\GitHub\\Python_Projects\\FAST\\Qt_Designer\\Email_page.ui")

#Variables globales
Client_name = NewProject.client_name.text()

def gui_home():
    pass

def gui_NewProject():
    Email.hide()
    Client_name = NewProject.client_name.text()

    if Client_name == "":
        NewProject.empty_warning.setText("Must enter a Client's Name!")
    elif Client_name != "":
        NewProject.empty_warning.setText("Click the Continue Button.")
        #input file
        fin = open(LIAM_q, "rt")
        #output file to write the result to
        fout = open("out.txt", "wt")
        #for each line in the input file
        for line in fin:
            #read replace the string and write to output file
            fout.write(line.replace('OppOwn', Client_name))
        #close input and output files
        fin.close()
        fout.close()
    else:
        pass

    Home.hide()
    NewProject.show()

def regresar_home():
    NewProject.hide()
    Home.show()

def salir():
    app.exit()

def email_page():
    NewProject.hide()
    Email.show()
    a_file = open("out.txt")
    lines = a_file.readlines()
    for line in lines:
        #print(line)
        Email.email_display.append(line)
    a_file.close()


#Botones
Home.Load_file_button.clicked.connect(gui_NewProject)
NewProject.back_button.clicked.connect(regresar_home)
Home.New_file_button.clicked.connect(salir)
NewProject.continue_2.clicked.connect(email_page)
Email.back_button.clicked.connect(gui_NewProject)

#ejecutable
Home.show()
app.exec()

