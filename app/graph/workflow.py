from langgraph.graph import StateGraph,END

from app.graph.agent_state import AgentState

from app.graph.nodes import router_node,rag_node,web_node,summarizer_node,critic_node

workflow = StateGraph(AgentState)



workflow.add_node(
    "router",
    router_node
)

workflow.add_node(
    "rag",
    rag_node
)

workflow.add_node(
    "web",
    web_node
)

workflow.add_node(
    "summarizer",
    summarizer_node
)

workflow.add_node(
    "critic",
    critic_node
)

workflow.set_entry_point("router")

def route_decision(state):
    return state["route"]

workflow.add_conditional_edges(
    "router",route_decision,
    {
        "rag":"rag",
        "web":"web"
    }
)

workflow.add_edge("rag","summarizer")

workflow.add_edge("web","summarizer")

workflow.add_edge("summarizer","critic")

workflow.add_edge("critic",END)

graph = workflow.compile()