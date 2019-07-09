# try:
from flask import Flask, flash, redirect, render_template, request, session, abort
import nfc
import nfc.snep
import ndef
import threading
from flask import json
app = Flask(__name__)

@app.route('/nfc/',methods = ['POST', 'GET'])
def nfc(): 
    if request.method == 'POST':
        vpa=request['VPA']
        amn=request.form['Amount']
        mer=request.form['Merchant']
        server = None
        uri="upi://pay?pa="+vpa+"&pn="+mer+"&am="+amn+"&tn=&mam=null&cu=INR"

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
        if(clf.connect()):
            return("True") 
# except ImportError:
    #return render_template("demo.html")         
if __name__ == "__main__":
    app.run()


