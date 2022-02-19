from flask import Flask

from flask import render_template as open_tmp

app = Flask(__name__)



@app.route('/')
def index():
    return open_tmp('index.html')
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 