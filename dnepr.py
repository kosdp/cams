# https://cam.dnepr.com
# https://cam.dnepr.com/hls/num1.m3u8

import requests
import urllib3
urllib3.disable_warnings()
from bs4 import BeautifulSoup
import re

chrome_ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
url_cam = 'https://cam.dnepr.com'
headers = {'User-Agent': chrome_ua}
resp = requests.get(url_cam, headers = headers, verify = False)

soup = BeautifulSoup(resp.text, 'lxml')
cams = { cam['href']:cam.text for cam in soup.find_all('a', {'href':re.compile('^index\.php\?cam=.*$')}) }
for cam in cams:
    if not 'нет' in cams[cam]:
        print('Дніпро', '|', cams[cam], '|', re.sub('$', '.m3u8', re.sub('index\.php\?cam=', 'https://cam.dnepr.com/hls/num', cam)))
