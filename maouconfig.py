from telethon import TelegramClient

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
bot_token = os.environ.get("bot_token")

bot = TelegramClient("bot", API_ID, API_HASH)
