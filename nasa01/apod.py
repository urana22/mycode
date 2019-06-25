import urllib.request
import json
import webbrowser

apodurl = 'https://api.nasa.gov/planetary/apod?'
mykey = 'api_key=sYgx1ZeQh4Ii1O6LGEj5zlTEqivY371bJlpBsjMM'

apodurlobj = urllib.request.urlopen(apodurl + mykey)

apodread = apodurlobj.read()

decodeapod = json.loads(apodread.decode('utf-8'))

print('\n\nConverted python data')
print(decodeapod)

input('\n Press Enter to open NASA Picture of the Day in Browser')
webbrowser.open(decodeapod['url'])
