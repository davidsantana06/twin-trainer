from typing import TypedDict, List


class Conversation(TypedDict):
    statements: List[str]
    answer: str
