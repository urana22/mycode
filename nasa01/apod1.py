import urllib.request
import json
import webbrowser
from pprint import pprint as pp

NASAAPI= 'https://api.nasa.gov/planetary/apod?'
MKEY ='api_key=sYgx1ZeQh4Ii1O6LGEj5zlTEqivY371bJlpBsjMM'

def main():
    nasaapiobj= urllib.request.urlopen(NASAAPI + MKEY)
    nasaread=nasaapiobj.read()
    convertedjson=json.loads(nasaread.decode('utf-8'))


    print(convertedjson)
    input('\nThis is converted json. Press Enter to continue:')
    pp(convertedjson)

    # pprint.pprint(convertedjson)

    input('\n This is pretty printed JSON. Press Enter to continue:')

    print(convertedjson['explanation'])
    input('\n Press ENTER to view this photo of the day')

    webbrowser.open(convertedjson['hdurl'])


main()
