from flask import Flask
from random import randint as rndi
from flask import render_template as open_tmp

app = Flask(__name__)



@app.route('/')
def index():
    return open_tmp('index.html')


@app.route('/result')
def result():
    this = rndi(0,1)
    
    return open_tmp('result.html',this=this)



