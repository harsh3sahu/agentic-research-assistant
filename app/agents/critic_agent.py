
from langchain_core.messages import HumanMessage
from app.agents.llm import llm
from app.prompts.critic_prompt import CRITIC_PROMPT

import re


class CriticAgent:

    def __init__(self):
        self.name = "Critic Agent"

    def critique(
        self,
        query: str,
        answer: str,
        context: str
    ):

        prompt = CRITIC_PROMPT.format(
            query=query,
            answer=answer,
            context=context[:6000]
        )

        try:

            response = llm.invoke(
                [
                    HumanMessage(
                        content=prompt
                    )
                ]
            )

            critique_text = response.content

            confidence = 0.5

            match = re.search(
                r"CONFIDENCE:\s*([0-9]*\.?[0-9]+)",
                critique_text,
                re.IGNORECASE
            )

            if match:
                confidence = float(
                    match.group(1)
                )

                critique_text = critique_text.replace(
                    match.group(0),
                    ""
                ).strip()

            return {
                "status": "success",
                "confidence": confidence,
                "critique": critique_text
            }

        except Exception as e:

            return {
                "status": "error",
                "confidence": 0.0,
                "critique": str(e)
            }


