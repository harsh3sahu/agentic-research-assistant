from langchain_core.messages import HumanMessage

from app.agents.llm import llm


from app.prompts.planner_prompt import PLANNER_PROMPT

from app.schemas.research_plan import ResearchPlan

class PlannerAgent:
    def __init__ (self):
        self.name="Planner Agent"

        self.structured_llm=llm.with_structured_output(ResearchPlan)


    def plan(self,query:str):
        prompt=PLANNER_PROMPT.format(query=query)

        result  =self.structured_llm.invoke(
            prompt
        )

        return result


