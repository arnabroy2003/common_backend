import os

from openai import OpenAI
from openai import RateLimitError

from app.services.llm.base_provider import BaseLLMProvider


class GroqProvider(BaseLLMProvider):

    def __init__(self):

        self.api_keys = [
            os.getenv("GROQ_API_KEY_1"),
            os.getenv("GROQ_API_KEY_2"),
            os.getenv("GROQ_API_KEY_3"),
            os.getenv("GROQ_API_KEY_4"),
        ]

        # Remove empty keys
        self.api_keys = [k for k in self.api_keys if k]

        if not self.api_keys:
            raise ValueError("No Groq API keys found.")

    def _get_client(self, api_key):
        return OpenAI(
            api_key=api_key,
            base_url="https://api.groq.com/openai/v1"
        )

    def _chat_completion(self, **kwargs):

        last_error = None

        for index, api_key in enumerate(self.api_keys, start=1):

            client = self._get_client(api_key)

            try:
                print(f"Using Groq Key #{index}")

                return client.chat.completions.create(**kwargs)

            except RateLimitError as e:

                print(f"Groq Key #{index} is rate limited. Trying next key...")

                last_error = e
                continue

            except Exception:
                # Don't hide non-rate-limit errors
                raise

        raise last_error or Exception("All Groq API keys failed.")

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

        response = self._chat_completion(
            model="llama-3.3-70b-versatile",
            messages=messages
        )

        return response.choices[0].message.content

    def generate_raw(
        self,
        system_prompt: str,
        message: str
    ) -> str:

        response = self._chat_completion(
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