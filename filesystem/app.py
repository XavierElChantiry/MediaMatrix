from flask import *  
from os import environ, path
from werkzeug.utils import secure_filename
import uuid
app = Flask(__name__)  

@app.route('/videos/<path:path>')
def send_report(path):
    return send_from_directory( environ["FILESYSTEM_ROOT"], path)

@app.route('/upload', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']  
        rename = (str(uuid.uuid4()) + '.mp4')
        f.filename = secure_filename(rename)
        f.save(path.join(environ["FILESYSTEM_ROOT"],f.filename))  

        data = {"fileLocation":f'http://{environ["FILE_SYSTEM_HOSTNAME"]}:{environ["FILESYSTEM_PORT"]}/videos/{rename}'}
        return make_response(jsonify(data), 201)

  
if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=5001)