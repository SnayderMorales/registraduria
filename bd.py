from flask import Flask
from flask_mysqldb import MySQL

class Database:
    
    def connection(self):
        app = Flask(__name__)
        app.config['MYSQL_HOST'] = 'localhost:3306'
        app.config['MYSQL_USER'] = 'root'
        app.config['MYSQL_PASSWORD'] = ''
        app.config['MYSQL_DB'] = 'registraduria'
        mysql = MySQL(app)
        return mysql
    