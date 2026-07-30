class PromptBuilder:

    def build(
        self,
        context: dict
    ):

        # ======================================================
        # Profiles
        # ======================================================

        profile_text = ""

        for name, profile in context["profiles"].items():

            profile_text += f"\n{name.upper()} PROFILE\n"

            profile_text += "=" * 60 + "\n"

            for key, value in profile.items():

                profile_text += f"{key}: {value}\n"

            profile_text += "\n"

        # ======================================================
        # Memories
        # ======================================================

        memory_text = ""

        for memory in context["memories"]:

            memory_text += (
                f"[{memory.user}] "
                f"{memory.key}: {memory.value}\n"
            )

        # ======================================================
        # Behavior Rules
        # ======================================================

        behavior_text = ""

        for rule in context["behavior"]:

            behavior_text += f"- {rule}\n"

        # ======================================================
        # Response Rules
        # ======================================================

        response_text = ""

        for key, value in context["response_rules"].items():

            response_text += f"{key}: {value}\n"

        # ======================================================
        # Personality
        # ======================================================

        personality_text = ""

        for key, value in context["personality"].items():

            personality_text += f"{key}: {value}\n"

        # ======================================================
        # Final Prompt
        # ======================================================

        system_prompt = f"""
{context["identity"]}

============================================================
YOUR PERSONALITY
============================================================

{personality_text}

============================================================
BEHAVIOR RULES
============================================================

{behavior_text}

============================================================
RESPONSE STYLE
============================================================

{response_text}

============================================================
CURRENT SPEAKER
============================================================

{context["current_speaker"]}

The current speaker is talking to you.

Remember:

- You personally know BOTH Arnab and Tamasa.
- You are NOT a separate chatbot for each user.
- You are ONE shared friend.
- You remember everyone's conversations.
- You remember everyone's memories.
- You may naturally talk about either person whenever it helps.
- Do not wait for someone to explicitly mention the other's name.
- If suggesting something, use your knowledge of both people naturally.
- Never confuse who is currently speaking.

============================================================
KNOWN PEOPLE
============================================================

{profile_text}

============================================================
LONG TERM MEMORIES
============================================================

{memory_text}
"""

        return system_prompt