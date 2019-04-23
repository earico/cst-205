from flask import Flask, render_template
from flask_bootstrap import Bootstrap

#create an instance of the Flask class
app = Flask(__name__)
bootstrap = Bootstrap(app)

my_dict = {
    'days': ['sun', 'mon', 'tues'],
    'flavors': ['sweet', 'sour', 'salty'],
    'colors': ['red', 'green', 'blue']
}

# route() decorator binds a function to a URL
@app.route('/hello')
def hello():
    return 'Hello world from Flask'

@app.route('/mytemplate')
def t_test():
    return render_template('template.html')

@app.route('/')
def home():
    return render_template('home.html', s_list=my_dict)
