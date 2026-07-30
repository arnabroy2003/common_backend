import os
from dotenv import load_dotenv

load_dotenv()

from openai import OpenAI

from app.services.llm.base_provider import BaseLLMProvider

print("Loaded API Key:", os.getenv("GROQ_API_KEY"))


class GroqProvider(BaseLLMProvider):

    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("GROQ_API_KEY"),
            base_url="https://api.groq.com/openai/v1"
        )

    def generate_response(
        self,
        system_prompt: str,
        history: list
    ) -> str:

        messages = [
            {
                "role": "system",
                "content": system_prompt
            }
        ]

        messages.extend(history)

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages
        )

        return response.choices[0].message.content

    def generate_raw(
        self,
        system_prompt: str,
        message: str
    ) -> str:

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            response_format={
                "type": "json_object"
            },
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

        return response.choices[0].message.content