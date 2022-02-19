from flask import Flask,render_template,request

app = Flask(__name__,template_folder="tmp")

auth = {'username' : 'masih','password':'013'}

@app.route('/',methods=['GET','POST'])
def index():
    rh = request.args.get('get_name')
    return render_template('index.html',rh=rh)


@app.route('/login',methods=["POST","GET"])
def login():
    return render_template("login_pg.html")

@app.route('/submit',methods=["POST",'GET'])
def submit():
    user = request.form['username'] # Or Get
    passwd = request.form.get['password']
    if user.lower() == auth['username'] and passwd == auth['password']:
        return "Logined"
    return "You Are Not"