import os
import telebot
from app import bot
from app.utils import register

# =====

@bot.message_handler(commands=['add'])
@register
def add_task(message):
    bot.send_message(message.chat.id, "Added task <task>")

@bot.message_handler(commands=['list'])
@register
def list_tasks(message):
    bot.send_message(message.chat.id, "Here are all your tasks")

@bot.message_handler(commands=['get'])
@register
def get_task(message):
    bot.send_message(message.chat.id, "Your next mission, should you choose to accept it, is: <task> / Wow, there is nothing for you to do at the moment. Lucky you.")

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
@register
def send_hi(message):
    bot.send_message(message.chat.id, "Hi, I'm TodoPoolBot, <usage>:")

@bot.message_handler(func=lambda m: True)
@register
def echo_all(message):
    # get message.chat.id
    # if db.Chat doesnt contain row with this id
    #   create new row

	bot.reply_to(message, message.text)

# =====

bot.polling()
