from abc import ABC, abstractmethod
import hashlib
from flask_mysqldb import MySQL
from flask import Flask
from automata.fa.nfa import NFA
class Template(ABC):
    app = Flask(__name__)
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'registraduria'
    mysql = MySQL(app)

    def template_method(self, file):
        return self.validate_file(file)
    
    def read_files(self, ruta):
        with open(ruta, "rb") as archivo:
                f = archivo.read()
                b = bytearray(f)
                return b

    @abstractmethod
    def validate_file(self, file):
        """Primitive operation. You HAVE TO override me, I'm a placeholder."""
        pass
    
    def hash_file(self, byte):
        filehash = hashlib.md5()
        filehash.update(byte)
        return filehash.hexdigest()

    def query_hash(self, hash_file):
        cur = self.mysql.connection.cursor()
        cur.execute('SELECT * FROM files INNER JOIN user ON files.user_iduser = user.iduser WHERE hash= %s',
        [hash_file])
        data = cur.fetchall()
        return data

    def guardar_archivo(self, ruta, hash_file, licencia, user_iduser):
        cur = self.mysql.connection.cursor()
        cur.execute('INSERT INTO files (ruta, hash, user_iduser, licencia) VALUES (%s, %s, %s, %s)',
        (str(ruta), hash_file, user_iduser, licencia))
        self.mysql.connection.commit()
        return "Archivo guardado"

    def automata(self, archivo, archivoConsulta):
        simbolos = []
        estados = set()
        transicion = {}
        i = 0
        j = 1
        cadena = ''
        for consul in archivoConsulta:
            cadena +=str(consul)
        cadena += ''
        cadena2 = ''
        for arch in archivo:
            simbolos.append(str(arch))
            estados.add('q'+str(i))
            transicion['q'+str(i)] = {str(arch): {'q'+str(j)}}
            cadena2+=str(arch)        
            i = i+1 
            j = j+1
        
        estados.add('q'+str(j-1))
        transicion['q'+str(i)] = {'': {'q'+str(i)}}
        print('Cadena')
        print(cadena)
        print('------------Quintupla-----------------')
        print('Transiciones')
        print(transicion)
        print('Estados')
        print(estados)
        print('Simbolos')
        print(simbolos)
        print('Estado Inicial')
        print('q0')
        print('Estado final')
        print('q'+str(i))
        print('-------------Final de Quintupla----------------')
        nfa = NFA(
    states=estados,
    input_symbols=simbolos,
    transitions=transicion,
    initial_state='q0',
    final_states={'q'+str(i)}
)
        i=0
        j=1
        romper = False
        estadoFinal = {}
        for salto in nfa.transitions:
            print(nfa.transitions[salto])
            if(romper):
                    return 'Rechazado'
            for valor in nfa.transitions[salto]:
                print(valor)
                if(romper):
                    break
                for val in valor:
                    if(cadena[i]==val):
                        i = i+1
                        j=j+1
                        estadoFinal = salto
                    else:
                        print('La cadena no cumple con el automata estado en el '+ salto+ '; Archivo son diferentes')
                        romper = True
                        break
        fin = list(nfa.final_states)
        finalRecorrido = int(estadoFinal.replace('q',''))
        finalEstado = int(str(fin[0]).replace('q',''))      
        if len(cadena)==i and finalEstado-finalRecorrido == 1:
            return 'La cadena cumple con el automata archivos existe'
        else:
            return 'Rechazado'
