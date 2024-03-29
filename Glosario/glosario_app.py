import os
import sqlite3

def conectar_base_datos():
    return sqlite3.connect('glosario.db')

def agregar_problema():
    problema = input("Introduce el problema/error: ")
    solucion = input("Introduce la solución propuesta o aproximada: ")

    conexion = conectar_base_datos()
    cursor = conexion.cursor()

    cursor.execute('INSERT INTO glosario (problema, solucion) VALUES (?, ?)', (problema, solucion))
    conexion.commit()
    conexion.close()

    print("Problema y solución agregados con éxito.\n")
    input("Presiona Enter para regresar al menú principal...")

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

def buscar_problema():
    consulta = input("Introduce palabras clave del problema/error que deseas buscar: ")

    conexion = conectar_base_datos()
    cursor = conexion.cursor()

    cursor.execute('SELECT problema, solucion FROM glosario WHERE problema LIKE ?', (f'%{consulta}%',))
    resultados = cursor.fetchall()
    conexion.close()

    if resultados:
        print("\nResultados encontrados:")
        for problema, solucion in resultados:
            print(f"Problema: {problema}\nSolución: {solucion}\n")
    else:
        print("\nNo se encontró el problema/error en el glosario.\n")
        agregar_nuevo_problema = input("Lo lamento, no tengo guardado ese error, ¿deseas añadirlo? (s/n): ")
        if agregar_nuevo_problema.lower() == 's':
            agregar_problema()
            return

    input("Presiona Enter para regresar al menú principal...")

def menu_principal():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Glosario de problemas y soluciones")
    print("1. Agregar problema y solución")
    print("2. Listar problemas")
    print("3. Buscar problema por palabras clave")
    print("4. Salir")
    opcion = input("Selecciona una opción: ")
    return opcion
    

def main():
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
            

if __name__ == '__main__':
    main()
