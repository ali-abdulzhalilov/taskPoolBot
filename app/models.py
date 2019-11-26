from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base

class Chat(Base):
    __tablename__ = 'chats'

    id = Column(Integer, primary_key=True)
    name = Column(Integer)
    # created_at
    # last_seen

    tasks = relationship('Task', backref='chat', lazy=True)

    def __repr__(self):
        return f'<Chat {self.id} : {self.name}>'

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    description = Column(String(300))
    chat_id = Column(Integer, ForeignKey('chats.id'), index=True, nullable=False)

    def __repr__(self):
        return f'<Task {self.id} : {self.description}>'
