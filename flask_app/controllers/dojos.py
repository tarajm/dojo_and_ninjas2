from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo


@app.route('/')
def index():
    return redirect('/dojos')

#this is for the class method Read (ALL)
@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template("index.html",all_dojos = dojos)

#this is for the class method Create
@app.route('/create/dojo',methods=['POST'])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')


#Show route...shows us 1 ID
#needs a data dictionary so it shows the data associated with the id
@app.route('/dojo/<int:id>')
def show_dojo(id):
    data = {
        "id": id
    }
    return render_template('dojo.html', dojo=Dojo.get_one_with_ninjas(data))