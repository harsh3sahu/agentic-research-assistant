from langchain_core.messages import HumanMessage
from app.agents.llm import llm

from app.prompts.summarizer_prompt import SUMMARIZER_PROMPT

class SummarizerAgent:

    def __init__(self):
        self.name="Summarizer Agent"


    def summarize(self,query:str,context:str):

        prompt=(SUMMARIZER_PROMPT.format(query=query,context=context[:6000]))

        try:
            response = llm.invoke(
                [
                    HumanMessage(content=prompt)
                ]
            )

            return {
                "status":"success",
                "summary":response.content
            }


        except Exception as e:
            return{
                "status":"error",
                "message":str(e)
            }



