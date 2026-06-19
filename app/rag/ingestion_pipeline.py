from pathlib import Path

from app.rag.document_loader import document_loader
from app.rag.text_splitter import text_splitter
from app.vectorstore.vector_store import vector_store





class IngestionPipeline:


    def __init__(self):
        self.name="Ingestion Pipeline"

    def ingest_pdf(self,file_path:str):

        pdf_name=Path(file_path).name

        indexed_files=vector_store.get_indexed_files()

        if pdf_name in indexed_files:

            # skipping this file and return
            return
    # loading documents

        documents=document_loader.load_pdf(file_path)

        # now chunking

        chunks=text_splitter.split_documents(documents)
        
      

        texts=[]
        metadatas=[]
        ids=[]

        for index, chunk in enumerate(chunks):
            texts.append(chunk["content"])
            metadatas.append(chunk["metadata"])
            ids.append(f"{pdf_name}_{index}")



        # storing in vector store, the embedding is done by vector store when passed

        vector_store.add_documents(documents=texts,metadatas=metadatas,ids=ids)






    def ingest_folder(self,folder_path="data"):

        pdf_files=list(Path(folder_path).glob("*.pdf"))


        if not pdf_files:
            print("No files found")

            return

        
        for pdf_file in pdf_files:

            self.ingest_pdf(str(pdf_file))

        
        print("-"*50)
        print(f"vectorcount = {vector_store.count()}")



ingestion_pipeline=IngestionPipeline()






        







