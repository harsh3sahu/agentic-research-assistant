from langchain_core.messages import HumanMessage
from app.agents.llm import llm
from app.prompts.critic_prompt import CRITIC_PROMPT


class CriticAgent:
    def __init__(self):
        self.name=(
            "Critic Agent"
        )


    def critique(self,query:str,answer:str,context:str):

        prompt=(
            CRITIC_PROMPT.format(query=query,answer=answer,context=context[:6000])

        )

        try:
            response=llm.invoke(
                [
                    HumanMessage(content=prompt)
                ]
            )

            critique_text= response.content
            confidence=0.5

            try:
                if ("CONFIDENCE:" in critique_text):

                    confidence_text=critique_text.split("CONFIDENCE:")[1].split("\n")[0].strip()

                    confidence=float(confidence_text)

            except :
                pass


            return {
                "status":"success",
                "confidence":confidence,
                "critique":critique_text
            }

        except Exception as e:
            return {
                "status":"error",
                "confidence":0.0,
                "critique":str(e)
            }
