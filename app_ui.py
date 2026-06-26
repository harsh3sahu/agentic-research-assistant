
import os
from pathlib import Path
import streamlit as st



from app.graph.workflow import graph
from app.rag.ingestion_pipeline import ingestion_pipeline
from app.agents.report_agent import report_agent
from app.agents.infographic_agent import infographic_agent
from app.config import Config

os.makedirs(Config.DATA_DIR,exist_ok=True)


if "indexed_files" not in st.session_state:
    st.session_state.indexed_files=set()


st.set_page_config(page_title="Agentic Research Assistant",
page_icon="🤖",
layout="wide"

)

st.title("🤖 Agentic Research Assistant")

left_col,right_col =st.columns([3,1])

with left_col:
    st.markdown(
        """

### Powered by

- LangGraph
- ChromaDB
- GROQ
- Tavily
        """
    )

with right_col:
    st.markdown("#### 📄Upload Pdfs")

    uploaded_files= st.file_uploader("", type=["pdf"], accept_multiple_files=True,label_visibility="collapsed")


    if uploaded_files:

        new_files_uploaded=False

        saved_files=[]

        for uploaded_file in uploaded_files:

            if uploaded_file.name not in st.session_state.indexed_files:
                save_path=Path(Config.DATA_DIR)/uploaded_file.name

                with open(save_path,"wb") as f:

                    f.write(uploaded_file.getbuffer())

                saved_files.append(uploaded_file.name)

                st.session_state.indexed_files.add(uploaded_file.name)
                    

                new_files_uploaded=True

        if new_files_uploaded:
            with st.spinner("Uploading and indexing pdfs"):
                ingestion_pipeline.ingest_folder(Config.DATA_DIR)

            st.success(f"{len(saved_files)} Pdf's uploaded successfully.")



pdf_files=list(Path(Config.DATA_DIR).glob("*.pdf"))


if pdf_files:
    with st.expander(f"Available Pdfs ({len(pdf_files)})",
    expanded=False
    ):
        for pdf in sorted(pdf_files,key=lambda x: x.name.lower()):

            st.write(pdf.name)

st.divider()




left_col,right_col=st.columns([3,1])


with left_col:

    query=st.text_area("Ask a Research Question",height=150)


with right_col:

    button_report=st.button("📄 Generate Report")

    image_button= st.button("Generate Infographic")



if st.button("🔍Research"):

    if not query.strip():

        st.warning("Please enter a research question")



    else:
        with st.spinner("Running agent workflow ...."):

            result = graph.invoke({
                "query":query
            })


        st.success("Research Complete")


        output=result.get("report") or result.get("answer") or "No output Generated"

        st.subheader("Result")

        st.write(output)

        st.subheader("Revised Answer")

        st.write(result.get("final_ans", "No output generated"))


        st.subheader("confidence")

        st.metric("score", round(result.get("confidence",0.0),2))


        # critic

        st.subheader("Critique")

        st.write(result.get("critique", "No critique available."))


        # sources


        st.subheader("sources")
        sources=result.get("sources",[])

        unique_sources={}

        for source in sources:

            source_name=source.get("source") or source.get("title") or "unknown source"

            if source_name not in unique_sources:
                unique_sources[source_name]=source


        final_sources=list(unique_sources.values())


        if final_sources:
            with st.expander(f"View sources ({len(final_sources)})"):

                for source in final_sources:
                    st.write(source)


        else:
            st.info("No sources available")



if button_report:
    try:

        with st.spinner("Generating Report..."):

            result = report_agent.generate_report()


        if result["status"]=="success":

            st.subheader("Report")

            st.write(result["report"])


        else:
            st.error(result["message"])


    except Exception as e:

        st.error(f"Report Generation Failed:{e}")


if image_button:

    try:
        with st.spinner("Generating infographic...."):

            report_text=""

            if os.path.exists("report.txt"):

                with open("report.txt", "r", encoding="utf-8") as f:


                    report_text=f.read()


            if len(report_text.strip())<500:

                report_result= report_agent.generate_report()


                if (report_result["status"]!="success"):
                    st.error(report_result["message"])


                
                    st.stop()


                report_text=report_result["report"]



            image=infographic_agent.generate(report_text)

            st.image(image,caption="Genrated Infographic image", use_container_width=True)


    except Exception as e:

        st.error(f"Infographic Generation Failed:{e}")


    


        



