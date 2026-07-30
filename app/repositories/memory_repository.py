from sqlalchemy.orm import Session

from app.models.memory import Memory


class MemoryRepository:

    def save_memory(
        self,
        db: Session,
        user: str,
        memory_type: str,
        key: str,
        value: str,
        importance: int,
        confidence: float
    ):

        memory = Memory(
            user=user,
            memory_type=memory_type,
            key=key,
            value=value,
            importance=importance,
            confidence=confidence
        )

        db.add(memory)
        db.commit()
        db.refresh(memory)

        return memory

    def get_all_memories(
        self,
        db: Session
    ):
        """
        Returns every memory from every user.
        Common has access to everyone's memories.
        """

        return (
            db.query(Memory)
            .order_by(
                Memory.importance.desc(),
                Memory.updated_at.desc()
            )
            .all()
        )

    def get_memories_by_user(
        self,
        db: Session,
        user: str
    ):
        """
        Returns memories for one specific user.
        Useful for future features.
        """

        return (
            db.query(Memory)
            .filter(Memory.user == user)
            .order_by(
                Memory.importance.desc(),
                Memory.updated_at.desc()
            )
            .all()
        )