import os
import telebot
from random import random

from app.models import Chat, Task
from app.db import db_session
from app.utils import register_first

bot = telebot.TeleBot(os.getenv("API_TOKEN"))

# =====

@bot.message_handler(commands=['add'], content_types=['text'])
@register_first
def add_task(message):
    chat = Chat.query.filter(Chat.id==message.chat.id).first()

    text = message.text.split(' ', 1)
    if len(text) <= 1:
        bot.send_message(message.chat.id, "Gimme something to work with, man.")
        return

    task = Task(description=text[1], chat_id=chat.id)

    db_session.add(task)
    db_session.commit()

    bot.send_message(message.chat.id, f'Added task "{task}"')

@bot.message_handler(commands=['list'])
@register_first
def list_tasks(message):
    tasks = Task.query.filter(Task.chat_id==message.chat.id).all()

    if len(tasks) == 0:
        bot.send_message(message.chat.id, "There's nothing for you to do.")
        return

    response = []
    response.append('Here are all your tasks:')
    for i in range(len(tasks)):
        response.append('\n')
        response.append(str(i+1))
        response.append('. ')
        response.append(tasks[i].description)

    bot.send_message(message.chat.id, ''.join(response))

@bot.message_handler(commands=['get'])
@register_first
def get_task(message):
    tasks = Task.query.filter(Task.chat_id==message.chat.id).all()

    if len(tasks) == 0:
        bot.send_message(message.chat.id, "There's nothing for you to do.")
        return

    task = tasks[int(random()*len(tasks))]
    db_session.delete(task)
    db_session.commit()

    bot.send_message(
        message.chat.id,
        "Your next mission, should you choose to accept it, is:\n\n" + \
            task.description)

# =====

# /current
# /reject
# /done
# -----
# /delete
# /edit
# -----
# /get <task | task_id>
# /clear

# =====

@bot.message_handler(commands=['start', 'help'])
@register_first
def send_hi(message):
    bot.send_message(message.chat.id, "Hi, I'm TodoPoolBot, <usage>:")

@bot.message_handler(func=lambda m: True)
@register_first
def echo_all(message):
    # get message.chat.id
    # if db.Chat doesnt contain row with this id
    #   create new row

	bot.reply_to(message, message.text)

# =====

bot.polling()
