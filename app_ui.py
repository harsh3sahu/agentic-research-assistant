import streamlit as st

from app.graph.workflow import graph

st.set_page_config(
    page_title="Agentic Research Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("Agentic Research Assistant")

st.markdown(
    """
    Powered by:
    -Langgraph
    -ChromaDB
    -GROQ
    -Tavily
    """
)

query=st.text_area("ask a research question", height=150)

if st.button("research"):
    if query.strip():

        with st.spinner("running agent workflow ..."):
            result = graph.invoke(
                {
                "query":query,
                "route" : "",
                "context":"",
                "answer":"",
                "confidence":0.0,
                "critique":"",
                "sources":[]
                }

            )

        st.success("Research Complete")
        
        st.subheader("answer")

        st.write(result["answer"])

        st.subheader("confidence")

        st.metric(
            "score",
            round(result["confidence"],2)
        )

        st.subheader("critique")

        st.write(result["critique"])

        st.subheader("Sources")

        sources = result.get("sources",[])

        if sources:
            
            for source in sources:
                st.write (source)

        else:
            st.info("No sources available.")


