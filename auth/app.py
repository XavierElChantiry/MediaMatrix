from flask import *  
import json
 
app = Flask(__name__)

f = open('users.json')
users = json.load(f)
f.close

@app.route('/login', methods = ['POST'])

def login():
    if request.method == 'POST':
        password = request.form['password']
        user = request.form['user']
        if password == users[user]:
            #The following flash message will be displayed on successful login
            data = {"Authenticated":'True'}
            return make_response(jsonify(data), 201)
        else:
            data = {"Authenticated":'False'}
            return make_response(jsonify(data), 403)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)
