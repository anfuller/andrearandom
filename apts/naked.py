import requests
from bs4 import BeautifulSoup
import re
import datetime
import _mysql
import os

sttime = datetime.datetime.now()

#Connecting
#conn = _mysql.connect(host="localhost",user="anfuller",passwd="oron",db="testing")
conn = _mysql.connect(host="localhost",user="anfuller",passwd="oron",db="testing")

# rows = conn.store_result()
# rows = rows.fetch_row(maxrows=0)

conn.query("""delete from naked""")

#headers
headers = ['href', 'lat', 'lon', 'sublines', 'station', 'distance', \
          'google', 'time', 'apttype', 'address', 'area', 'borough', 'price', \
          'price2', 'bedrooms', 'listed', 'updated', 'avail', 'building', \
          'feet', 'amenslist', 'laundry', 'unitlaundry', 'gym', 'dishwasher', 'offerslist', 'nofee']

with open('output/naked.txt', 'w') as f:
    f.write('|'.join(headers) + '\n')

#list of page numbers
for x in range (1,2):
    #hitting the naked homepage
    links = ['http://www.nakedapartments.com/renter/listings/search?aids=3&amids=3&baths=&broker_id=&max_rent=2300&min_rent=&move_date=&nids=23%2C211%2C6%2C21%2C203%2C191%2C18%2C24%2C76%2C205%2C10%2C14%2C5%2C93%2C206%2C22%2C17%2C13%2C155%2C16%2C72%2C9%2C20%2C19%2C73%2C7%2C208%2C209%2C192%2C8%2C74%2C210%2C11%2C4%2C3%2C12%2C36%2C30%2C37%2C31%2C38%2C213%2C32%2C33%2C34%2C39%2C43%2C127%2C27%2C28%2C88%2C40%2C35%2C44%2C47%2C48%2C49%2C50%2C113%2C115%2C51%2C52&page=' + str(x) + '&pets=', 'http://www.nakedapartments.com/renter/listings/search?aids=3&amids=14&baths=&broker_id=&max_rent=2300&min_rent=&move_date=&nids=23%2C211%2C6%2C21%2C203%2C191%2C18%2C24%2C76%2C205%2C10%2C14%2C5%2C93%2C206%2C22%2C17%2C13%2C155%2C16%2C72%2C9%2C20%2C19%2C73%2C7%2C208%2C209%2C192%2C8%2C74%2C210%2C11%2C4%2C3%2C12%2C36%2C30%2C37%2C31%2C38%2C213%2C32%2C33%2C34%2C39%2C43%2C127%2C27%2C28%2C88%2C40%2C35%2C44%2C47%2C48%2C49%2C50%2C113%2C115%2C51%2C52&page=' + str(x) + '&pets=']
    for link in links[0:1]:
        try:
            r = requests.get(link)
            soup = BeautifulSoup(r.content)

            #getting all the entries on that page
            listings = soup.findAll('div', {'class': 'listing-details floatLeft'})

            #looping through all the listings
            for l in listings:
                #getting the link ot individual listings
                href = l.find('a')
                href = href.get('href')
                r2 = requests.get(href)
                soup2 = BeautifulSoup(r2.content)
                # getting the lat/lon of each listing
                lat = soup2.find('meta', {'name': 'og:latitude'}).get('content')
                lon = soup2.find('meta', {'name': 'og:longitude'}).get('content')
                # getting the distance to the closest subway
                transit = soup2.find('div', {'class': 'transportation'})
                if transit != None:
                    li = transit.find('li')
                    #nearest subway line
                    lines = []
                    spans = li.findAll('span')
                    for span in spans:
                        line = span.string
                        lines.append(line)
                    lines = ','.join(lines)
                    #nearest subway station
                    station = re.search('(.*) \(0.(.*) mi\)', str(li))
                    station = station.group(1).strip()
                    #distance
                    distance = re.search('\(0.(.*) mi\)', str(li))
                    distance = distance.group(1)
                    distance = float(distance)/100
                    #filtering out apts > .45 miles from a subway
                    if distance <= .45:
                        google = '\N'
                        time = '\N'
                        # #hitting up google with the lat/lon of our apartment
                        # google = 'http://www.google.com/maps/dir/Wall+Street+Journal,+1211+Avenue+of+the+Americas,+New+York,+NY+10036/%27%27/data=!3m1!4b1!4m12!4m11!1m5!1m1!1s0x89c258ff6b2dac81:0x8579374f9050c674!2m2!1d' + lon + '!2d' + lat + '!1m3!2m2!1d' + lon + '!2d' + lat + '!3e3'
                        # r3 = requests.get(google)
                        # soup3 = BeautifulSoup(r3.content)
                        # #getting the shortest route via subway + duration
                        # route = soup3.find('li', {'id': 'altroute_0'})
                        # duration = route.find('div', {'class': 'altroute-rcol altroute-info'})
                        # time = duration.string
                        # time = re.search('(.*?) min',time)
                        # time = time.group(1)
                        # #if the commute time is < 35 minutes, continue
                        # if float(time) <= 35:
                        if distance <= .45:
                            #getting our header info (apt location, type, price) from the listing
                            header = soup2.find('h1')
                            header = header.string.split(',')
                            apttype = header[0].strip()
                            header1 = header[1].strip()
                            if header1[0:1].isdigit():
                                address = header1
                                area = header[2].strip()
                                price = header[3]+header[4]
                                price = price.strip().strip('$')
                                borough = ''
                            else:
                                area = header1
                                price = header[3]+header[4]
                                price = price.strip().strip('$')
                                borough = header[2].strip()
                                address = ''
                            ovr = soup2.find('table', {'id': 'listingOverview'})
                            rows = ovr.findAll('tr')
                            #setting our attributes to blank since some will not be available for every listing
                            price2 = '\N'
                            bedrooms = '\N'
                            listed = '\N'
                            updated = '\N'
                            availal = '\N'
                            building = '\N'
                            feet = '\N'
                            #looping through the rows in our apt. attribute tables
                            for row in rows:
                                tds = row.findAll('td')
                                field = tds[0].string.strip(':')
                                detail = tds[1].string
                                #matching up rows with our column names for attributes
                                if field == 'Price':
                                    price2 = detail.strip().strip('$').replace(',', '')
                                elif field == 'Bedrooms':
                                    bedrooms = detail.strip()
                                elif field == 'Listed for':
                                    listed = detail.strip()
                                elif field == 'Last updated':
                                    updated = detail.strip()
                                elif field == 'Available':
                                    avail = detail.strip()
                                elif field == 'Building Type':
                                    building = detail.strip()
                                elif field == 'Square ft':
                                    feet = detail.strip()
                                else:
                                    pass
                            #amenities
                            amenslist = []
                            #individual amens
                            diswhasher = '\N'
                            gym = '\N'
                            laundry = '\N'
                            unitlaundry = '\N'
                            nofee = '\N'
                            dishwasher = '\N'
                            amenities = soup2.find('div', {'class': 'amens'})
                            try:
                                amens = re.search('<div class="amens">(.*)</div>', str(amenities), re.S)
                                amens = amens.group(1).strip()
                                amens = amens.split(',')
                                for amen in amens:
                                    amen = amen.strip()
                                    amenslist.append(amen)
                                if 'Dishwasher' in amenslist:
                                    dishwasher = 'x'
                                if 'Gym' in amenslist:
                                    gym = 'x'
                                if 'Laundry Room' in amenslist:
                                    laundry = 'x'
                                if 'In-Unit Laundry' in amenslist:
                                    unitlaundry = 'x'
                                amenslist = ','.join(amenslist)
                            except Exception, e:
                                amenslist = '\N'
                            #offers
                            offerslist = []
                            try:
                                offs = soup2.find('div', {'id': 'specialOffers'})
                                spans = offs.findAll('span')
                                for span in spans:
                                    offer = span.string.strip()
                                    offerslist.append(offer)
                                if 'No fee' in offerslist:
                                    nofee = 'x'
                                if offerslist != []:
                                    offerslist = ','.join(offerslist)
                                else:
                                    offerslist = '\N'
                            except Exception, e:
                                offerslist = '\N'
                            record = (href, lat, lon, lines, station, str(distance), google, time, apttype, address, area, borough, price, price2, bedrooms, listed, updated, avail, building, feet, amenslist, laundry, unitlaundry, gym, dishwasher, offerslist, nofee)    
                            #filtering out records < 550 square feet but including unknowns
                            if (feet == '\N' or int(feet) >= 550) and station != '96 St' and station != 'Roosevelt Island' and station != '103 St' and station != '110 St' and station != '125 St' and station != 'Cathedral Pkwy' and station != 'Cathedral Pkwy (110 St)' and station != 'Central Park North (110 St)':
                                print record[1]
                                with open('output/naked.txt', 'a+b') as f:
                                    f.write('|'.join(record) + '\n')
        except Exception, e:
            pass

# conn.query("""LOAD DATA INFILE \'""" + os.getcwd() + '/' + """/output/naked.txt\' INTO TABLE naked
#               FIELDS TERMINATED BY '|'
#               LINES TERMINATED BY '\n'
#               IGNORE 1 LINES;""")
conn.close()

endtime = datetime.datetime.now()
runtime = endtime - sttime
print runtime
