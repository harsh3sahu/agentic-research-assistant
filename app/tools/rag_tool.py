from app.agents.llm import llm

from langchain_core.messages import HumanMessage


class RAGTool:
    def __init__(self,retriever):
        self.retriever=retriever


    def run(self,query:str,top_k:int=5, min_score:float=0.2):
        results=self.retriever.retrieve(
            query=query,
            top_k=top_k,
            score_threshold=min_score
        )

        if not results:
            return{
                "answer":
                    "no relevant information found",
                "sources":[],
                "confidence":0.0
            }

        context= "\n\n".join(
            [
                doc["content"]
                for doc in results
            ]
            )

        prompt= f"""
        Answer the question using ONLY the context.

        Question:
        {query}

        Context:
        {context}

        Answer:
        """

        response =llm.invoke([
            HumanMessage(content=prompt)
        ])

        sources=[
            {
                "source": doc["metadata"].get("source_file","unknown"),
                "page":doc["metadata"].get("page","unknown"),
                "score":doc["similarity_score"]

                    
            } for doc in results
        ]

        return{
            "answer":response.content,
            "sources":sources,
            "confidence":1.0
        }