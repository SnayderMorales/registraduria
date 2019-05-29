import hashlib
from template import Template

class Files(Template):
    UPLOAD_FOLDER = './files'
    ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
    UPLOAD_FOLDER_QUERY = './files_query'
    
    def __init__(self, licencia, user_iduser):
        self.licencia = licencia
        self.user_iduser = user_iduser

    def allowed_file(self, filename):
        return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in self.ALLOWED_EXTENSIONS
    
    def validate_file(self, ruta):
        file = super(Files, self).read_files(ruta)
        hash_file = super(Files, self).hash_file(file)
        data = super(Files, self).query_hash(hash_file)
        if len(data) > 0:
            for rut in data:
                file2= super(Files, self).read_files(rut[1])
                if super(Files, self).automata(file2, file) != 'Rechazado':
                    return rut
            return super(Files, self).guardar_archivo(ruta, hash_file,
            self.licencia, self.user_iduser)
        else:
            return super(Files, self).guardar_archivo(ruta, hash_file,
            self.licencia, self.user_iduser)


