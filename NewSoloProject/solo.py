import flask, uuid
from flask import request, render_template, flash, url_for, redirect, abort, Response



#-----------------------------------------------------------------------------------

class Member:

    def __init__(self, firstname, lastname, role):
        self.firstname = firstname
        self.lastname = lastname
        self.email = firstname + "." + lastname + "@email.com"
        self.role = role

class MembersList:

    def __init__(self):
        self.members = []

    def add_member(self, firstname, lastname, role):
        self.members.append(Member(firstname, lastname, role)) 

    def remove_member(self, Rfirstname, Rlastname, Rrole):
        remove_from_list = next(d for d in self.members if d.firstname == Rfirstname and d.lastname == Rlastname and d.role == Rrole)
        self.members.remove(remove_from_list)   

    def display_members(self):
        displayList = []
        for member in self.members:
            displayList.append("Fistname: " + member.firstname)
            displayList.append("Lastname: " + member.lastname)
            displayList.append("Email: " + member.email)
            displayList.append("Job role: " + member.role)
            displayList.append(" ------------------------------------------------")
            location = self
        return displayList
    

#-------------------------------------------------------------------------------------

app = flask.Flask(__name__)
members_list = MembersList()

members_list.add_member("John", "Marston", "manager")
members_list.add_member("Arthur", "Morgan", "Programmer")
members_list.add_member("Mrs", "Graphics", "Graphic designer")
members_list.add_member("Everyday", "Joe", "Accounts")

@app.route('/', methods=['GET'])
def home():
    return render_template('main.html', displayList = members_list.display_members())

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/add')
def my_form():
    return render_template('formpage.html')

@app.route('/add', methods=['POST'])
def my_form_post():
    firstname = request.form['formFirstname']
    lastname = request.form['formLastname']
    role = request.form['formRole']
    members_list.add_member(firstname, lastname, role)
    return "success"

@app.route('/del')
def my_del_form():
    return render_template('delformpage.html')

@app.route('/del', methods=['POST'])
def my_form_del():
    Rfirstname = request.form['delformFirstname']
    Rlastname = request.form['delformLastname']
    Rrole = request.form['delformRole']
    members_list.remove_member(Rfirstname, Rlastname, Rrole)
    return "success"

app.config['SECRET_KEY'] = 'any secret string'
if __name__ == '__main__':
    #app.config.from_object(Config)
    app.run(host="0.0.0.0", debug=True)



