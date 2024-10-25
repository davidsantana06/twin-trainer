from dotenv import load_dotenv
from flask import Flask

from . import parameter, path


def _apply_parameters(app: Flask) -> None:
    for key in dir(parameter):
        is_parametter = key.isupper()
        if is_parametter:
            value = getattr(parameter, key)
            app.config[key] = value


def setup_enviroment(app: Flask) -> None:
    load_dotenv(path.ENV_FILE)
    _apply_parameters(app)
