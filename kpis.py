# http://ss.kpis.com.ua/89/hls/live.m3u8
# http://bezpekamista.com.ua/
# http://ss.bezpekamista.dp.ua/42/hls/live.m3u8

import requests
from bs4 import BeautifulSoup
import re

chrome_ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
url_cam = 'http://bezpekamista.com.ua/'
headers = {'User-Agent': chrome_ua}
resp = requests.get(url_cam, headers = headers)

soup = BeautifulSoup(resp.text, 'lxml')
cams = { cam['href']:cam.text for cam in soup.find_all('a', {'href':re.compile('^/onlinecams/.*-0$')}) }
for cam in cams:
    print(cams[cam], re.sub('-0', '/hls/live.m3u8', re.sub('/onlinecams/kamera-', 'ffplay http://ss.kpis.com.ua/', cam)))
