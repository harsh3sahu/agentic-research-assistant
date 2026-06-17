from botocore import model
from app.agents.llm import llm
from huggingface_hub import InferenceClient
from app.config import Config
from google import genai


from app.prompts.infographic_prompt import INFOGRAPHIC_PROMPT

class InfographicAgent:

    def __init__(self):

        self.name="Infographic Agent"

        self.client=genai.Client(api_key=Config.GOOGLE_API_KEY)

    

    def generate(self,report:str):

        prompt=INFOGRAPHIC_PROMPT.format(report=report)

        print("prompt")
        print(prompt)

        

        image_prompt=llm.invoke(prompt)

        image_prompt_text= image_prompt.content

        client=InferenceClient(provider="nscale",
        api_key=Config.HF_TOKEN
        )

        image=client.text_to_image(image_prompt_text,
        model="black-forest-labs/FLUX.1-schnell"
        )

        print("*"*50)
        print(image_prompt_text)
        print("*"*50)



infographic_agent=InfographicAgent()    