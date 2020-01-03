from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from base64 import b64encode


class MyHTTPRequestHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        wf = self.wfile
        
        wf.write(b'<html><head><title>DneproNet Cams</title></head><body>')

        if self.path == '/plates':

            for num in [7,27,28,34,36,57,59]:
                wf.write(b'<br>Cam ' + str(num).zfill(2).encode())
                try:
                    wf.write(urlopen('http://connect.dnepro.net/cams/' + str(num).zfill(2) + '.txt').read())
                except HTTPError:
                    wf.write(b'<br>No plates')

        else:

            for num in range(60):
                try:
                    resp = urlopen(Request('http://camera.dnepro.net/camera' + str(num) + 's.jpg',headers={'Referer':'http://dnepro.net/cams/'}))
                    img = b'data:image/jpg;base64,' + b64encode(resp.read())
                    wf.write(b'<a href="http://dnepro.net/cams/' + str(num).zfill(2).encode() + b'"><img src="' + img + b'"></a><br>')
                except HTTPError:
                    print("There is no cam " + str(num))


        wf.write(b'</body></html>')


httpd = HTTPServer(('', 3000), MyHTTPRequestHandler)

httpd.serve_forever()

