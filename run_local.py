from flask import Flask
from waitress import serve
from handlers import hello
from app import app

if __name__ == '__main__':
    # serve(app, host='0.0.0.0', port=8080)
    app.run(host='0.0.0.0', port=8080)
