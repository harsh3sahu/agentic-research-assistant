from pydantic import BaseModel
from langchain_core.prompts import PromptTemplate

from app.agents.llm import llm
from app.prompts.critic_prompt import CRITIC_PROMPT


class CriticResponse(BaseModel):
    confidence: float
    strengths: list[str]
    weaknesses: list[str]
    feedback: str


class CriticAgent:

    def __init__(self):
        self.name = "Critic Agent"

        self.structured_llm = (
            llm.with_structured_output(
                CriticResponse
            )
        )

        self.prompt_template = PromptTemplate(
            template=CRITIC_PROMPT,
            input_variables=[
                "query",
                "answer",
                "context"
            ]
        )

    def critique(
        self,
        query: str,
        answer: str,
        context: str
    ):

        prompt = self.prompt_template.format(
            query=query,
            answer=answer,
            context=context[:6000]
        )

        try:

            result = self.structured_llm.invoke(
                prompt
            )

            # print("======================critique confidence============")
            print(f"confidence={result.confidence}")
            # print(f"CONFIDENCE={result.CONFIDENCE}")
            # print("======================================================")

            critique_text = f"""
STRENGTHS:
{chr(10).join(f"- {s}" for s in result.strengths)}

WEAKNESSES:
{chr(10).join(f"- {w}" for w in result.weaknesses)}

FEEDBACK:
{result.feedback}
""".strip()

            return {
                "status": "success",
                "confidence": result.confidence,
                "critique": critique_text
            }

        except Exception as e:

            return {
                "status": "error",
                "confidence": 0.0,
                "critique": str(e)
            }