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

def editar_eliminar_problema():
    problema_id = simpledialog.askinteger("Editar o eliminar problema", "Ingresa el ID del problema que deseas editar o eliminar:")

    if problema_id is not None:
        conexion = conectar_base_datos()
        cursor = conexion.cursor()
        cursor.execute('SELECT id, problema, solucion FROM glosario WHERE id=?', (problema_id,))
        resultado = cursor.fetchone()

        if resultado:
            accion = messagebox.askquestion("Editar o eliminar problema", "Deseas editar o eliminar el problema seleccionado?", icon="question", type="yesnocancel")

            if accion == "yes":
                problema_editado = simpledialog.askstring("Editar problema", "Ingresa el nuevo nombre del problema:", initialvalue=resultado[1])
                solucion_editada = simpledialog.askstring("Editar solución", "Ingresa la nueva solución:", initialvalue=resultado[2])

                if problema_editado and solucion_editada:
                    cursor.execute('UPDATE glosario SET problema=?, solucion=? WHERE id=?', (problema_editado, solucion_editada, problema_id))
                    conexion.commit()
                    messagebox.showinfo("Problema editado", "El problema y la solución han sido actualizados.")
            elif accion == "no":
                cursor.execute('DELETE FROM glosario WHERE id=?', (problema_id,))
                conexion.commit()
                messagebox.showinfo("Problema eliminado", "El problema y la solución han sido eliminados.")
            else:
                messagebox.showinfo("Acción cancelada", "Operación cancelada, regresando al menú principal.")
        else:
            messagebox.showerror("Error", "No se encontró el problema con el ID especificado.")

        conexion.close()

def ajustar_columnas(treeview):
    for column in treeview["columns"]:
        treeview.column(column, width=tk.StringVar())

    treeview.bind("<Configure>", lambda event, treeview=treeview: auto_ajustar_columnas(event, treeview))

def auto_ajustar_columnas(event, treeview):
    for column in treeview["columns"]:
        treeview.column(column, width=max(treeview.column(column)["width"], treeview.bbox("all", column)[2]))

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

    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)

    agregar_button = tk.Button(frame, text="Agregar problema y solución", command=agregar_problema_gui)
    agregar_button.pack(fill=tk.X, pady=5)

    listar_button = tk.Button(frame, text="Listar problemas y soluciones", command=listar_problemas_gui)
    listar_button.pack(fill=tk.X, pady=5)

    buscar_button = tk.Button(frame, text="Buscar problema por palabra clave", command=buscar_problema_gui)
    buscar_button.pack(fill=tk.X, pady=5)

    editar_eliminar_button = tk.Button(frame, text="Editar o eliminar problema", command=editar_eliminar_problema)
    editar_eliminar_button.pack(fill=tk.X, pady=5)

    salir_button = tk.Button(frame, text="Salir", command=root.destroy)
    salir_button.pack(fill=tk.X, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()

