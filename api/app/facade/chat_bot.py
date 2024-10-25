from chatterbot import ChatBot
from chatterbot.conversation import Statement
from chatterbot.trainers import ListTrainer
from difflib import SequenceMatcher
import random


class ChatBotFacade:
    __FALLBACKS = (
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
        self.__chat_bot = ChatBot(
            name=name,
            database_uri=f'{database_uri}?check_same_thread=False',
            read_only=True,
            statement_comparasion_function=self.__compare_statements,
            logic_adapter=[{'import_path': 'chatterbot.logic.BestMatch'}]
        )
        self.__minimum_confidence = minimum_confidence
        self.__trainer = ListTrainer(
            self.__chat_bot,
            show_training_progress=False
        )

    def __compare_statements(
        self,
        input: Statement,
        candidate: Statement
    ) -> float:
        confidence = 0
        if input.text and candidate.text:
            confidence = SequenceMatcher(
                input.text,
                candidate.text
            ).ratio()
        return round(confidence, 2)

    def learn(self, statement: str, answer: str) -> None:
        self.__trainer.train([statement, answer])

    def _get_fallback(self) -> str:
        return random.choice(self.__FALLBACKS)

    def answer(self, statement: str) -> str:
        response = self.__chat_bot.get_response(statement)
        is_reliable = response.confidence >= self.__minimum_confidence
        return response.text if is_reliable else self._get_fallback()
