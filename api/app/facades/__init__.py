from app.config import parameters
from .chat_bot import ChatBotFacade


chat_bot = ChatBotFacade(
    name='Twin Trainer',
    minimum_confidence=0.75,
    database_uri=parameters.DATABASE_URI,
)
