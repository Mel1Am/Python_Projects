import os
import sqlite3
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

def conectar_base_datos():
    return sqlite3.connect('glosario.db')

def agregar_problema(problema, solucion):
    conexion = conectar_base_datos()
    cursor = conexion.cursor()

    cursor.execute('INSERT INTO glosario (problema, solucion) VALUES (?, ?)', (problema, solucion))
    conexion.commit()
    conexion.close()


def listar_problemas():
    conexion = conectar_base_datos()
    cursor = conexion.cursor()

    cursor.execute('SELECT id, problema FROM glosario')
    resultados = cursor.fetchall()
    conexion.close()

    if resultados:
        print("Problemas listados:")
        for id, problema in resultados:
            print(f"{id}. {problema}")
        
        id_problema = int(input("\nIntroduce el número del problema para ver su solución: "))
        
        os.system('cls' if os.name == 'nt' else 'clear')
        mostrar_solucion(id_problema)
    else:
        print("No hay problemas guardados en el glosario.\n")
        input("Presiona Enter para regresar al menú principal...")


def mostrar_solucion(id_problema):
    conexion = conectar_base_datos()
    cursor = conexion.cursor()

    cursor.execute('SELECT problema, solucion FROM glosario WHERE id = ?', (id_problema,))
    resultado = cursor.fetchone()
    conexion.close()

    if resultado:
        problema, solucion = resultado
        print(f"\nProblema: {problema}")
        print(f"Solución: {solucion}\n")
    else:
        print("No se encontró el problema en el glosario.\n")

    input("Presiona Enter para regresar al menú principal...")

def buscar_problema(consulta):
    consulta = f"%{consulta}%"
    conexion = conectar_base_datos()
    cursor = conexion.cursor()

    cursor.execute('SELECT id, problema, solucion FROM glosario WHERE problema LIKE ?', (consulta,))
    resultados = cursor.fetchall()
    conexion.close()

    return resultados


'''def menu_principal():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Glosario de problemas y soluciones")
    print("1. Agregar problema y solución")
    print("2. Listar problemas")
    print("3. Buscar problema por palabras clave")
    print("4. Salir")
    opcion = input("Selecciona una opción: ")
    return opcion
    '''

def agregar_problema_gui():
    problema = simpledialog.askstring("Agregar problema", "Introduce el problema/error:")
    solucion = simpledialog.askstring("Agregar solución", "Introduce la solución propuesta o aproximada:")

    if problema and solucion:
        agregar_problema(problema, solucion)
        messagebox.showinfo("Problema agregado", "El problema y la solución se han agregado al glosario.")

def listar_problemas_gui():
    window = tk.Toplevel()
    window.title("Listar problemas")

    treeview = ttk.Treeview(window, columns=("id", "problema", "solucion"), show="headings")
    treeview.heading("id", text="ID")
    treeview.heading("problema", text="Problema")
    treeview.heading("solucion", text="Solución")
    treeview.pack(fill=tk.BOTH, expand=True)

    conexion = conectar_base_datos()
    cursor = conexion.cursor()
    cursor.execute('SELECT id, problema, solucion FROM glosario')
    resultados = cursor.fetchall()
    conexion.close()

    for resultado in resultados:
        treeview.insert("", "end", values=resultado)


def buscar_problema_gui():
    consulta = simpledialog.askstring("Buscar problema", "Introduce palabras clave del problema/error que deseas buscar:")

    if consulta:
        resultados = buscar_problema(consulta)

        window = tk.Toplevel()
        window.title("Resultados de búsqueda")

        treeview = ttk.Treeview(window, columns=("id", "problema", "solucion"), show="headings")
        treeview.heading("id", text="ID")
        treeview.heading("problema", text="Problema")
        treeview.heading("solucion", text="Solución")
        treeview.pack(fill=tk.BOTH, expand=True)

        for resultado in resultados:
            treeview.insert("", "end", values=resultado)


'''def main():
    while True:
        opcion = menu_principal()

        if opcion == "1":
            agregar_problema()
        elif opcion == "2":
            listar_problemas()
        elif opcion == "3":
            buscar_problema()
        elif opcion == "4":
            print("Gracias por utilizar el glosario. ¡Hasta la próxima!")
            break
        else:
            print("Opción no válida, por favor ingresa un número del 1 al 4.")
            '''

def main():
    root = tk.Tk()
    root.title("Glosario de problemas y soluciones")

    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack()

    agregar_button = tk.Button(frame, text="Agregar problema y solución", command=agregar_problema_gui)
    agregar_button.pack(fill=tk.X, pady=(0, 10))

    listar_button = tk.Button(frame, text="Listar problemas", command=listar_problemas_gui)
    listar_button.pack(fill=tk.X, pady=(0, 10))

    buscar_button = tk.Button(frame, text="Buscar problema por palabras clave", command=buscar_problema_gui)
    buscar_button.pack(fill=tk.X)

    salir_button = tk.Button(frame, text="Salir", command=root.quit)
    salir_button.pack(fill=tk.X, pady=(10, 0))

    root.mainloop()

if __name__ == '__main__':
    main()
