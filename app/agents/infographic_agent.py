from app.agents.llm import llm
from huggingface_hub import InferenceClient
from app.config import Config
from google import genai
import os
from huggingface_hub import InferenceClient


from app.prompts.infographic_prompt import (
    INFOGRAPHIC_PROMPT
)


class InfographicAgent:

    def __init__(self):

        self.name = (
            "Infographic Agent"
        )
        self.client= genai.Client(
        api_key=Config.GOOGLE_API_KEY
)


    def generate(
        self,
        report: str
    ):

        prompt = (
            INFOGRAPHIC_PROMPT.format(
                report=report
            )
        )

        print("prompt")
        print(prompt)

        image_prompt = llm.invoke(
            prompt
        )

        image_prompt_text=image_prompt.content
        print("image prompt")
        print(image_prompt)

        client = InferenceClient(
            provider="nscale",
            api_key=Config.HF_TOKEN,
        )

        # output is a PIL.Image object
        image = client.text_to_image(
            image_prompt_text,
            model="black-forest-labs/FLUX.1-schnell",
        )

        print("="*50)
        print(image_prompt_text)
#         image_prompt_text=image_prompt.content
#         print("image prompt")
#         print(image_prompt)

#         image = self.client.models.generate_content(
#         model="imagen-4-fast-generate",
#         contents=image_prompt_text
# )

        

        return image


infographic_agent = (
    InfographicAgent()
)



# import os
# from huggingface_hub import InferenceClient

# client = InferenceClient(
#     provider="fal-ai",
#     api_key=os.environ["HF_TOKEN"],
# )

# # output is a PIL.Image object
# image = client.text_to_image(
#     "Astronaut riding a horse",
#     model="black-forest-labs/FLUX.1-dev",
# )