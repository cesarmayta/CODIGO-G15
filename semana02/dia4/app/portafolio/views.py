from flask import Flask,render_template,request,session

from . import portafolio

from app import fb

@portafolio.route('/')
def index():
    dicBiografia = fb.getCollection('biografia')[0]
    session['biografia'] = dicBiografia
    return render_template('portafolio/index.html')