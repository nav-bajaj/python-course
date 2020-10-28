# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Maiah.html'
urltemp = str()
linknum = 18
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
i=0
# Retrieve all of the anchor tags
tags = soup('a')

while i < 7 :
    urltemp = str()
    linknum = 18
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    
# Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags[0:linknum]:
        urltemp = tag.get('href', None)
    url = urltemp
    print(url)    
    i = i+1
        
answer = url.split("_")
name = answer[2].split(".")

print(name[0])
