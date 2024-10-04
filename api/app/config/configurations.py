from dotenv import load_dotenv
from flask import Flask

from . import parameters, paths


def _apply_parameters(app: Flask) -> None:
    for key in dir(parameters):
        is_parametter = key.isupper()
        if is_parametter:
            value = getattr(parameters, key)
            app.config[key] = value


def configure_enviroment(app: Flask) -> None:
    load_dotenv(paths.ENV_FILE)
    _apply_parameters(app)
