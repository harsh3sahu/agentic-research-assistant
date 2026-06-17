import os
from pathlib import Path
import streamlit as st
from app.graph.workflow import graph
from app.rag.ingestion_pipeline import ingestion_pipeline
from app.agents.report_agent import report_agent
from app.config import Config
from app.agents.infographic_agent import infographic_agent

os.makedirs(Config.DATA_DIR, exist_ok=True)

st.set_page_config(page_title="Agentic Research Assistant",
page_icon="🤖",
layout="wide"
)

st.title("🤖Agentic Research Assistant")

left_col,right_col=st.columns([3,1])

with left_col:
    st.markdown("""
    Powered by:
    -LangGraph\n
    -ChromaDB\n
    -GROQ \n
    -Tavily \n


    """)

with right_col:

    st.markdown("#### 📄 Upload pdfs")

    uploaded_files=(st.file_uploader(
        "",
        type=["pdf"],
        accept_multiple_files=True,
        label_visibility="collapsed"
    ))


    if uploaded_files:

        saved_files=[]

        with st.spinner("Uploading and indexing PDF's..."):

            for uploaded_file in uploaded_files:
                save_path=Path(Config.DATA_DIR)/uploaded_file.name

                with open(save_path,"wb") as f:

                    f.write(uploaded_file.getbuffer())

                saved_files.append(uploaded_file.name)


            ingestion_pipeline.ingest_folder(Config.DATA_DIR)

        st.success(f"{len(saved_files)} PDF's uploaded and indexed successfully!")


pdf_files=list(Path(Config.DATA_DIR).glob("*.pdf"))

if pdf_files:

    with st.expander(f"Available PDFs ({len(pdf_files)})",expanded=False):

        for pdf in pdf_files:
            st.write(f"{pdf.name}")



st.divider()
left_col,right_col=st.columns([3,1])
with left_col:
    query= st.text_area("Ask a research Question", height=150)


with right_col:
    button_report=st.button("generate a report from PDFs")
    image_button=st.button("Genrate Infographic")
    

if st.button("research"):

    if query.strip():
        with st.spinner("Running agent Workflow...."):
            result= graph.invoke({
                "query":query
            })

    st.success("Result")

    output= result.get("report") or result.get("answer") or "No output Generated"

    st.write(output)


    st.subheader("Revised Answer")

    output2=result.get("final_ans") or "No Output generated"

    st.write(output2)

    st.subheader("confidence")

    st.metric("score", result.get("confidence",0.0))


    st.subheader("critique")
    st.write(result.get("critique", "no critique available"))


    st.subheader("sources")
    sources=result.get("sources",[])

    unique_sources={}

    for source in sources:

        source_name=source.get("sources") or source.get("title") or "unknown source"

        if source_name not in unique_sources:
            unique_sources[source_name]=source

        
    final_sources=list(unique_sources.values())


    if final_sources:
        with st.expander(
            f"View Sources ({len(final_sources)})",
            expanded=False
        ):

            for source in final_sources:
                st.write(source)

    else:
        st.info("no sources available")






if button_report:

    result=(report_agent.generate_report())

    st.write(result["report"])

if image_button:

    with st.spinner(
        "Generating infographic..."
    ):

        report_result = (
            report_agent.generate_report()
        )

        if (
            report_result["status"]
            != "success"
        ):

            st.error(
                report_result["message"]
            )

        else:
            image= infographic_agent.generate(report_result)
            st.image(image,
                caption="Generated Infographic",
                use_container_width=True)


