from app.agents.llm import llm

from app.prompts.supervisor_prompt import SUPERVISOR_PROMPT

class SupervisorAgent:
    
    def __init__(self):
        self.name=(
            "Supervisor Agent"
        )

    def route(self,query:str):
        prompt=f"""
        {SUPERVISOR_PROMPT}

        User Query:
        {query}
        """
        

        response= llm.invoke(prompt)

        decision=(response.content.strip().lower())

        if"web" in decision:
            return "web"

        return "rag"

    
        
        
        