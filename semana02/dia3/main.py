from flask import Flask,render_template,request
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from FirebaseAdmin import FirebaseAdmin

cred = credentials.Certificate("token.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

app = Flask(__name__)

@app.route('/')
def index():
    fb = FirebaseAdmin(db)
    dicBiografia = fb.getCollection('biografia')[0]
    print(dicBiografia)
    return render_template('index.html',**dicBiografia)

app.run(debug=True)