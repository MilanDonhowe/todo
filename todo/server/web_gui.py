# flask websever script

from flask import Flask, render_template
from ..crud import crud



todoList = crud.System()
todoApp = Flask(__name__)

@todoApp.route('/')
def index():
    return "<h1>¡Hola Mundo!</h1>"


@todoApp.route('/todo/')
def temp():
    
    # format the todo list into a list
    '''
    responseList = "<ol>"
    
    for i in todoList.read():
        responseList += ("<li>" + str(i) + "</li>")
    responseList += "</ol>"
    '''
    return render_template("todo.html", myList=todoList.read())



#@todoApp.route('/todo/<data>')
#def todo(data):
#    return f"<p>this is interesting info: {data}</p>"
# return render_template('user.html', data=data)
#

# for testing purposes
if __name__ == "todo.server.web_gui":
    todoApp.run()

"""








"""