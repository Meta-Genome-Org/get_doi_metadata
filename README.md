# Get bibliographic information for one DOI

## Requirements 
pip3 install crossref-commons


## Usage: 
    >>> import cross_ref
    >>> cross_ref.get_pub(doi)

    Returns a Python dictionary with structure:
    
    {
    'author': [
       {'ORCID': 
            'http: //orcid.org/0000-0001-5966-6083', 
            'authenticated-orcid': True, 
            'given': 'Harrison J.', 
            'family': 'Cox', 
            'sequence': 'first', 
            'affiliation': [
                {'name': 'Department of Chemistry, Durham University, Durham DH1 3LE, England, U.K.'
                }
             ]
        },
        {'given': 'Gary J.', 
            'family': 'Sharples', 
            'sequence': 
            'additional', 
            'affiliation': [
                {'name': 'Department of Biosciences, Durham University, Durham DH1 3LE, England, U.K.'
                }
            ]
        },
        {'ORCID': 
            'http: //orcid.org/0000-0002-5086-5737', 
            'authenticated-orcid': True, 
            'given': 'Jas Pal S.', 
            'family': 'Badyal', 
            'sequence': 'additional', 
            'affiliation': [
                {'name': 'Department of Chemistry, Durham University, Durham DH1 3LE, England, U.K.'
                }
            ]
        }
    ], 
    'title': ['Tea–Essential Oil–Metal Hybrid Nanocoatings for Bacterial and Viral Inactivation'
    ], 
    'journal': ['ACS Applied Nano Materials'
    ], 
    'issue': '11', 
    'volume': '4', 
    'pages': '12619-12628', 
    'pub_year': 2021
    }
    


## Execute module as a script:

**python3 cross_ref.py prefix/suffix**

> Example 1:
  python3 cross_ref.py 10.1021/acsanm.1c03151
    
  Returns dictionary above.
    
> Example 2:
  python3 cross_ref.py 10.25250/thescbr.brk569
  
    {
        'author': [
            {'given': 'Stefan', 'family': 'Szyniszewski', 'sequence': 'first', 'affiliation': []}, 
            {'given': 'Miranda', 'family': 'Anderson', 'sequence': 'additional' , 'affiliation': []}], 
        'title': ['Non-cuttable material inspired by seashells'], 
        'journal': ['TheScienceBreaker'], 
        'issue': '03', 
        'volume': '07', 
        'pages': '', 
        'pub_year': 2021
    }

