from typing import TypedDict

class AgentState(TypedDict):
    query:str
    
    route: str

    context: str

    answer : str

    confidence: float

    critique: str

    sources: list