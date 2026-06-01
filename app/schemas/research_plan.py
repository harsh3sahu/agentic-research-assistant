from pydantic import BaseModel

from typing import List

class ResearchPlan(BaseModel):
    research_tasks:List[str]

