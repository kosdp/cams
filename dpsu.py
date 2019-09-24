# curl -v -A "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0" https://dpsu.gov.ua/ua/border/
# curl -v https://stream.dpsu.gov.ua:5101/005_Krakivec_rear/index.m3u8
# curl -v https://stream.dpsu.gov.ua:5101/005_Krakivec_rear/embed.html

import requests
import urllib3
urllib3.disable_warnings()
from bs4 import BeautifulSoup
import re

chrome_ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
url_cam = 'https://dpsu.gov.ua/ua/border/'
headers = {'User-Agent': chrome_ua}
resp = requests.get(url_cam, headers = headers, verify = False)

soup = BeautifulSoup(resp.text, 'lxml')
options = soup.find_all('option',{'data-link': re.compile('http.*')})
for opt in options:
    link = re.sub(r'embed\.html.*$', 'index.m3u8', opt['data-link'])
    print(opt['value'], opt.text, 'mpv ' + link)
