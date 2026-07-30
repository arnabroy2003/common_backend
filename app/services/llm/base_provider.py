from abc import ABC, abstractmethod


class BaseLLMProvider(ABC):

    @abstractmethod
    def generate_response(self, user: str, message: str) -> str:
        pass