import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl



# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_995417.xml"


uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)
sum = 0
results = tree.findall('comments/comment')

for item in results:
    num = int(item.find('count').text)
    sum = sum + num


print(sum)