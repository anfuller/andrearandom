#modules

import mechanize
from bs4 import BeautifulSoup
import cookielib
import time
import datetime

br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# User-Agent (this is cheating, ok(?)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

url = 'https://maps.google.com/maps?saddr=7950+Jones+Branch+Dr,+McLean,+VA&daddr=1216+N+Troy+St,+Arlington,+VA&hl=en&ll=38.904927,-77.150116&spn=0.154959,0.235863&sll=38.90653,-77.155609&sspn=0.154955,0.235863&geocode=Fd4IUgIdB8Nl-ylRH3nclUq2iTEBTUSp16rWAQ%3BFZ5fUQIdh9Bn-ym3KoGoi7a3iTEkv6fGYdOtOA&dirflg=t&mra=ls&t=m&z=12'
page = br.open(url)
html = page.read()
soup = BeautifulSoup(html)

ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

myfile = "routes_home.txt"

li0 = soup.find("li", id="altroute_0")
li1 = soup.find("li", id="altroute_1")
li2 = soup.find("li", id="altroute_2")
route0 = li0.text.replace("     ", "|").replace("   ", "|") + st + "\n"
route1 = li1.text.replace("     ", "|").replace("   ", "|") + st + "\n"
route2 = li2.text.replace("     ", "|").replace("   ", "|") + st + "\n"

with open(myfile, "a+b") as f:
    f.write(route0)
    f.write(route1)
    f.write(route2)







