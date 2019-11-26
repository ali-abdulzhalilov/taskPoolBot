from sqlalchemy import Column, Integer, String
from app.db import Base

class Chat(Base):
    __tablename__ = 'chats'

    id = Column(Integer, primary_key=True)
    name = Column(Integer)

    def __repr__(self):
        return f'Chat {self.id}'
