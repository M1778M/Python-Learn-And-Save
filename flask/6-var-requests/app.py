from flask import Flask , render_template,request
from requests import get
app = Flask(__name__,template_folder='tmp')


@app.route('/')
def index():

    return "Wait..."
@app.route('/rq')
def rq():
    res = "Request Con\n<br/>"
    res += "Request Meth {}".format(request.method)
    res += f"<br/>request get args: {request.args}"
    # request.args.get("name")
    res += f"<br/>FORM Body/Data: {request.form}" # form / data

    return res + "<br/>" + request.args.get("name") + "<br/>" + str(request.args.getlist('lastname'))

@app.route('/post',methods=['POST','GET'])
def pos():
    return "NICE POST"

@app.route('/get')
def get_():
    site = request.args.get("site")
    gv = get(site).text
    return str(gv)