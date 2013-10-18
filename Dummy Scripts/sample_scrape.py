import datetime
import requests
import simplejson as json
import pyodbc

#Connect to SQL
connstr = 'DRIVER={SQL Server};SERVER=[xxxxx];DATABASE=[xxxx]'
conn = pyodbc.connect(connstr)
cursor = conn.cursor()
print "connecting"

#print start time
start_script_time = datetime.datetime.now()
print start_script_time

#hitting the download.
link = 'XXXXX'

#writing results
filename = 'XXXXX.txt'

r = requests.get(link)

with open(filename, 'w') as f:
    f.write(r.content)

#importing raw data
cursor.execute("""
DELETE FROM TABLE;

BULK INSERT TABLE
...
""")
conn.commit()

#You hit a buffer
cursor.execute("""
SELECT latitude, longitude from [TABLE]
""")

rows = cursor.fetchall()
for row in rows:
    link2 = 'XXXX' + str(row.longitude) + ',' + str(row.latitude) + ']}'
    r = requests.get(link2)
    location = json.loads(r.text)
    for county in range(0, 1):
        try:
            county_name = location['objects'][county]['name']

            cursor.execute("""
            UPDATE [TABLE]
            SET county_name = ?
            WHERE latitude = ? AND longitude = ?
            """, county_name, str(row.latitude), str(row.longitude))
            conn.commit()

        except IndexError, e:
            pass

conn.close()