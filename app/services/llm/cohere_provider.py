import os

import cohere
from dotenv import load_dotenv

# from app.services.llm.base_provider import BaseLLMProvider

load_dotenv()


class CohereProvider:

    def __init__(self):

        self.client = cohere.ClientV2(
            api_key=os.getenv("COHERE_API_KEY")
        )

    def generate_raw(
        self,
        system_prompt: str,
        message: str
    ) -> str:

        response = self.client.chat(
            model="command-a-plus-05-2026",
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": message
                }
            ]
        )

        return next(
            item.text
            for item in response.message.content
            if item.type == "text"
        )