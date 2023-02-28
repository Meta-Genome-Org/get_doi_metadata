


from get_doi_metadata import cross_ref

class CancelledError(Exception): pass

def main():
    while True:
        try:
            cross_ref.get_pub(doi)

