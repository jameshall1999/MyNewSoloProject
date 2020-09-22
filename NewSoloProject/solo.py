import flask, uuid
from flask import request, render_template, flash, url_for, redirect, abort, Response
from forms import PassForm

#---------------------------------------------------------#

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('main.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

app.config['SECRET_KEY'] = 'any secret string'
if __name__ == '__main__':
    #app.config.from_object(Config)
    app.run(host="0.0.0.0", debug=True)

#----------------------------------------------------------#