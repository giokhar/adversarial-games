from bottle import route, run, template, request, static_file
from main import start_web, end_web, o_strategy, x_strategy
import os

print("Please wait till server runs !")

@route('/')
def index():
	return template('views/index', table = start_web(), moves = end_web(), o = o_strategy, x = x_strategy)

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

@route('static/img/:path#.+#')
def send_static(filename):
    return static_file(filename, root='static/img') 
	
run(host='localhost', port=8080, debug=False, reloader=False)
