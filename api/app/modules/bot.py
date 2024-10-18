from flask import Blueprint
from pathlib import Path
from typing import List
import json

from app.config import paths
from app.facades import chat_bot
from app.types import Conversation


bot = Blueprint('bot', __name__, url_prefix='/bot')


# service _

def _get_conversations(path: Path) -> List[Conversation]:
    with open(path, 'r') as file:
        return json.load(file)


@bot.before_app_first_request
def learn_conversations() -> None:
    for path in paths.CONVERSATIONS_DIR.glob('*.json'):
        conversations = _get_conversations(path)
        for conversation in conversations:
            statements = conversation['statements']
            answer = conversation['answer']
            for statement in statements:
                chat_bot.learn(statement, answer)


def _get_answer(statement: str) -> str:
    return chat_bot.answer(statement)


# controller _

@bot.get('/<string:statement>')
def get_answer(statement: str):
    return {
        'statement': statement,
        'answer': _get_answer(statement),
    }
