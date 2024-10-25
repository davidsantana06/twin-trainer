from flask import Blueprint
from http import HTTPStatus
from werkzeug.exceptions import HTTPException


error = Blueprint('error', __name__)


# service _

def _get_code(e: Exception) -> int:
    is_http_exception = isinstance(e, HTTPException)
    return e.code if is_http_exception else 500


# controller _

@error.app_errorhandler(HTTPException)
def handle_exception(e: HTTPException):
    code = _get_code(e)
    return (
        {'message': 'Ocorreu um erro inesperado.'},
        HTTPStatus(code)
    )
