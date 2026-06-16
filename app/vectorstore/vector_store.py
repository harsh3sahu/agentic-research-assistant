from app.vectorstore.chroma_manager import chroma_manager

from app.rag.embedding_manager import embedding_manager

class VectorStore:
    def __init__(self):
        self.collection=(chroma_manager.collection)


    def add_documents(self,documents:list[str],metadatas:list[dict],ids:list[str]):
        embeddings=(embedding_manager.generate_embeddings(documents))

        self.collection.add(
            documents=documents,
            embeddings=embeddings.tolist(),
            metadatas=metadatas,
            ids=ids
        )

    def count(self):
        return self.collection.count()
    


    
    def clear(self):

        ids = self.collection.get()["ids"]

        if ids:

            self.collection.delete(
                ids=ids
            )

        print("Vector DB cleared.")


    def get_indexed_files(self):

        data = self.collection.get(
            include=["metadatas"]
        )

        files = set()

        for metadata in data["metadatas"]:

            if metadata:

                files.add(
                    metadata.get(
                        "source_file"
                    )
                )

        return files

vector_store=VectorStore()



