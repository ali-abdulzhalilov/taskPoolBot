from app.models import Chat
from app.db import db_session

def register_first(func):
    def wrapper_register(*args, **kwargs):
        message = args[0]
        if message is not None:
            chat = message.chat
            if Chat.query.filter(Chat.id==chat.id).first() is None:
                name = chat.first_name if chat.type == 'private' else chat.title
                new_chat = Chat(id=chat.id, name=name)
                db_session.add(new_chat)
                db_session.commit()
                
        func(*args, **kwargs)
    return wrapper_register
