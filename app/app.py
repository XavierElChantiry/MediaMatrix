from os import environ
import string
from dotenv import load_dotenv
from flask import Flask, flash, render_template, request, redirect, make_response
import requests
from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    current_user,
    logout_user,
    login_required,
)
from hashlib import sha256

from database_get import get_titles, get_video

if environ["PROD"] != "True":
    load_dotenv()


app = Flask(__name__)

app.secret_key = "SuperSecwet"

def hashing(pw): 
    return(sha256(pw.encode('utf-8')).hexdigest())

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
    if request.args.get('id') != None:
        id = request.args.get('id')
    else:
        id = request.form['id']
    if request.method == 'POST':
        res = requests.post(f"http://{environ['AUTH_HOSTNAME'] }:{environ['AUTH_PORT'] }/login",
        request.form)
        video = get_video(id)
        if res.status_code == 201:

            return render_template("video.html", src=video[2], title=video[1])

        else:
            return redirect(f'/login?id={id}')
    return render_template('login.html', id=id)

@app.route('/', methods=['GET'])
def search_page():
    search_title = request.args.get('search', default = "")
    if search_title == "":
        videos = get_titles()
    else:
        videos = get_titles(search_title)
    return render_template("search.html", videos=videos, len=len(videos), search=search_title)



if __name__ == "__main__":
    app.run("localhost", 5000)
