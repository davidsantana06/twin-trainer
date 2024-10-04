from flask import Flask

from .config import configure_enviroment
from .modules import bot, error


app = Flask(__name__)
configure_enviroment(app)
app.register_blueprint(bot)
app.register_blueprint(error)
