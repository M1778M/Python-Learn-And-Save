from flask import Flask

app = Flask(__name__)

#Live Prewive [set FLASK_ENV=development] or [set FLASK_DEBUG=1]

def welcom():
    return '<h2 style="background-color:rgb(150,40,20);">Hello</h2>'

@app.route('/')   #Can you Get / for exp /index or /main/server and .....
@app.route('/hellome') # can has more page one function
def Hello():
    return "<p>Hello<p>"+welcom()+'<h4 style="color:red">Hello</h4>'



 

