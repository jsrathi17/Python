import json
import urllib.request, urllib.parse, urllib.error
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
address = input('Enter location: ')
print('Retrieving', address)
uh = urllib.request.urlopen(address, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')
info = json.loads(data)
X=[]
for i in range(len(info["comments"])):
    X.append(info['comments'][i]['count'])
print('Count:', len(X))
print('Sum:', sum(X))