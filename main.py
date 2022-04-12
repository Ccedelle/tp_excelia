from helpers import hello
import sys
from bottle import route, run


@route("/")
def homepage():
    return hello()


run(host="0.0.0.0", port=sys.argv[1], reloader=True)
