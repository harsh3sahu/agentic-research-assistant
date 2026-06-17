from app.prompts.document_summarizer import DOCUMENT_SUMMARIZE_PROMPT
from app.agents.llm import llm


class DocumentSummarizerAgent:


    def __init__(self):
        self.name="Document Sumaarizer Agent"


    def summarize(self,context:str):

        prompt= DOCUMENT_SUMMARIZE_PROMPT.format(context=context)

        response= llm.invoke(prompt)

        return response.content

document_summarizer_agent=DocumentSummarizerAgent()