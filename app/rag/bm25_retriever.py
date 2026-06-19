from attr.filters import include
from rank_bm25 import BM25Okapi
from app.vectorstore.vector_store import vector_store



class BM25Retriever:

    def __init__(self):

        self.documents=[]
        self.metadatas=[]
        self.ids=[]



        self.bm25=None

        self.refresh_index()


    def refresh_index(self):

        data =vector_store.collection.get(include=["documents","metadatas"])


        self.documents=data["documents"]
        self.metadatas=data["metadatas"]
        self.ids=data["ids"]

        
        print(type(self.documents))
        print(type(self.documents[0]))


        tokenized_docs=[
            doc.lower().split()
            for doc in self.documents
        ]


        self.bm25=BM25Okapi(tokenized_docs)

        print(f"BM25 indexed {len(self.documents)} chunks")




    def retrieve(self,query:str,top_k:int=5):

        # self.refresh_index()

        scores=self.bm25.get_scores(
            query.lower().split()
        )

        ranked=sorted(
            enumerate(scores),
            key=lambda x : x[1], reverse=True
        )[:top_k]

        results=[]


        for index,score in ranked:
            results.append({

                "id":self.ids[index],
                "content":self.documents[index],
                "metadata":self.metadatas[index],
                "bm25_score":score


            })


        return results

bm25_retriever=BM25Retriever()


