import chromadb

from app.config import Config

class ChromaManager:
    def __init__(self):
        self.client = chromadb.PersistentClient(path=Config.CHROMA_PATH)


        self.collection=(
            self.client.get_or_create_collection(
                name=Config.COLLECTION_NAME
                # ,
                # metadata={ "hnsw:space": "cosine" }
            )
        )
        print(self.collection.metadata)
chroma_manager = ChromaManager()