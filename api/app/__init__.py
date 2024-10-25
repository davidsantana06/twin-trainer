from flask import Flask

from .config import setup_enviroment
from .module import bot, error


app = Flask(__name__)
setup_enviroment(app)
app.register_blueprint(bot)
app.register_blueprint(error)
