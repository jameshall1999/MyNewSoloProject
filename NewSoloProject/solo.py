import flask, uuid
from flask import request, render_template, flash, url_for, redirect, abort, Response


#---------------------------------------------------------

class Member:

    Memberlist = []
    Testlist = []

    def __init__(self, firstname, lastname, role):
        self.firstname = firstname
        self.lastname = lastname
        self.email = firstname + "." + lastname + "@email.com"
        self.role = role
        self.fulldetails = "Name: " + firstname + " " + lastname + " " + "Email: " +  self.email + " " + "Role: " + role
        Member.Memberlist.append(self.fulldetails) 
        Member.Testlist.append("Fistname: " + self.firstname)
        Member.Testlist.append("Lastname: " + self.lastname)
        Member.Testlist.append("Email: " + self.email)
        Member.Testlist.append("Job role: " + self.role)
        Member.Testlist.append(" ------------------------------------------------")

dev1 = Member("John", "Marston", "manager")
dev2 = Member("Arthur", "Morgan", "Programmer")
dev3 = Member("Mrs", "Graphics", "Graphic designer")
dev4 = Member("Everyday", "Joe", "Accounts")
#---------------------------------------------------------

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    teamlist = Member.Memberlist
    mytestlist = Member.Testlist
    return render_template('main.html', teamlist = teamlist, mytestlist = mytestlist)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

app.config['SECRET_KEY'] = 'any secret string'
if __name__ == '__main__':
    #app.config.from_object(Config)
    app.run(host="0.0.0.0", debug=True)



