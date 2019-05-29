from template import Template

class Automata(Template): 
    
    def validate_file(self, ruta):
        file = super(Automata, self).read_files(ruta)
        hash_file = super(Automata, self).hash_file(file)
        data = super(Automata, self).query_hash(hash_file)
        if len(data) > 0:
            for rut in data:
                file2= super(Automata, self).read_files(rut[1])
                if super(Automata, self).automata(file2, file) != 'Rechazado':
                    return rut
            return "No existe"
        else:
            return "No existe"