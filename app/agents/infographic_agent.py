from sentence_transformers.base import model
from app.agents.llm import llm
from huggingface_hub import InferenceClient
from app.config import Config
from google import genai
from google.genai import types

from io import BytesIO

from PIL import Image


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

#         response = self.client.models.generate_content(
#         model="gemini-2.5-flash-image",
#         contents=image_prompt_text,
#         config= types.GenerateContentConfig(
#         response_modalities=["TEXT", "IMAGE"]

#     )
# )

        # for candidate in (
        #     response.candidates
        # ):

        #     for part in (
        #         candidate.content.parts
        #     ):

        #         if (
        #             hasattr(
        #                 part,
        #                 "inline_data"
        #             )
        #             and
        #             part.inline_data
        #         ):

        #             image = (
        #                 Image.open(
        #                     BytesIO(
        #                         part.inline_data.data
        #                     )
        #                 )
        #             )

        #             print(
        #                 "Image generated successfully"
        #             )

        #             return image

        # raise ValueError(
        #     "No image found in Gemini response."

            
        # )
        # return 



        client=InferenceClient(provider="nscale",
        api_key=Config.HF_TOKEN
        )

        image=client.text_to_image(image_prompt_text,
        model="black-forest-labs/FLUX.1-schnell"
        )

        print("*"*50)
        print(image_prompt_text)
        print("*"*50)
        return image



infographic_agent=InfographicAgent()    