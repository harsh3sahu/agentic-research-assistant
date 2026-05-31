from sentence_transformers import SentenceTransformer
from app.config import Config

class EmbeddingManager:
    def __init__(self):
        self.model=SentenceTransformer(
            Config.EMBEDDING_MODEL
        )

    def generate_embeddings(self,texts:list[str]):
        return self.model.encode(texts, show_progress_bar=False)


embedding_manager=EmbeddingManager()