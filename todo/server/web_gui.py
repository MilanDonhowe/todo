# flask websever script

from flask import Flask, render_template, request
from ..crud import crud
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, StringField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap

todoList = crud.System()
todoApp = Flask(__name__)
bootstrap = Bootstrap(todoApp)


# super secret key
# in real flask applications this should be instead set as an enviromental variable
# having it declared in the source code is not super secure.
todoApp.config["SECRET_KEY"] = 'He1234S1247'


# forms

class AgeForm(FlaskForm):
    age = IntegerField("How old are you?", validators=[DataRequired()])
    submit = SubmitField("Submit")

class newEntry(FlaskForm):
    entry = StringField("ADD: ", validators=[DataRequired()])
    submit = SubmitField("Add")

class delEntry(FlaskForm):
    deleteEntry = StringField("DEL: ", validators=[DataRequired()])
    submit = SubmitField("Delete")

# url mapping


@todoApp.route('/')
def index():
    return "<h1>¡Hola Mundo!</h1>"


@todoApp.route('/todo/', methods=['GET', 'POST'])
def temp():
    thisEntry = None
    addForm = newEntry()
    delForm = delEntry()

    # remove value
    if "delNumber" in request.form:
        removableKey = request.form["delNumber"]
        todoList.delete(todoList.readFromKey(str(removableKey)))


    # if the user removes a value
    if delForm.validate_on_submit():
        removableEntry = delForm.deleteEntry.data
        todoList.delete(removableEntry)
        delForm.deleteEntry.data = None


    # if the user adds a new value
    if addForm.validate_on_submit():
        thisEntry = addForm.entry.data
        print(thisEntry)
        todoList.create(thisEntry)
        addForm.entry.data = None
    
    return render_template("todo.html", myList=todoList.read(), addForm=addForm, delForm=delForm)

#@todoApp.errorhandler(404)
# def page_not_found(error):
#   return render_template('404.html), 404


#@todoApp.route('/todo/<data>')
#def todo(data):
#    return f"<p>this is interesting info: {data}</p>"
# return render_template('user.html', data=data)
#

# for testing purposes
if __name__ == "todo.server.web_gui":
    todoApp.run(port=6234)

"""








"""