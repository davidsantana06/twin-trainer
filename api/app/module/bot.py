from flask import Blueprint
from pathlib import Path
from typing import List
import json

from app.config import path
from app.facade import chat_bot_facade
from app.typing import Conversation


bot = Blueprint('bot', __name__, url_prefix='/bot')


# service _

def _get_conversations(file_path: Path) -> List[Conversation]:
    with open(file_path, encoding='utf-8') as file:
        return json.load(file)


@bot.before_app_first_request
def learn_conversations() -> None:
    for file_path in path.CONVERSATIONS_DIR.glob('*.json'):
        conversations = _get_conversations(file_path)
        for conversation in conversations:
            statements = conversation['statements']
            answer = conversation['answer']
            for statement in statements:
                chat_bot_facade.learn(statement, answer)


def _normalize_statement(content: str) -> str:
    return content.lower().rstrip()


def _get_answer(statement: str) -> str:
    return chat_bot_facade.answer(statement)


# controller _

@bot.get('/<string:statement>')
def get_answer(statement: str):
    statement = _normalize_statement(statement)
    return {
        'statement': statement,
        'answer': _get_answer(statement),
    }
