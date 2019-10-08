# https://img.snig.info/38/last_s.jpg
# https://img.snig.info/38/last_s.jpg?version=1570525825

# https://img.snig.info/38/last.jpg
# https://img.snig.info/38/last.jpg?version=1570525825

# https://hls.cdn.ua/sneg.info_camera/_definst_/38.stream/playlist.m3u8
# https://5c463ef86ff69.streamlock.net:10443/bukovel/18.stream/playlist.m3u8
# https://5c463ef86ff69.streamlock.net:10443/bukovel/08.stream/playlist.m3u8

# https://bukovel.com/media/cams_th/18_full.jpg
# https://bukovel.com/media/cams/preview/cam_18.mp4
# https://5c463ef86ff69.streamlock.net:10443/bukovel/<<<camId>>>.stream/playlist.m3u8

import requests
import urllib3
urllib3.disable_warnings()
from bs4 import BeautifulSoup
import re

chrome_ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
url_cam = 'https://snig.info/uk'
headers = {'User-Agent': chrome_ua}
resp = requests.get(url_cam, headers = headers, verify = False)

soup = BeautifulSoup(resp.content, 'lxml')

places = { re.sub('/uk/', '', place['href']):place.text for place in soup.find_all('a', {'href':re.compile('^/uk/[^0-9]*$'), 'class':''}) }

cams = { cam['href']:cam.text for cam in soup.find_all('a', {'href':re.compile('^/uk/.*[0-9]$')}) }

#url = 'https://img.snig.info/{}/last.jpg'

for cam in cams:
    place, num = cam.split('/')[2:4]
    if place == 'Bukovel':
        bukovel = {7: 10, 72: 17, 73: 4, 74: 21, 75: 19, 76: 2, 77: 3, 78: 9, 80: 8, 81: 16, 82: 6, 84: 5, 85: 23, 86: 18, 87: 12, 88: 7, 89: 14}
        url = 'https://5c463ef86ff69.streamlock.net:10443/bukovel/{}.stream/playlist.m3u8'
        num = bukovel[int(num)]
    else:
        url = 'https://hls.cdn.ua/sneg.info_camera/_definst_/{}.stream/playlist.m3u8'

    cam_num = str(num).zfill(2)
    print(places[place], '|', cams[cam], 'mpv ' + url.format(cam_num))
