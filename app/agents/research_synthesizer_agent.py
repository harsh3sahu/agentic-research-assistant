from langchain_core.messages import HumanMessage
from app.agents.llm import llm

from app.prompts.research_synthesizer_prompt import RESEARCH_SYNTHESIZER_PROMPT

class ResearchSynthesizerAgent:

    def __init__ (self):
        self.name= "Research Synthesizer Agent"


    def synthesize(self,findings:str):
        prompt=RESEARCH_SYNTHESIZER_PROMPT.format(findings = findings)

        response = llm.invoke([
            HumanMessage(content=prompt)
        ])

        return response.content
        