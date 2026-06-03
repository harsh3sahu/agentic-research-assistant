from langgraph.graph import StateGraph,END

from app.graph.agent_state import AgentState

from app.graph.nodes import supervisor_node,rag_node,web_node,summarizer_node,critic_node,mode_router_node,planner_node,research_tasks_node,synthesizer_node

workflow = StateGraph(AgentState)



workflow.add_node(
    "supervisor",
    supervisor_node
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

workflow.add_node(
    "mode_router",
    mode_router_node
)

workflow.add_node(
    "planner",
    planner_node
)

workflow.add_node(
    "research",
    research_tasks_node
)

workflow.add_node(
    "synthesizer",
    synthesizer_node
)

workflow.set_entry_point("mode_router")

def mode_decision(state):

    return state["mode"]


def route_decision(state):
    return state["route"]

workflow.add_conditional_edges(
    "mode_router",mode_decision,{
        "qa":"supervisor",
        "research":"planner"
    }
)



workflow.add_conditional_edges(
    "supervisor",route_decision,
    {
        "rag":"rag",
        "web":"web"
    }
)

workflow.add_edge("rag","summarizer")

workflow.add_edge("web","summarizer")

workflow.add_edge("summarizer","critic")

workflow.add_edge("planner","research")

workflow.add_edge("research", "synthesizer")

workflow.add_edge("synthesizer", "critic")

workflow.add_edge("critic",END)

graph = workflow.compile()