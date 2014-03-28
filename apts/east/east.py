from bs4 import BeautifulSoup

with open('east.txt', 'w') as f:
    f.write('address|price|laundry\n')
filename = open('east.html', 'r')
contents = filename.read()
soup = BeautifulSoup(contents)
bigtab = soup.findAll('table', {'width': '700'})
for t in bigtab:
    tables = t.findAll('table', {'width': '100%'})
    for table in tables:
        td = table.find('td', {'width': '85%'})
        if td is not None:
            span = td.find('span')
            address = span.string
            attribs = t.find('table', {'style': 'width:368px;float:left'})
            rent = attribs.find('table', {'width': '100%'})
            spans = rent.findAll('span')
            for span in spans:
                if '$' in str(span):
                    price = span.string
                    features = t.find('td', {'style': 'text-align:justify;height:400px;vertical-align:top'})
                    print address
                    print features
                    items = ['laundry', 'LAUNDRY', 'Laundry']
                    if any(x in str(features) for x in items):
                        laundry = 'yes'
                    else:
                        laundry = 'no'
                    print laundry
                    record = (address,price,laundry)
                    with open('east.txt', 'a+b') as f:
                        f.write('|'.join(record) + '\n')