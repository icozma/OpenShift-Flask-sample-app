from flask import Flask
from waitress import serve
from handlers import hello

app = Flask(__name__)

app.add_url_rule('/', view_func=hello, methods=['GET'])


