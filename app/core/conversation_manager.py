from collections import defaultdict


class ConversationManager:

    def __init__(self):
        self.conversations = defaultdict(list)

    def add_user_message(self, user: str, message: str):
        self.conversations[user].append(
            {
                "role": "user",
                "content": message
            }
        )

    def add_assistant_message(self, user: str, message: str):
        self.conversations[user].append(
            {
                "role": "assistant",
                "content": message
            }
        )

    def get_messages(self, user: str):
        return self.conversations[user][-10:]