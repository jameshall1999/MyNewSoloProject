import flask, uuid
from flask import request, render_template, flash, url_for, redirect, abort, Response


#---------------------------------------------------------

class Member:

    Memberlist = []

    def __init__(self, firstname, lastname, role):
        self.firstname = firstname
        self.lastname = lastname
        self.email = firstname + "." + lastname + "@email.com"
        self.role = role
        self.fulldetails = "Name: " + firstname + " " + lastname + " " + "Email: " +  self.email + " " + "Role: " + role
        Member.Memberlist.append(self.fulldetails) 
        
dev1 = Member("John", "Marston", "manager")
dev2 = Member("Arthur", "Morgan", "Programmer")

#---------------------------------------------------------

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    teamlist = Member.Memberlist
    return render_template('main.html', teamlist = teamlist)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

app.config['SECRET_KEY'] = 'any secret string'
if __name__ == '__main__':
    #app.config.from_object(Config)
    app.run(host="0.0.0.0", debug=True)



