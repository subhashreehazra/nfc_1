# try:
from flask import Flask, flash, redirect, render_template, request, session, abort
import nfc
import ndef
from threading import Thread
from flask import json
app = Flask(__name__)

@app.route('/nfc/',methods = ['POST', 'GET'])
def nfc(): 
    if request.method == 'POST':
        vpa=request['VPA']
        amn=request.form['Amount']
        mer=request.form['Merchant']
        uri="upi://pay?pa="+vpa+"&pn="+mer+"&am="+amn+"&tn=&mam=null&cu=INR"

        def beam(llc):
            snep_client=nfc.snep.SnepClient(llc)
            snep_client.put_records([ndef.UriRecord('www.google.com')])

        def connected(llc):
            Thread(target=beam, args=(llc,)).start()
            return True

        clf = nfc.ContactlessFrontend()
        assert clf.open('ttyS0') is True
        clf.connect(llcp={'on-connect': connected})
        if(clf.connect()):
            return("True") 
# except ImportError:
    #return render_template("demo.html")         
if __name__ == "__main__":
    app.run()


