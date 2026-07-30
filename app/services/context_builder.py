from app.personality.behavior_rules import BEHAVIOR_RULES
from app.personality.common_personality import COMMON_PERSONALITY
from app.personality.response_rules import RESPONSE_RULES
from app.prompts.common_identity import COMMON_IDENTITY
from app.profiles.profile_loader import ProfileLoader


class ContextBuilder:

    def __init__(self):
        self.profile_loader = ProfileLoader()

    def build(
        self,
        user: str,
        memories: list,
        history: list
    ) -> dict:

        profiles = self.profile_loader.get_all_profiles()

        return {

            # ==========================
            # Common
            # ==========================

            "identity": COMMON_IDENTITY,

            "personality": COMMON_PERSONALITY,

            "behavior": BEHAVIOR_RULES,

            "response_rules": RESPONSE_RULES,

            # ==========================
            # Conversation
            # ==========================

            "current_speaker": user,

            # ==========================
            # People Common Knows
            # ==========================

            "profiles": profiles,

            # ==========================
            # Shared Memory
            # ==========================

            "memories": memories,

            # ==========================
            # Shared Conversation
            # ==========================

            "history": history

        }