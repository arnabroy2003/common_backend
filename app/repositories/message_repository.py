from sqlalchemy.orm import Session

from app.models.message import Message


class MessageRepository:

    def save_message(
        self,
        db: Session,
        user: str,
        role: str,
        content: str
    ) -> Message:

        message = Message(
            user=user,
            role=role,
            content=content
        )

        db.add(message)
        db.commit()
        db.refresh(message)

        return message

    def get_recent_messages(
        self,
        db: Session,
        limit: int = 30
    ):
        """
        Returns the latest conversation from everyone.
        Common has one shared conversation history.
        """

        messages = (
            db.query(Message)
            .order_by(Message.created_at.desc())
            .limit(limit)
            .all()
        )

        messages.reverse()

        return messages

    def get_messages_by_user(
        self,
        db: Session,
        user: str,
        limit: int = 30
    ):
        """
        Returns messages from one user only.
        Useful for future features.
        """

        messages = (
            db.query(Message)
            .filter(Message.user == user)
            .order_by(Message.created_at.desc())
            .limit(limit)
            .all()
        )

        messages.reverse()

        return messages