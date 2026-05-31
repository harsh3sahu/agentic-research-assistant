from app.rag.document_loader import document_loader
from app.rag.text_splitter import text_splitter
from app.vectorstore.vector_store import vector_store

class IngestionPipeline:

    def ingest_pdf(self,file_path:str):
        print(f"\n Loading Pdf: {file_path}")

        documents=(document_loader.load_pdf(file_path))

        print(f"Pages Loaded: {len(documents)}")

        chunks=(text_splitter.split_documents(documents))

        print(f"chunks created : {len(chunks)}")

        texts=[]
        metadatas=[]
        ids=[]

        for index, chunk in enumerate(chunks):
            texts.append(chunk["content"])
            
            metadatas.append(chunk["metadata"])

            ids.append(f"{file_path}_{index}")

        vector_store.add_documents(documents=texts,metadatas=metadatas,ids=ids)

        print("ingestion completed")

        print(f"total documents : {vector_store.count()}")

ingestion_pipeline= IngestionPipeline()

