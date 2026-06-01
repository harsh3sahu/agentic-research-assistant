from app.agents.supervisor_agent import SupervisorAgent

from app.tools.rag_tool import RAGTool
from app.rag.retriever import retriever

from app.tools.web_search_tool import WebSearchTool

from app.agents.summarizer_agent import SummarizerAgent

from app.agents.critic_agent import CriticAgent

critic= CriticAgent()

summarizer = SummarizerAgent()


web_tool = WebSearchTool()

rag_tool = RAGTool(retriever)






supervisor=SupervisorAgent()

def router_node(state):

    route= supervisor.route(
        state["query"]
    )

    state["route"]=route

    return state


def rag_node(state):
    result= rag_tool.run(state["query"])

    state["context"]= result["context"]

    state["sources"]= result["sources"]

    return state

def web_node(state):
    result=web_tool.run(state["query"])

    state["context"]=result["context"]

    state["sources"]=result["sources"]

    return state


def summarizer_node(state):
    result = summarizer.summarize(
        query=state["query"],
        context=state["context"]
    )

    state["answer"]=result.get("summary","")

    return state


def critic_node(state):
    result = critic.critique(
        query=state["query"],
        answer=state["answer"],
        context=state["context"]
    )

    state["confidence"]=result.get("confidence",0.0)

    state["critique"]=result.get("critique","")

    return state
    









