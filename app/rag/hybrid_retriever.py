from app.rag.retriever import retriever
from app.rag.bm25_retriever import bm25_retriever


class HybridRetriever:

    def retrieve(
        self,
        query:str,
        top_k:int=5
    ):

        semantic_results = retriever.retrieve(
            query=query,
            top_k=10
        )

        bm25_results = bm25_retriever.retrieve(
            query=query,
            top_k=10
        )

        return {
            "semantic": semantic_results,
            "bm25": bm25_results
        }


hybrid_retriever = HybridRetriever()