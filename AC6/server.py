from flask import Flask

App = Flask(__name__)

from errorhandler import *
from routes import *


if __name__ == "__main__":
    App.run(port=8080)
