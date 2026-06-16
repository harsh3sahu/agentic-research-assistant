from langchain_core.messages import HumanMessage
from app.agents.llm import llm
from app.tools.rag_tool import RAGTool
from app.tools.web_search_tool import WebSearchTool
from app.rag.retriever import retriever


from app.prompts.summarizer_prompt import SUMMARIZER_PROMPT

class SummarizerAgent:

    def __init__(self):
        self.name="Summarizer Agent"
        self.rag_tool=RAGTool(retriever)
        self.web_tool=WebSearchTool()


    def summarize(self,query:str):


        # ragtool
        try:

            result = self.rag_tool.run(query)
            context=result.get("context","")
            sources=result.get("sources","")

            # check

            if len(context.strip()) == 0 or len(sources)==0:
                print("-"*50)
                print("web result")
                
                result=self.web_tool.run(query)
                context=result["context"]
                sources=result["sources"]
                print(result)



           
            

            prompt=(SUMMARIZER_PROMPT.format(query=query,context=context[:6000]))

            response = llm.invoke([HumanMessage(content=prompt)])

            print("="*50)
            print("RESPONSE")
            print(response)



             
            return {
                    "status":"success",
                    "summary":response.content,
                    "context":context,
                    "sources":sources
                }



        except Exception as e:
            return{
                "status":"error",
                "message":str(e)
            }










        # prompt=(SUMMARIZER_PROMPT.format(query=query,context=context[:6000]))

        # try:
        #     response = llm.invoke(
        #         [
        #             HumanMessage(content=prompt)
        #         ]
        #     )

        #     return {
        #         "status":"success",
        #         "summary":response.content
        #     }


        # except Exception as e:
        #     return{
        #         "status":"error",
        #         "message":str(e)
        #     }



