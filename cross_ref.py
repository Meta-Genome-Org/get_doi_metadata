import crossref_commons.retrieval
import json
import sys

#test dois
#  10.25250/thescbr.brk569


def get_pub(doi):
    """Get bibliographic details for doi.

    doi must be in format xx.xxxx/yyyyyyyyy
    """

    out = 'zcrossref.json'
    fh = open(out, 'w')
    try:
        data = crossref_commons.retrieval.get_publication_as_json(doi.rstrip())
        print('Found doi')
        print('Creating JSON file ' + out)
        bib_string = json.dumps(data)
        fh.write(bib_string)
        bibrec = read(data)
        print(bibrec)
        return bibrec
    except ValueError:
        print('Did not find DOI ' + doi + ' in Crossref database')
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
    bibrec['author']   = d['author']
    bibrec['title']    = d['title']
    bibrec['journal']  = d['container-title']
    bibrec['volume']   = "vol"
    bibrec['pages']    = "pages"
    bibrec['year']     = d['published']

    return bibrec

def main():
    get_pub(sys.argv[1])

if __name__ == '__main__':
    sys.exit(main())  # 

