from langchain_core.messages import HumanMessage
from app.agents.llm import llm

from app.prompts.revise_prompt import REVISE_PROMPT

class ReviseAgent:

    def __init__(self):
        self.name="Replanner Agent"

    def revise(self,query:str,critique:str,answer:str,context:str):
        prompt= REVISE_PROMPT.format(
            query=query,
            critique=critique,
            answer=answer,
            context=context
        )

        response=llm.invoke([HumanMessage(content=prompt)])
        
        return response.content