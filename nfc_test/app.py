
from flask import Flask, flash, redirect, render_template, request, session, abort,Response
import nfc
import ndef
from threading import Thread
from flask import json
import os
app = Flask(__name__)

@app.route('/', methods=["POST","GET"])
def nfc():
    if request.method == "POST":
        vpa=request.form['VPA']
        amn=request.form['Amount']
        mer=request.form['Merchant']
        uri="upi://pay?pa="+vpa+"&pn="+mer+"&am="+amn+"&tn=&mam=null&cu=INR"
        os.system('python ndef_url.py -u \"'+uri+'\"')
        return Response(status=200)
    else:
        return Respose(status=400)

if __name__ == "__main__":
    app.run()


