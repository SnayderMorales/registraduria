from flask import Flask, redirect, render_template, request, flash, sessions, url_for
import datetime
from flask_mysqldb import MySQL
import hashlib
from werkzeug.utils import secure_filename
from files import Files
from automata_file import Automata
import os


app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'registraduria'
mysql = MySQL(app)
app.config['UPLOAD_FOLDER'] = Files.UPLOAD_FOLDER
app.config['UPLOAD_FOLDER_QUERY'] = Files.UPLOAD_FOLDER_QUERY

@app.route('/')
def do_the_login():
    return render_template('query.html', resultado='')

@app.route('/register/')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def Authentication():
    if request.method == 'POST':
        email = request.form['email']
        m = hashlib.md5()
        m.update(request.form['password'].encode('utf-8'))
        password = m.hexdigest()
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM user WHERE email= %s AND password = %s',(email,password))
        data = cur.fetchone()
        if data is None:
            return 'Usario no existe o usuario invalido'
        else:            
            return render_template('index.html', usuario=data)

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        email = request.form['email']
        m = hashlib.md5()
        m.update(request.form['password'].encode('utf-8'))
        password = m.hexdigest()
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO user (nombres, apellidos, email, password) VALUES (%s, %s, %s, %s)',
       (nombre, apellidos, email,   password))
        mysql.connection.commit()
        return nombre

@app.route('/save_file', methods=['GET', 'POST'])
def save_file():
    if request.method == 'POST':
        archivo = Files(request.form['licencia'], request.form['id_user'])
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and archivo.allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            ruta = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            return render_template('index.html',
                                    data=archivo.template_method(ruta))
    return render_template('index.html')

@app.route('/query_file', methods=['GET', 'POST'])
def query_file():
    if request.method == 'POST':
            archivo = Files("","")
            # check if the post request has the file part
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            # if user does not select file, browser also
            # submit an empty part without filename
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and archivo.allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER_QUERY'], filename))
                ruta = os.path.join(app.config['UPLOAD_FOLDER_QUERY'], filename)
                automata = Automata()
                return render_template('query.html',
                            resultado=automata.template_method(ruta) )
    return render_template('query.html', resultado='')


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=4000, debug=True)