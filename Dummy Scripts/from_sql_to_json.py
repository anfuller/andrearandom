import pyodbc
import json
import collections
from time import strftime

#Connecting
connstr = 'DRIVER={SQL Server};SERVER=[XXXXX];DATABASE=[XXXXX]'
conn = pyodbc.connect(connstr)
cursor = conn.cursor()

#Do your SQL here to select stuff
cursor.execute("""
[SELECT ALL YOUR SQL HERE]
""")

#Fetch all the rows
rows = cursor.fetchall()

#Empty list
objects_list = []
#Add rows
for row in rows:
    d = collections.OrderedDict()
    d['id'] = row.id
    '[....]'
    try:
        d['lt'] = float(row.lat)
    except TypeError, e:
        d['lt'] = None
    objects_list.append(d)

#Timestamp
timestamp = strftime("%Y-%m-%d %H:%M:%S")

#You make a dictionary
final_dict = collections.OrderedDict()

#Dump the dictionary into json
j = json.dumps(final_dict)

#Write your file
objects_file = '[XXXXX].json'
f = open(objects_file, 'w')
print >> f, j
f.close()

conn.close()