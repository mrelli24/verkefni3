import bottle
from bottle import *
bottle.debug(True)

#A liður - mappan "view" á að nefna "views"

@route("/")
def index():
    return """
    <h2>Verkefni 3</h2>
    <p> <a href="/a">Liður A</a></p>
    <p> <a href="/b">Liður B</a></p>
"""

@route("/a")
def index():
    return template("temp-A.tpl")

@route("/sida/<kt>")
def page(kt):
    return template("temp-kt.tpl", kt=kt)

#B liður

@route("/Static/<skra>")
def stati_skra(skra):
    return static_file(skra, root='./static')

@route("/b")
def index():
    return template("index.tpl")



##############################################

@error(404)
def villa(error):
    return "<h2 style = color:red>Þessi síða finnst ekki</h2>"

run(host="0.0.0.0", port=os.environ.get('PORT'))
