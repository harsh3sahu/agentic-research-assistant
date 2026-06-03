from langchain_core.messages import HumanMessage
from app.agents.llm import llm
from app.prompts.mode_router_prompt import MODE_ROUTER_PROMPT

class ModeRouterAgent:

    def __init__(self):
        self.name="Mode Router Agent"

    def route(self,query:str):

        prompt=MODE_ROUTER_PROMPT.format(query=query)

        response=llm.invoke([
            HumanMessage(content=prompt)
        ])

        return response.content.strip().lower()