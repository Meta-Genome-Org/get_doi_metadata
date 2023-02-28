import crossref_commons.retrieval
import json
import sys

def get_pub(doi):
    """Get bibliographic details for doi.

    doi must be in format xx.xxxx/yyyyyyyyy
    """

    out = 'record.json'
    fh = open(out, 'w')
    try:
        data = crossref_commons.retrieval.get_publication_as_json(doi.rstrip())
        print('Found doi')
        print('Creating JSON file ' + out)
        print(data)
        bib_string = json.dumps(data)
        fh.write(bib_string)
        return data
    except ValueError:
        print('Did not find DOI ' + doi + ' in Crossref database')

"""   
    try:
        data = bib.json()
    except ValueError:
        print('Invalid JSON')
    json_string = json.dumps(bib.json())
    print(json_string)
"""



def main():
    get_pub(sys.argv[1])


if __name__ == '__main__':
    sys.exit(main())  # 



