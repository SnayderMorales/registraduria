import hashlib
class Files:
    UPLOAD_FOLDER = './files'
    ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
    UPLOAD_FOLDER_QUERY = './files_query'
    def allowed_file(self, filename):
        return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in self.ALLOWED_EXTENSIONS
