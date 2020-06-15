
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
co = int(input('Enter count:'))
po = int(input('Enter position:'))

def find(url,i):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    print('Retrieving:', tags[po-1].get('href', None))
    return tags[po-1].get('href', None), tags[po-1].contents[0]


for i in range(co):
    url, output = find(url, i)
print(output)