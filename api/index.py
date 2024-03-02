from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'loda Sanu muno pogi jaje nakkar ricksha ma aavavu padase, CHARUSAT ni placement policy joi nathi and bhai ne T&C jovi chhe.'

@app.route('/about')
def about():
    return 'About'