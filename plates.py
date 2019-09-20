import sqlite3
import requests
from datetime import date as dt

database = "plates.db"

sql_create = '''create table plates
(cam, date, time, num)
'''

sql_insert = '''insert into plates
values (?,?,?,?)
'''

conn = sqlite3.connect(database)
cursor = conn.cursor()

try:
    cursor.execute(sql_create)
except sqlite3.OperationalError:
    print("Table already exists")


plates = []
for num in [7,27,28,34,36,57,59]:
    date = dt.today().strftime("%Y.%m.%d")
    cam = str(num).zfill(2)
    url = 'http://connect.dnepro.net/cams/' + cam + '.txt'
    resp = requests.get(url).text
    for line in resp.splitlines():
        time = line[4:12]
        num = line[15:]
        plates.append((cam, date, time, num))


cursor.executemany(sql_insert, plates)

conn.commit()
conn.close()

print("Done")
