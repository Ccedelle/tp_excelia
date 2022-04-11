from helpers import hello
from bottle import route, run


@route('/')
def homepage():
    return hello()


run(host='localhost', port=8080, reloader=True)
