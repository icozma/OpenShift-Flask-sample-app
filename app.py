from flask import Flask
from waitress import serve
from handlers import hello

app = Flask(__name__)

app.add_url_rule('/', view_func=hello, methods=['GET'])

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
    # app.run(host='0.0.0.0', port=8080)
