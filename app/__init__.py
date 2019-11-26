from dotenv import load_dotenv
load_dotenv()

import os
import telebot
bot = telebot.TeleBot(os.getenv("API_TOKEN"))

from app import routes
