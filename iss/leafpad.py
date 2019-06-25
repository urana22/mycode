
import urllib.request
import json

majortom='http://api.open-notify.org/astros.json'

groundctrl = urllib.request.urlopen(majortom)

helmet= groundctrl.read()

helmetson= json.loads(helmet.decode('utf-8'))

#print('\n\n Converted python data')
#print(helmetson)

print('People In Space: ', helmetson['number'])
people = helmetson['people']

#print(people)

for a in people:
    print(a.get('name') + " on the " + a.get('craft'))
