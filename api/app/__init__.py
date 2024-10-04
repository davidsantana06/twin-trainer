from flask import Flask
from .config import configure_enviroment


app = Flask(__name__)
configure_enviroment(app)
