import sqlite3

def crear_base_datos():
    conexion = sqlite3.connect('glosario.db')
    cursor = conexion.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS glosario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            problema TEXT NOT NULL,
            solucion TEXT NOT NULL
        );
    ''')
    
    conexion.commit()
    conexion.close()

if __name__ == "__main__":
    crear_base_datos()
