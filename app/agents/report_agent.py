from app.agents.llm import llm
from app.vectorstore.vector_store import (
    vector_store
)
from langchain_core.prompts import PromptTemplate
from app.prompts.report_prompt import REPORT_PROMPT


class CorpusReportAgent:

    def __init__(self):

        self.name = (
            "Corpus Report Agent"
        )

        self.max_context = 50000

        self.prompt_template = PromptTemplate(
            template=REPORT_PROMPT,
            input_variables=[
                "corpus_context"
            ]
        )

    def generate_report(self):

        print(
            "\n=== CORPUS REPORT ==="
        )

        results = (
            vector_store.collection.get(
                include=["documents"]
            )
        )

        documents = (
            results.get(
                "documents",
                []
            )
        )

        if not documents:

            return {
                "status": "error",
                "message":
                "No documents found in vector database."
            }

        print(
            f"Chunks Found: "
            f"{len(documents)}"
        )

        # ==========================
        # BUILD CORPUS CONTEXT
        # ==========================

        corpus_context = ""

        used_chunks = 0

        for doc in documents:

            if (
                len(corpus_context)
                >= self.max_context
            ):
                break

            corpus_context += (
                doc + "\n\n"
            )

            used_chunks += 1

        print(
            f"Chunks Used: "
            f"{used_chunks}"
        )

        print(
            f"Context Length: "
            f"{len(corpus_context)}"
        )

        # ==========================
        # REPORT PROMPT
        # ==========================

        prompt=self.prompt_template.format(corpus_context=corpus_context)

        response = llm.invoke(
            prompt
        )

        print(
            "\n=== REPORT GENERATED ==="
        )

        return {
            "status": "success",
            "report":
                response.content,
            "chunks_used":
                used_chunks,
            "context_length":
                len(corpus_context)
        }


corpus_report_agent = (
    CorpusReportAgent()
)