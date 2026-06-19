from app.vectorstore.vector_store import vector_store
from app.rag.embedding_manager import embedding_manager



class Retriever:

    def __init__(self):
        self.vector_store=vector_store
        self.embedding_manager = embedding_manager


    def retrieve(self,query:str,top_k:int=5):

        print(f"retrieving for query{query}")


        query_embedding= self.embedding_manager.generate_embeddings([query])[0]



        results= self.vector_store.collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=top_k
        )

        retrieved_docs=[]

        if results["documents"] and results["documents"][0]:

            documents=results["documents"][0]
            metadatas=results["metadatas"][0]
            distances=results["distances"][0]

            ids=results["ids"][0]


            for i,(doc_id,document,metadata,distance) in enumerate (zip(ids,documents,metadatas,distances)):

                

                retrieved_docs.append({
                    "id":doc_id,
                    "content":document,
                    "metadata":metadata,
                    "distance":distance,
                    "rank":i+1
                })
                    
        

        return retrieved_docs



retriever=Retriever()



