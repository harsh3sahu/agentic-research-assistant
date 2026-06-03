from torch._inductor.config import score_fusion_memory_threshold
from app.config import Config

class RAGTool:

    def __init__(self,retriever):
        self.retriever=retriever


    def run (self,query:str,top_k:int=Config.TOP_K, min_score=Config.SCORE_THRESHOLD):

        results = self.retriever.retrieve(query=query,top_k=top_k,score_threshold=min_score)

        if not results :
            return {
                "context":"",
                "sources":[]
            }

        context= "\n\n".join(doc["content"] for doc in results)

        sources=[
            {
                "sources":doc["metadata"].get("source_file","unknown"),
                "page":doc["metadata"].get("page","unknown"),
                "score":doc["similarity_score"]

            }
            for doc in results
        ]

        return {
            "context":context,
            "sources":sources
        }