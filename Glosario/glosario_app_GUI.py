import os
import sqlite3
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

def conectar_base_datos():
    return sqlite3.connect('glosario.db')

def agregar_problema(problema, solucion):
    conexion = conectar_base_datos()
    cursor = conexion.cursor()

    cursor.execute('SELECT MAX(id) FROM glosario')
    max_id = cursor.fetchone()[0]

    if max_id is None:
        num_problema = 1
    else:
        num_problema = max_id + 1

    cursor.execute('INSERT INTO glosario (id, problema, solucion) VALUES (?, ?, ?)', (num_problema, problema, solucion))
    conexion.commit()
    conexion.close()

def listar_problemas(imprimir_id=False):
    conexion = conectar_base_datos()
    cursor = conexion.cursor()
    cursor.execute('SELECT id, problema, solucion FROM glosario ORDER BY id')

    problemas = cursor.fetchall()
    lista_problemas = ''

    for problema in problemas:
        if imprimir_id:
            lista_problemas += f'ID: {problema[0]}\n'
        lista_problemas += f'Problema: {problema[1]}\nSolución: {problema[2]}\n\n'

    if lista_problemas:
        messagebox.showinfo("Lista de problemas", lista_problemas)
    else:
        messagebox.showinfo("Lista de problemas", "No hay problemas en la base de datos.")

    conexion.close()

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
    listar_problemas(True)

    accion = simpledialog.askstring("Editar o eliminar problema", "Deseas 'editar', 'eliminar' o 'cancelar' el problema seleccionado?")

    if accion.lower() == "editar":
        problema_id = simpledialog.askinteger("Editar problema", "Ingresa el ID del problema que deseas editar:")

        if problema_id is not None:
            conexion = conectar_base_datos()
            cursor = conexion.cursor()
            cursor.execute('SELECT id, problema, solucion FROM glosario WHERE id=?', (problema_id,))
            resultado = cursor.fetchone()

            if resultado:
                problema_editado = simpledialog.askstring("Editar problema", "Ingresa el nuevo nombre del problema:", initialvalue=resultado[1])
                solucion_editada = simpledialog.askstring("Editar solución", "Ingresa la nueva solución:", initialvalue=resultado[2])

                if problema_editado and solucion_editada:
                    cursor.execute('UPDATE glosario SET problema=?, solucion=? WHERE id=?', (problema_editado, solucion_editada, problema_id))
                    conexion.commit()
                    messagebox.showinfo("Problema editado", "El problema y la solución han sido actualizados.")
            else:
                messagebox.showerror("Error", "No se encontró el problema con el ID especificado.")

            conexion.close()
    elif accion.lower() == "eliminar":
        problema_id = simpledialog.askinteger("Eliminar problema", "Ingresa el ID del problema que deseas eliminar:")

        if problema_id is not None:
            conexion = conectar_base_datos()
            cursor = conexion.cursor()
            cursor.execute('SELECT id, problema, solucion FROM glosario WHERE id=?', (problema_id,))
            resultado = cursor.fetchone()

            if resultado:
                cursor.execute('DELETE FROM glosario WHERE id=?', (problema_id,))
                conexion.commit()
                messagebox.showinfo("Problema eliminado", "El problema y la solución han sido eliminados.")
                actualizar_ids(problema_id)
            else:
                messagebox.showerror("Error", "No se encontró el problema con el ID especificado.")

            conexion.close()
    else:
        messagebox.showinfo("Acción cancelada", "Operación cancelada, regresando al menú principal.")

def actualizar_ids(id_eliminar):
    conexion = conectar_base_datos()
    cursor = conexion.cursor()
    cursor.execute('UPDATE glosario SET id = id - 1 WHERE id > ?', (id_eliminar,))
    conexion.commit()
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
    conexion = conectar_base_datos()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, problema, solucion FROM glosario")
    resultados = cursor.fetchall()
    conexion.close()

    listar_problemas_window = tk.Toplevel()
    listar_problemas_window.title("Lista de problemas y soluciones")

    text_widget = tk.Text(listar_problemas_window, wrap=tk.NONE)
    text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scroll_y = tk.Scrollbar(listar_problemas_window, orient=tk.VERTICAL, command=text_widget.yview)
    scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

    scroll_x = tk.Scrollbar(listar_problemas_window, orient=tk.HORIZONTAL, command=text_widget.xview)
    scroll_x.pack(side=tk.BOTTOM, fill=tk.X)

    text_widget.config(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

    for resultado in resultados:
        text_widget.insert(tk.END, f"ID: {resultado[0]}\nProblema: {resultado[1]}\nSolución: {resultado[2]}\n\n")

    text_widget.config(state=tk.DISABLED)

def buscar_problema_gui():
    consulta = simpledialog.askstring("Buscar problema", "Ingresa palabras clave para buscar un problema:")

    if consulta:
        resultados = buscar_problema(consulta)
        buscar_problema_window = tk.Toplevel()
        buscar_problema_window.title("Resultados de búsqueda")

        text_widget = tk.Text(buscar_problema_window, wrap=tk.NONE)
        text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scroll_y = tk.Scrollbar(buscar_problema_window, orient=tk.VERTICAL, command=text_widget.yview)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        scroll_x = tk.Scrollbar(buscar_problema_window, orient=tk.HORIZONTAL, command=text_widget.xview)
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)

        text_widget.config(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

        if resultados:
            for resultado in resultados:
                text_widget.insert(tk.END, f"ID: {resultado[0]}\nProblema: {resultado[1]}\nSolución: {resultado[2]}\n\n")
        else:
            text_widget.insert(tk.END, "No se encontraron resultados para la búsqueda.")

        text_widget.config(state=tk.DISABLED)

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

