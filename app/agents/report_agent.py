from app.agents.llm import llm
from app.vectorstore.vector_store import vector_store
from langchain_core.prompts import PromptTemplate
from app.prompts.report_prompt import REPORT_PROMPT


class ReportAgent:

    def __init__(self):

        self.name="Report Agent"

        self.max_content= 20000

        self.prompt_template= PromptTemplate(template=REPORT_PROMPT,input_variables=["corpus context"])

    

    def generate_report(self):


        results= vector_store.collection.get(include=["documents"])

        
        documents=results.get("documents",[])

        if not documents:

            return{
                "status":"error",
                "message":"No documents found in vector database"
            }

        print("chunks found:")
        print(len(documents))


        corpus_context=""

        used_chunks=0

        for doc in documents:
            if (len(corpus_context) >= self.max_content ):
                break

            corpus_context+=( doc + "\n\n")

            used_chunks+=1

        print(used_chunks)





        prompt = self.prompt_template.format(corpus_context=corpus_context)

        response = llm.invoke(prompt)

        return {
            "status":"success",
            "report":response.content,
            "chunks_used":used_chunks,
            "context_length":len(corpus_context)

        }


report_agent= ReportAgent()