import os
import mysql.connector
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Use environment variables to connect to the database (to support Docker)
db = mysql.connector.connect(
    host="mysql-db",  # MySQL container name
    user="root",
    password="password",
    database="todo_app"
)

cursor = db.cursor()

@app.route('/')
def index():
    cursor.execute("SELECT * FROM todos")
    todos = cursor.fetchall()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    cursor.execute("INSERT INTO todos (task) VALUES (%s)", (task,))
    db.commit()
    return redirect(url_for('index'))

@app.route('/complete/<int:id>')
def complete_task(id):
    cursor.execute("UPDATE todos SET completed = TRUE WHERE id = %s", (id,))
    db.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_task(id):
    cursor.execute("DELETE FROM todos WHERE id = %s", (id,))
    db.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
