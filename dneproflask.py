from flask import Flask

app = Flask(__name__)

@app.route('/')
def cams():
    return 'cams here'

@app.route('/cam/<cam>')
def show_cam(cam):
    return 'here is cam ' + cam

@app.route('/plates')
def plates():
    return 'plates here'

# https://flask.palletsprojects.com/en/1.1.x/quickstart
