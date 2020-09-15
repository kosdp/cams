# https://cams.dnepr.com
# https://cams.dnepr.com/cam1/cam1.m3u8

import requests
import urllib3
urllib3.disable_warnings()

chrome_ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
url_cam_base = 'https://cams.dnepr.com'
headers = {'User-Agent': chrome_ua}

places = {1: "Парус",
    2: "Серова",
    3: "Башни 1",
    4: "ТЭС 1",
    5: "Плеханова 2",
    6: "Плеханова 1",
    7: "Курчатова",
    8: "Метро",
    9: "Башни 2",
    10: "Монастырский",
    11: "Сакура 1",
    12: "Сакура 2",
    13: "Сакура 3",
    14: "Сакура 4",
    15: "ТЭС 2",
    16: "Сентоза 1",
    17: "Сентоза 2",
    19: "Ек.бульвар",
    20: "Набережная",
    21: "Гражданпроект",
    22: "Евр.площадь",
    25: "Евраз",
    27: "Плеханова 3",
    28: "Мост-Сити",
    29: "Паникахи",
    30: "Центр.мост",
    31: "Театральный",
    34: "Литейная, 9",
    35: "Бювет",
    36: "Литейная, 4",
    37: "Мандрык 1",
    38: "Мандрык 2"}

for cam in range (0,100):
    url_cam = url_cam_base + "/cam{}/cam{}.m3u8".format(cam, cam)
    if requests.get(url_cam, headers = headers, verify = False).ok:
        place = places[cam] if cam in places else ""
        print("Дніпро", '|', place, '|', url_cam)
