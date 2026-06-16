import os
from pathlib import Path

import streamlit as st

from app.graph.workflow import graph


# ==========================================
# CONFIG
# ==========================================

DATA_DIR = "data"

os.makedirs(
    DATA_DIR,
    exist_ok=True
)


# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Agentic Research Assistant",
    page_icon="🤖",
    layout="wide"
)


# ==========================================
# HEADER SECTION
# ==========================================

st.title(
    "Agentic Research Assistant"
)

left_col, right_col = st.columns(
    [3, 1]
)

with left_col:

    st.markdown(
        """
### Powered by:

- LangGraph
- ChromaDB
- GROQ
- Tavily
"""
    )

with right_col:

    st.markdown(
        "### 📄 Upload PDFs"
    )

    uploaded_files = (
        st.file_uploader(
            "",
            type=["pdf"],
            accept_multiple_files=True,
            label_visibility="collapsed"
        )
    )

    if uploaded_files:

        saved_files = []

        for uploaded_file in uploaded_files:

            save_path = (
                Path(DATA_DIR)
                / uploaded_file.name
            )

            with open(
                save_path,
                "wb"
            ) as f:

                f.write(
                    uploaded_file.getbuffer()
                )

            saved_files.append(
                uploaded_file.name
            )

        st.success(
            f"{len(saved_files)} PDF(s) uploaded successfully."
        )


# ==========================================
# AVAILABLE PDFS
# ==========================================

pdf_files = list(
    Path(DATA_DIR).glob("*.pdf")
)

if pdf_files:

    with st.expander(
        f"📚 Available PDFs ({len(pdf_files)})",
        expanded=False
    ):

        for pdf in sorted(
            pdf_files,
            key=lambda x: x.name.lower()
        ):

            st.write(
                f"• {pdf.name}"
            )


st.divider()


# ==========================================
# QUERY INPUT
# ==========================================

query = st.text_area(
    "Ask a research question",
    height=150
)


# ==========================================
# RESEARCH BUTTON
# ==========================================

if st.button("Research"):

    if query.strip():

        with st.spinner(
            "Running agent workflow..."
        ):

            result = graph.invoke(
                {
                    "query": query,
                    "route": "",
                    "context": "",
                    "answer": "",
                    "confidence": 0.0,
                    "critique": "",
                    "sources": []
                }
            )

        st.success(
            "Research Complete"
        )

        # ==================================
        # RESULT
        # ==================================

        st.subheader(
            "Result"
        )

        output = (
            result.get("report")
            or result.get("answer")
            or "No output generated."
        )

        st.write(
            output
        )

        # ==================================
        # REVISED ANSWER
        # ==================================

        st.subheader(
            "Revised Answer"
        )

        output2 = (
            result.get("final_ans")
            or "No output generated."
        )

        st.write(
            output2
        )

        # ==================================
        # CONFIDENCE
        # ==================================

        st.subheader(
            "Confidence"
        )

        st.metric(
            "Score",
            round(
                result.get(
                    "confidence",
                    0.0
                ),
                2
            )
        )

        # ==================================
        # CRITIQUE
        # ==================================

        st.subheader(
            "Critique"
        )

        st.write(
            result.get(
                "critique",
                "No critique available."
            )
        )

        # ==================================
        # SOURCES
        # ==================================

        st.subheader(
            "Sources"
        )

        sources = result.get(
            "sources",
            []
        )

        unique_sources = {}

        for source in sources:

            source_name = (
                source.get("source")
                or source.get("title")
                or "Unknown Source"
            )

            if (
                source_name
                not in unique_sources
            ):

                unique_sources[
                    source_name
                ] = source

        deduped_sources = list(
            unique_sources.values()
        )

        if deduped_sources:

            with st.expander(
                f"View Sources ({len(deduped_sources)})",
                expanded=False
            ):

                for source in deduped_sources:

                    st.write(
                        source
                    )

        else:

            st.info(
                "No sources available."
            )