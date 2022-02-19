from flask import Flask,render_template

app = Flask(__name__,template_folder="tmp")


@app.route('/')
def index():
    names = ["ali",'reza','gholam']
    names2 = names + ['mamad','abol']
    fori = [i for i in range(20) ]
    return render_template("index.html",names=names,names2=names2,fori=fori)

