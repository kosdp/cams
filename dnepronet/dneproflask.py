from flask import Flask, Response, render_template, stream_with_context
from base64 import b64encode
import requests

# app
app = Flask(__name__)

# cams
@app.route('/')
@app.route('/cams')
def get_cams():
    cams = []
    for num in range(60):
        url = 'http://camera.dnepro.net/camera' + str(num) + 's.jpg'
        headers = {'Referer':'http://dnepro.net/cams/'}
        resp = requests.get(url, headers=headers)
        if resp.status_code == requests.codes.ok and len(resp.content) > 0:
            img = 'data:image/jpg;base64,' + b64encode(resp.content).decode()
            params = 'width="960" height="540"'
            cam = '<a href="/cam/' + str(num) + '"><br><img ' + params + ' src="' + img + '"></a><br>'
            cams.append({'data': cam, 'name': num })
    return render_template('cams.html', cams = cams)

# cam
@app.route('/cam/<cam>')
def show_cam(cam):
    url = 'http://camera.dnepro.net/camera' + cam + '.jpg'
    headers = {'Referer':'http://dnepro.net/cams/'}
    resp = requests.get(url, headers = headers, stream = True)
    return Response(response = stream_with_context(resp.iter_content(chunk_size = 8192)), content_type = resp.headers['Content-Type'], status = resp.status_code)

# plates
@app.route('/plates')
def get_plates():
    plates = []
    for num in [7,27,28,34,36,57,59]:
        url = 'http://connect.dnepro.net/cams/' + str(num).zfill(2) + '.txt'
        plate = requests.get(url).text + '<br>'
        plates.append({'data': plate, 'name': num })
    return render_template('cams.html', cams = plates)
