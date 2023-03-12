####
#### Query DataCite API
####

# test doi
# Syrotiuk:    10.15128/r1c247ds09q
# Breckon:     10.5281/zenodo.3338077

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
#            print(data)
            bib_string = json.dumps(data)
            fh.write(bib_string)
            fh.close()
            bibrec = read(data)
            print(bibrec)
            return bibrec
        except ValueError:
            print('ValueError')
    elif r.status_code == 404:
         print('Did not find DOI ' + doi + ' in DataCite database')
         return None

def read(d):

    """bibrecord = 
    author=['J. Timmer', 'M. König'],
    title="On generating power law noise",
    journal="Astronomy and Astrophysics",
    volume="300",
    pages="707--710",
    year="1995"
    """
    
    bibrec = dict(author = [], title = "", journal = "", volume = "", pages = "", year = "")
    bibrec['author']   = d['data']['attributes']['creators']
    bibrec['title']    = d['data']['attributes']['titles']
#    bibrec['journal']  = d['data']['attributes'][['container-title']
#    bibrec['volume']   = d['data']['attributes'][['volume']
    try:
        bibrec['pages'] = d['data']['attributes']['page']
    except KeyError:
        print("Did not find pages")
    bibrec['year']      = d['data']['attributes']['publicationYear']

    return bibrec

def main():
    get_pub(sys.argv[1])

if __name__ == '__main__':
    sys.exit(main())  #

