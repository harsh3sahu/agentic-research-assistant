from langchain_core.outputs import chat_result
from app.agents.supervisor_agent import SupervisorAgent

from app.tools.rag_tool import RAGTool
from app.rag.retriever import retriever

from app.tools.web_search_tool import WebSearchTool

from app.agents.summarizer_agent import SummarizerAgent

from app.agents.critic_agent import CriticAgent

from app.agents.planner_agent import PlannerAgent

from app.agents.research_synthesizer_agent import ResearchSynthesizerAgent

from app.agents.mode_router_agent import ModeRouterAgent

mode_router= ModeRouterAgent()

research_synthesizer=ResearchSynthesizerAgent()

planner=PlannerAgent()

critic= CriticAgent()

summarizer = SummarizerAgent()


web_tool = WebSearchTool()

rag_tool = RAGTool(retriever)

supervisor=SupervisorAgent()


#  NODES----------------------------


def mode_router_node(state):
    mode=mode_router.route(state["query"])

    state["mode"]=mode

    return state



def planner_node(state):
    plan=planner.plan(state["query"])

    state["research_tasks"]=plan.research_tasks


    return state




def research_tasks_node(state):

    

    
    findings=[]

    all_sources=[]

    for task in state["research_tasks"]:
        result = rag_tool.run(task)
        context=result.get("context","")

        if  len(context.strip())<300 or len(result["sources"]) == 0:

            
            result = web_tool.run(task)

        all_sources.extend(result.get("sources",[]))

        findings.append(
            f"""

            Task:{task}

            Findings:{result["context"]}

            """
        )

    state["research_findings"]="\n\n".join(findings)

    state["context"]= state["research_findings"]

    unique_sources=[]
    seen=set()

    for source in all_sources:
        key=str(source)
        if key not in seen :
            seen.add(key)
            unique_sources.append(source)


    state["sources"]=unique_sources

    # result = rag_tool.run(task)


    # context = result.get("context","")

    

    return state


def rag_node(state):
    task=state["query"]

    result = rag_tool.run(task)

    context = result["context"]

    if len(context.strip()) < 100:

        result = web_tool.run(task)

    state["context"]= result["context"]

    state["sources"]= result["sources"]

    return state



def web_node(state):
    result=web_tool.run(state["query"])

    state["context"]=result["context"]

    state["sources"]=result["sources"]

    return state




def synthesizer_node(state):

    print("\n=== SYNTHESIZER INPUT ===")
    print(state["research_findings"][:2000])
    print("=========================")


    report= research_synthesizer.synthesize(state["research_findings"])

    state["report"]=report

    

    return state





    


def supervisor_node(state):

    route= supervisor.route(
        state["query"]
    )

    state["route"]=route

    return state






def summarizer_node(state):
    result = summarizer.summarize(
        query=state["query"],
        context=state["context"]
    )

    state["answer"]=result.get("summary","")

    return state






def critic_node(state):
    answer = state.get("answer","")
    if not answer:
        answer=state.get("report","")

    print("\n=== ANSWER SENT TO CRITIC ===")
    print(answer)
    print("============================")

    

    result = critic.critique(
    query=state["query"],
        answer=answer,
        context=state.get(
            "context",
            ""
        )
    )

    state["confidence"]=result.get("confidence",0.0)

    state["critique"]=result.get("critique","")

    

    return state
    











