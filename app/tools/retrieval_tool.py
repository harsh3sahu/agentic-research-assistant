class RetrievalTool:
    def __init__(self,retriever):
        self.retriever = retriever


    def run (self,query:str,top_k:int=5, min_score:float=0.2):

        results=self.retriever.retrieve(
            query=query,
            top_k=top_k,
            score_threshold=min_score
        )

        if not results:
            return {
                "context":"",
                "sources":[]
            }

        context="\n\n".join(
            [doc["content"] for doc in results]
        )

        sources=[
            {
                "source":doc["metadata"].get("source_file","unknown"),

                "page":doc["metadata"].get("page","unknown"),

                "score":doc["similarity_score"]

            }

            for doc in results
        ]

        return {
            "context":context,
            "sources":sources
        }