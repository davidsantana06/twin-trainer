from flask import Blueprint
from http import HTTPStatus
from werkzeug.exceptions import HTTPException, InternalServerError


error = Blueprint('error', __name__)


# service _

def _get_code(e: Exception) -> int:
    is_http_exception = isinstance(e, HTTPException)
    return e.code if is_http_exception else InternalServerError.code


def _get_description(code: int) -> str:
    return {
        404: 'Opa, página não encontrada!',
        500: 'Ih, o servidor está com problemas!',
    }.get(code, 'Algo deu errado, aguente firme!')


# controller _

@error.app_errorhandler(HTTPException)
def handle_exception(e: HTTPException):
    code = _get_code(e)
    description = _get_description(code)
    return ({'message': description}, HTTPStatus(code))
