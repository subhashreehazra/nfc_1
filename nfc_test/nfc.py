import nfc
import nfc.snep
import ndef
import threading

server = None
uri='google.com'

def send_ndef_message(llc):
   sp_record = ndef.SmartposterRecord(uri, 'UPI - Link')
   nfc.snep.SnepClient(llc).put_records( [sp_record] )

def startup(llc):
   global server
   server = nfc.snep.SnepServer(llc, "urn:nfc:sn:snep")
   return llc

def connected(llc):
   server.start()
   threading.Thread(target=send_ndef_message, args=(llc,)).start()
   return True

clf = nfc.ContactlessFrontend()
assert clf.open('ttyS0') is True
clf.connect(llcp={'on-startup': startup, 'on-connect': connected})