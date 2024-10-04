from chatterbot import ChatBot
from chatterbot.conversation import Statement
from chatterbot.trainers import ListTrainer
from difflib import SequenceMatcher
import random


class ChatBotFacade:
    _FALLBACKS = (
        'Desculpe, não consegui entender.',
        'Sinto muito, não consigo responder isso.',
        'Não entendi. Pode reformular o seu texto?'
    )

    def __init__(
        self,
        name: str,
        minimum_confidence: float,
        database_uri: str
    ) -> None:
        self._chat_bot = ChatBot(
            name=name,
            database_uri=f'{database_uri}?check_same_thread=False',
            read_only=True,
            statement_comparasion_function=self._compare_statements,
            logic_adapter=[{'import_path': 'chatterbot.logic.BestMatch'}]
        )
        self._minimum_confidence = minimum_confidence
        self._trainer = ListTrainer(
            self._chat_bot,
            show_training_progress=False
        )

    def _compare_statements(
        self,
        input: Statement,
        candidate: Statement
    ) -> float:
        confidence = 0.0
        if input.text and candidate.text:
            confidence = SequenceMatcher(
                a=input.text,
                b=candidate.text
            ).ratio()
        return round(confidence, 2)

    def learn(self, statement: str, answer: str) -> None:
        self._trainer.train([statement, answer])

    def _get_fallback(self) -> str:
        return random.choice(self._FALLBACKS)

    def answer(self, statement: str) -> str:
        response = self._chat_bot.get_response(statement.lower())
        is_reliable = response.confidence >= self._minimum_confidence
        return response.text if is_reliable else self._get_fallback()
