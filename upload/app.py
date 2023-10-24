from os import environ
from dotenv import load_dotenv
from flask import Flask, flash, render_template, request, redirect, make_response,session
import requests
from hashlib import sha256
from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    current_user,
    logout_user,
    login_required,
)
from database_acc import upload_to_db

if environ["PROD"] != "True":
    load_dotenv()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in environ['ALLOWED_EXTENSIONS']

app = Flask(__name__)

app.secret_key = "SuperSecwet"

def hashing(pw): 


    print(sha256(usr.encode('utf-8')).hexdigest())

login_manager = LoginManager()

login_manager.init_app(app)

class User(UserMixin):
    pass


@login_manager.user_loader
def user_loader(user):

    user = User()
    user.id = user
    return user


@login_manager.request_loader
def request_loader(request):
    user = request.form.get('user')

    user = User()
    user.id = user
    return user



@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        res = requests.post(f"http://{environ['AUTH_HOSTNAME'] }:{environ['AUTH_PORT'] }/login",
        request.form)
        if res.status_code == 201:
            username = request.form['user']
            flash('Logged in successfully.')
            user = User()
            user.id = username
            login_user(user,remember=True)
            return render_template('upload.html')
        else:
            render_template('login.html')



    return render_template('login.html')

@app.route('/', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        for i in request.files:
            print(i)
        if 'file' not in request.files:
            flash('No file part', "error")
            return redirect(request.url, 400)
        
        file = request.files['file']
        title = request.form['title'].strip()
    
        #Checks for empty data
        if title == '':
            title = "__UNTITLED__"
        
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file', "error")
            return redirect(request.url, 400)
        
        if file and allowed_file(file.filename):
            #Potential success! Submitting to file system service for storing.
            res = requests.post(f"http://{environ['FILE_SYSTEM_HOSTNAME'] }:{environ['FILE_SYSTEM_PORT'] }/upload",
            files=request.files)
            # If the filesystem service confirms object was created, continue
            # Otherwise, raise a 500 error.
            if res.status_code == 201:
                print("Content added to file server!")
            else:
                flash("FILESYSTEM FAILED", "warning")
                return make_response("Error 500 occured. Filesystem failed", 500)
            
            link = res.json()['fileLocation']
            stored_name = upload_to_db(request.form["title"], link)
            if stored_name == "":
                flash("DATABASE FAILED", "warning")
                return make_response("Error 500 occured. Database failed", 500)
            return render_template("upload.html", success=True, filename=stored_name, link=link)
    return render_template('login.html')




if __name__ == "__main__":
    app.run("localhost", 5000)