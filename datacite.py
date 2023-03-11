####
#### Query DataCite API
####

#test doi
#     10.15128/r1c247ds09q

import json
import requests
import sys


def get_pub(doi):
    """Get bibliographic details for doi.

    doi must be in format xx.xxxx/yyyyyyyyy
    """
    API = 'https://api.datacite.org/dois/'
    out = 'zdatacite.json'
  
    print('opening output file ' + out)
    fh = open(out, 'w')

    r = requests.get(API + doi.rstrip())
    if r.status_code == 200:
        try:
            data = r.json()
            print('Found doi')
            print(data)
            bib_string = json.dumps(data)
            fh.write(bib_string)
            fh.close()
            return data
        except ValueError:
            print('ValueError')
    elif r.status_code == 404:
         print('Did not find DOI ' + doi + ' in DataCite database')
         return None

def main():
    get_pub(sys.argv[1])

if __name__ == '__main__':
    sys.exit(main())  #

