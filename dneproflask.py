from flask import Flask, render_template
from base64 import b64encode
import requests

# app
app = Flask(__name__)

# cams
@app.route('/')
def get_cams():
    cams = []
    for num in range(60):
        url = 'http://camera.dnepro.net/camera' + str(num) + 's.jpg'
        headers = {'Referer':'http://dnepro.net/cams/'}
        resp = requests.get(url, headers=headers)
        if resp.status_code == requests.codes.ok and len(resp.content) > 0:
            img = 'data:image/jpg;base64,' + b64encode(resp.content).decode()
            #params = 'width="1280" height="720"'
            params = 'width="640" height="360"'
            cam = '<a href="http://dnepro.net/cams/' + str(num).zfill(2) + '"><br><img ' + params + ' src="' + img + '"></a><br>'
            cams.append({'data': cam, 'name': num })
    return render_template('cams.html', cams=cams)

# cam
@app.route('/cam/<cam>')
def show_cam(cam):
    return 'here is cam ' + cam

# plates
@app.route('/plates')
def get_plates():
    plates = []
    for num in [7,27,28,34,36,57,59]:
        url = 'http://connect.dnepro.net/cams/' + str(num).zfill(2) + '.txt'
        plate = requests.get(url).text + '<br>'
        plates.append({'data': plate, 'name': num })
    return render_template('cams.html', cams=plates)
