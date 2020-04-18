# https://cams.dnepr.com
# https://cams.dnepr.com/cam1/cam1.m3u8

import requests
import urllib3
urllib3.disable_warnings()

chrome_ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
url_cam_base = 'https://cams.dnepr.com'
headers = {'User-Agent': chrome_ua}

for cam in range (0,100):
    url_cam = url_cam_base + "/cam{}/cam{}.m3u8".format(cam, cam)
    if requests.get(url_cam, headers = headers, verify = False).ok:
        print(url_cam)
