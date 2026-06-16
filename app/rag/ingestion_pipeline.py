from pathlib import Path

from app.rag.document_loader import document_loader
from app.rag.text_splitter import text_splitter
from app.vectorstore.vector_store import vector_store


class IngestionPipeline:

    def ingest_pdf(self, file_path: str):

        print("="*50)
        print("Vector Count=")
        print(vector_store.count())

        pdf_name = Path(file_path).name

        indexed_files = (
            vector_store.get_indexed_files()
        )

        # =====================================
        # SKIP IF ALREADY INDEXED
        # =====================================

        if pdf_name in indexed_files:

            print(
                f"\nSkipping {pdf_name} "
                "(already indexed)"
            )

            return

        print(
            f"\nLoading PDF: {pdf_name}"
        )

        # =====================================
        # LOAD PDF
        # =====================================

        documents = (
            document_loader.load_pdf(
                file_path
            )
        )

        print(
            f"Pages Loaded: "
            f"{len(documents)}"
        )

        # =====================================
        # CHUNKING
        # =====================================

        chunks = (
            text_splitter.split_documents(
                documents
            )
        )

        print(
            f"Chunks Created: "
            f"{len(chunks)}"
        )

        texts = []

        metadatas = []

        ids = []

        # =====================================
        # PREPARE DATA
        # =====================================

        for index, chunk in enumerate(chunks):

            texts.append(
                chunk["content"]
            )

            metadatas.append(
                chunk["metadata"]
            )

            ids.append(
                f"{pdf_name}_{index}"
            )

        # =====================================
        # STORE IN CHROMA
        # =====================================

        vector_store.add_documents(
            documents=texts,
            metadatas=metadatas,
            ids=ids
        )

        print(
            f"Indexed: {pdf_name}"
        )

        print(
            f"Total Chunks In DB: "
            f"{vector_store.count()}"
        )

    # =========================================
    # INGEST ALL PDFS IN DATA FOLDER
    # =========================================

    def ingest_folder(
        self,
        folder_path="data"
    ):

        pdf_files = list(
            Path(folder_path).glob(
                "*.pdf"
            )
        )

        if not pdf_files:

            print(
                "\nNo PDFs found."
            )

            return

        print(
            f"\nFound "
            f"{len(pdf_files)} PDF(s)"
        )

        for pdf_file in pdf_files:

            self.ingest_pdf(
                str(pdf_file)
            )
        print("="*50)
        print("Vector Count=")
        print(vector_store.count())


ingestion_pipeline = (
    IngestionPipeline()
)