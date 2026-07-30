from sqlalchemy.orm import Session

from app.repositories.memory_repository import MemoryRepository
from app.repositories.message_repository import MessageRepository
from app.schemas.chat_schema import ChatRequest
from app.services.context_builder import ContextBuilder
from app.services.llm.groq_provider import GroqProvider
from app.services.memory_extractor import MemoryExtractor
from app.services.prompt_builder import PromptBuilder


class ChatService:

    def __init__(self):

        self.provider = GroqProvider()

        self.context_builder = ContextBuilder()

        self.prompt_builder = PromptBuilder()

        self.message_repository = MessageRepository()

        self.memory_repository = MemoryRepository()

        self.memory_extractor = MemoryExtractor()

    def chat(
        self,
        db: Session,
        request: ChatRequest
    ):

        # --------------------------------------------------
        # STEP 1 : Save current user's message
        # --------------------------------------------------

        self.message_repository.save_message(
            db=db,
            user=request.user,
            role="user",
            content=request.message
        )

        # --------------------------------------------------
        # STEP 2 : Extract long-term memory
        # --------------------------------------------------

        memory = self.memory_extractor.extract(
            request.message
        )

        if memory.get("should_save"):

            self.memory_repository.save_memory(
                db=db,
                user=request.user,
                memory_type=memory["memory_type"],
                key=memory["key"],
                value=memory["value"],
                importance=memory["importance"],
                confidence=memory["confidence"]
            )

        # --------------------------------------------------
        # STEP 3 : Load shared conversation history
        # --------------------------------------------------

        messages = self.message_repository.get_recent_messages(
            db=db
        )

        history = []

        for message in messages:

            if message.role == "user":
                history.append(
                    {
                        "role": "user",
                        "content": f"[{message.user}] {message.content}"
                    }
                )

            else:
                history.append(
                    {
                        "role": "assistant",
                        "content": message.content
                    }
                )

        # --------------------------------------------------
        # STEP 4 : Load all memories
        # --------------------------------------------------

        memories = self.memory_repository.get_all_memories(
            db=db
        )

        # --------------------------------------------------
        # STEP 5 : Build context
        # --------------------------------------------------

        context = self.context_builder.build(
            user=request.user,
            memories=memories,
            history=history
        )

        # --------------------------------------------------
        # STEP 6 : Build system prompt
        # --------------------------------------------------

        system_prompt = self.prompt_builder.build(
            context
        )

        # --------------------------------------------------
        # STEP 7 : Generate AI response
        # --------------------------------------------------

        reply = self.provider.generate_response(
            system_prompt=system_prompt,
            history=history
        )

        # --------------------------------------------------
        # STEP 8 : Save Common's reply
        # --------------------------------------------------

        self.message_repository.save_message(
            db=db,
            user="common",
            role="assistant",
            content=reply
        )

        return reply