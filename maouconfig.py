from telethon import TelegramClient
import os

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
bot_token = os.environ.get("bot_token")
my_id = os.environ.get("my_id")

bot = TelegramClient("bot", API_ID, API_HASH)
