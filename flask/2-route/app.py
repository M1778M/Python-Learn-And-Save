from flask import Flask

app = Flask(__name__)

def t_p(value,style={}):
    if style=={}:
        return "<p>{}</p>".format(value)
    else:
        try:
            color = style['color']
            bgcolor = style['bgcolor'] or style['background-color']
            border = style['border'] 
        except Exception:
            pass
        return '<p style="color:{};background-color:{};border:{}">{}</p>'.format(color,bgcolor,border,value)
        



@app.route('/')
def index():
    return "<h1>Wellcome To Index</h1>"

@app.route('/help')
def help_():
    return "<script>alert('This Page Is Help');</script>"

@app.route('/HelloTM')
def hello_To_Me():
    name = "Ali"
    return("<p>Hello {}".format(name) + t_p("Yo Whatsup",style={'bgcolor':'red','color':'#fff','border':'1px solid #000'}))


#variable To Link / open link white your name and see
@app.route('/Hello/<var_name>') # variable is ok
def hello_to_var_name(var_name):
    return t_p("Hello {}".format(var_name),style={'color':'black','bgcolor':'green','border':'2px solid white'})


#variable Type
@app.route('/age/<int:your_age>') # string , int , float , bool ...... and path / path dont read '/' exp [myweb.com/helloMe/ali_/01]
def show_age(your_age):
    return 'you are {}'.format(str(your_age))






