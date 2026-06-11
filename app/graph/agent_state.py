from typing import TypedDict

class AgentState(TypedDict):
    query:str
    
    route: str

    context: str

    answer : str

    confidence: float

    critique: str

    sources: list

    research_tasks:list

    research_findings:str

    report:str

    mode: str

    retry_count: int

    replan_task:str

    final_ans:str

