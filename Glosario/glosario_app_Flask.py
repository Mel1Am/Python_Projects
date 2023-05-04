# app.py
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def create_connection():
    connection = sqlite3.connect('glosario.db')
    return connection

def init_db():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS glosario (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        problema TEXT NOT NULL,
                        solucion TEXT NOT NULL)''')
    connection.commit()
    connection.close()

@app.route('/buscar', methods=['POST'])
def buscar():
    termino_busqueda = request.form['termino_busqueda']
    with sqlite3.connect("glosario.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM glosario WHERE problema LIKE ? OR solucion LIKE ?", ('%' + termino_busqueda + '%', '%' + termino_busqueda + '%'))
        rows = cursor.fetchall()
    return render_template('index.html', data=rows)


@app.route('/')
def index():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM glosario')
    rows = cursor.fetchall()
    connection.close()
    return render_template('index.html', data=rows)

@app.route('/agregar', methods=['POST'])
def agregar_problema():
    problema = request.form['problema']
    solucion = request.form['solucion']

    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO glosario (problema, solucion) VALUES (?, ?)', (problema, solucion))
    connection.commit()
    connection.close()
    return redirect(url_for('index'))

@app.route('/mostrar_agregar_problema')
def mostrar_agregar_problema():
    return render_template('agregar.html')

@app.route('/editar_eliminar/<int:id>', methods=['GET', 'POST'])
def editar_eliminar(id):
    connection = create_connection()
    cursor = connection.cursor()

    if request.method == 'POST':
        problema = request.form['problema']
        solucion = request.form['solucion']

        cursor.execute('UPDATE glosario SET problema=?, solucion=? WHERE id=?', (problema, solucion, id))
        connection.commit()
        connection.close()
        return redirect(url_for('index'))

    cursor.execute('SELECT * FROM glosario WHERE id=?', (id,))
    row = cursor.fetchone()
    connection.close()
    return render_template('editar.html', data=row)

@app.route('/eliminar/<int:id>')
def eliminar_problema(id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('DELETE FROM glosario WHERE id=?', (id,))
    connection.commit()
    connection.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
