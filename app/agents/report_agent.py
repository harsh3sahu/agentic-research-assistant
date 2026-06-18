from concurrent.futures import ThreadPoolExecutor
from app.agents.llm import llm
from app.vectorstore.vector_store import vector_store
from app.agents.document_summarizer_agent import document_summarizer_agent
from langchain_core.prompts import PromptTemplate
from app.prompts.report_prompt import REPORT_PROMPT



class ReportAgent:


    def __init__(self):
        self.name="Report Agent"
        self.max_content=60000
        self.max_workers=6
        self.prompt_template=PromptTemplate(
            template=REPORT_PROMPT,
            input_variables=["context","chunks"]
        )



    def split_context(self,text:str):

        context= [text[i:i+self.max_content] for i in range(
            0,len(text),self.max_content
        )]

        return context


    
    def generate_report(self):
        results=(vector_store.collection.get(include=["documents"]))

        documents= results.get("documents",[])

        print(type(documents))


        if not documents:
            return {
                "status":"error",
                "message":"No documents in vector database"
            }

        # print("corpus report----------------")
        # print(len(documents))

        corpus_context= ""
        used_chunks=0

        for doc in documents:

            corpus_context+=( doc + "\n\n")

            used_chunks+=1

        print(used_chunks)

        # print("corpus context----------")
        # print(len(corpus_context))



        contexts= self.split_context(corpus_context)





        # =======================
#  now parallel summarization code, this will summarize the corpus context chunks all at once, first we will break the corpus to max_length

        

        with ThreadPoolExecutor(max_workers=5) as executor:

            summaries=list(
                executor.map(document_summarizer_agent.summarize,contexts)
            )

            print("all summaries generated")
            print(len(summaries))



        total_summary= "\n\n".join(summaries)



        # now final report

        prompt=self.prompt_template.format(corpus_context=total_summary)


        response=llm.invoke(prompt)

        with open("report.txt","w",encoding="utf-8")as f:
            f.write(response.content)


        return {
            "status":"success",
            "report":response.content
        }


report_agent=ReportAgent()







