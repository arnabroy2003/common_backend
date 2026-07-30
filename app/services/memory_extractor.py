import json

from app.prompts.memory_extractor_prompt import MEMORY_EXTRACTION_PROMPT
from app.services.llm.cohere_provider import CohereProvider




class MemoryExtractor:

    def __init__(self):

        self.provider = CohereProvider()

    def extract(self, text: str):

        try:

            response = self.provider.generate_raw(
                system_prompt=MEMORY_EXTRACTION_PROMPT,
                message=text
            )

            return json.loads(response)

        except Exception:

            return {
                "should_save": False
            }