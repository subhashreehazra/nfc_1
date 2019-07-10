import nfc
import ndef
import argparse
from threading import Thread
ap=argparse.ArgumentParser()
ap.add_argument("-u","--uri", required=True,help="add url here")
args=vars(ap.parse_args())
uri=args['uri']

def beam(llc):
    snep_client=nfc.snep.SnepClient(llc)
    snep_client.put_records([ndef.UriRecord(uri)])

def connected(llc):
    Thread(target=beam, args=(llc,)).start()
    return True


clf=nfc.ContactlessFrontend()
assert clf.open('ttyS0') is True
clf.connect(llcp={'on-connect':connected})


