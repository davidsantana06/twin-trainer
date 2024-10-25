from app.config import parameter
from .chat_bot import ChatBotFacade


chat_bot_facade = ChatBotFacade(
    name='Twin Trainer',
    minimum_confidence=0.75,
    database_uri=parameter.DATABASE_URI
)
